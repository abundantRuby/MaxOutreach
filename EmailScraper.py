from googleplaces import GooglePlaces
from colorama import Fore, Style
from bs4 import BeautifulSoup
import re
import requests

LOC = '33.465218, -112.071320'
KEY = 'Painters'
RADIUS = 40000
YOUR_API_KEY = 'AIzaSyA6gKTmIjiZDezLV1GYmwtyP70ww8Up5qM'

unwanted_words = ['landscap', 'excavat', 'roofing', 'decorat', 'garden', 'plumb', 'renovat', 'carpent', 'floor', 'electric', 'pest', 'masonry', 'demolition', 'carpet']
data_list = []
counter = 0
total_places = 0

try:
    google_places = GooglePlaces(YOUR_API_KEY)
    print(f'{Style.BRIGHT}{Fore.GREEN}GooglePlaces Authentication Complete{Style.RESET_ALL}')

    # Initial search
    query_result = google_places.nearby_search(
        location=LOC, keyword=KEY,
        radius=RADIUS, types=[])

    if query_result.has_attributions:
        print(query_result.html_attributions)

    while True:
        for place in query_result.places:
            total_places += 1

            try:
                place.get_details()

                if (place.website) and not any(word in place.name.lower() for word in unwanted_words):
                    website = (place.website)
                    data_list.append(website)
                    counter += 1

            except Exception as e:
                print(f"Error getting details for place '{place.name}': {e}")

        # Check for additional pages of results
        if 'next_page_token' in query_result.raw_response:
            next_page_token = query_result.raw_response['next_page_token']
            query_result = google_places.nearby_search(pagetoken=next_page_token, location=LOC)
        else:
            break

except Exception as e:
    print(f'{Style.BRIGHT}{Fore.RED}GooglePlaces Authentication Failed{Style.RESET_ALL}')
    print(f"Error: {e}")


def clean_email_string(email_str):
    # Use a more restrictive regex pattern to filter out invalid email-like strings
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', email_str)
    
    if email_match:
        # Additional checks to filter out email-like strings with unusual patterns
        email_address = email_match.group()
        if ('@' in email_address) and ('.' in email_address) and (len(email_address) <= 40) and ('png' not in email_address) and ('godaddy' not in email_address) and ('example' not in email_address) and ('townsquare' not in email_address) and ('lato' not in email_address):
            return email_address
    return None


def extract_emails_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        emails = set()
        for text in soup.stripped_strings:
            email = clean_email_string(text)
            if email:
                emails.add(email)

        for mailto_link in soup.find_all('a', href=re.compile(r'^mailto:')):
            email_from_mailto = clean_email_string(mailto_link['href'][7:])
            if email_from_mailto:
                emails.add(email_from_mailto)

        return emails

    except requests.exceptions.RequestException as e:
        return set()
    
def extract_emails_from_data_list(data_list):
    extracted_emails = []
    for website in data_list:
        emails = extract_emails_from_url(website)
        extracted_emails.extend(emails)
    return extracted_emails


extracted_emails = extract_emails_from_data_list(data_list)


print('Total Query Places: ' + str(total_places))
print('Total Results: ' + str(counter))

print(f"{Style.BRIGHT}{Fore.MAGENTA}Extracted Emails{Style.RESET_ALL}")
print(extracted_emails)





































