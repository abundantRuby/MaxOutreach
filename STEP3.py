import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
from multiprocessing import Pool

def clean_email_string(email_str):
    # Use a more restrictive regex pattern to filter out invalid email-like strings
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', email_str)
    
    if email_match:
        # Additional checks to filter out email-like strings with unusual patterns
        email_address = email_match.group()
        if '@' in email_address and '.' in email_address and len(email_address) <= 40:
            return email_address
        
    return None

def extract_emails_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html5lib')

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
    urls_to_scrape = [
        "https://homeservicesmc.com",
        "http://www.marketreadypaint.com"
            ]

    # Set the number of processes based on the number of URLs you want to scrape in parallel
    num_processes = min(len(urls_to_scrape), 4)  # Adjust the number of processes as needed

    with Pool(processes=num_processes) as pool:
        # Scrape the websites and get unique email addresses
        extracted_emails_list = pool.map(extract_emails_from_url, urls_to_scrape)

    # Combine the extracted email sets from different processes
    extracted_emails = set.union(*extracted_emails_list)

    if extracted_emails:
        print("| EMAIL ADDRESSES |")
        formatted_emails = ', '.join(f'"{email}"' for email in extracted_emails)
        print(formatted_emails)
    else:
        print("Failed to extract email addresses.")

if __name__ == "__main__":
    main()





