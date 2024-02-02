import requests
from urllib.parse import urlparse, parse_qs
import time

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
            'term': 'painters',
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

            time.sleep(10)  # Pause for 10 seconds before the next page
        else:
            print(f"Failed to fetch data from Yelp API for {yelp_url}. Status code: {response.status_code}")
            print(response.text)  # Print the response content for debugging

    for i, url in enumerate(all_listing_urls, start=1):
        print(f'"{url}"', end=", " if i < len(all_listing_urls) else "")

# Example usage with the provided URL
yelp_url = "https://www.yelp.com/search?find_desc=restaurants&find_loc=Seattle%2C+WA"
get_listing_urls(yelp_url, max_pages=10, results_per_page=50)




































