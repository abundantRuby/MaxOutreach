# --------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- IMPORT LIBRARIES -------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------- #

import requests
from urllib.parse import urlparse, parse_qs, unquote, urljoin
import re
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool
import sys

# --------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- VARIABLES TO EXECUTE ---------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------- #
        
yelp_urls = [ "https://www.yelp.com/search?find_desc=painters&find_loc=Mesa%2C+AZ"]

search_term = "painters"

error_counter = 0

print('test')
sys.exit(1)
print('test')

# --------------------------------------------------------------------------------------------------------------- #
# --------------------------------------- DEFINE FUNCTIONS -------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------- #

def clean_yelp_url(original_url):
    cleaned_url = original_url.split('?')[0]  # Keep only the business URL without query parameters
    return cleaned_url

def get_city_from_url(yelp_url):
    query_params = parse_qs(urlparse(yelp_url).query)
    city = query_params.get('find_loc', [''])[0]
    return city

def get_listing_urls(yelp_url, max_pages=5, results_per_page=50):
    all_listing_urls = set()

    for page in range(max_pages):
        start_offset = page * results_per_page
        city = get_city_from_url(yelp_url)
        api_url = "https://api.yelp.com/v3/businesses/search"

        params = {
            'term': search_term,
            'location': city,
            'limit': results_per_page,
            'offset': start_offset
        }

        headers = {
            'Authorization': 'Bearer pMIqEfqQPOncWCYTIDUDrx3ObCpuCqmAF4hiwAe6WdtDpMHZk-JKwnsZBt9ViZWy0bfxTwN8ppPG7TCovFJlr8bRN2hsIsrPPP49fkp8l8I-0xWgufHRSldXKwS7ZXYx',
            'User-Agent': 'Mozilla/5.0'
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            businesses = data.get('businesses', [])

            listing_urls = {clean_yelp_url(business['url']) for business in businesses}
            new_listing_urls = listing_urls - all_listing_urls  # Only keep new URLs

            all_listing_urls.update(new_listing_urls)

            time.sleep(10)
        else:
            print(f"Failed to fetch data from Yelp API for {yelp_url}. Status code: {response.status_code}")
            print(response.text)  # Print the response content for debugging

        time.sleep(30)
    ALL_PROFILE_URLS.extend(all_listing_urls)

def extract_business_url(profile_url):
    try:
        response = requests.get(profile_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        error_counter += 1
        print(f"Error making request to {profile_url}: {e}")
        if error_counter >= 4:
                print('Exiting GitHub Action due to too many errors.')
                sys.exit(1)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all links with href starting with "/biz_redir"
    business_links = soup.select('[href^="/biz_redir"]')

    business_urls = set()
    for business_link in business_links:
        href = business_link.get('href')
        # Parse the href to get the actual business URL and remove unwanted text
        parsed_url = urlparse(href)
        business_url = unquote(parsed_url.query.split('=')[1]).split('&')[0]
        business_urls.add(business_url)

    return list(business_urls)

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

def main():
    # List of URLs to scrape
    urls_to_scrape = ALL_BUSINESS_URLS

    # Set the number of processes based on the number of URLs you want to scrape in parallel
    num_processes = min(len(urls_to_scrape), 4)  # Adjust the number of processes as needed

    with Pool(processes=num_processes) as pool:
        # Scrape the websites and get unique email addresses
        extracted_emails_list = pool.map(extract_emails_from_url, urls_to_scrape)

    # Combine the extracted email sets from different processes
    extracted_emails = set.union(*extracted_emails_list)

    if extracted_emails:
        print("Status Update: Finished Collecting Emails")
        print('-------------------- FINAL OUTPUT --------------------')
        print(list(extracted_emails))
    else:
        print("CRITICAL FUCKING ERROR: Failed to extract email addresses.")

# --------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- MAIN CODE --------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------- #
        

# -- GETS PROFILE URLS FROM YELP LINKS --
        
print('STARTED PROGRAM')
        
ALL_PROFILE_URLS = []

for i in range(len(yelp_urls)):
    get_listing_urls(yelp_urls[i], max_pages=10, results_per_page=50)
    print(f"Status Update: Collected Profile Url's for {i+1}/{len(yelp_urls)} Url's")
    if (i+1) == (len(yelp_urls)):
        print("Status Update: Finished Collecting All Profile URL's")

# -- GETS BUSINESS WEBSITE URLS FROM PROFILE URLS -- 
        
ALL_BUSINESS_URLS = [] #container

print("Status Update: Collecting Website Url's from Profile Url's")

for profile_url in ALL_PROFILE_URLS:
    time.sleep(10)
    business_urls = extract_business_url(profile_url)

    if business_urls:
        ALL_BUSINESS_URLS.extend(business_urls)

print("Status Update: Finished Collecting Website Url's")

# -- GETS EMAILS FROM WEBSITE URLS --

print("Status Update: Collecting Emails from Website Url's")
if __name__ == "__main__":
    main()





































