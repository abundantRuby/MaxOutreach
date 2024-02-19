import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

def extract_business_url(profile_url):
    response = requests.get(profile_url)
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

# Example usage with a list of profile URLs
profile_urls = [
    "https://www.yelp.com/biz/fitzpatrick-painting-albany-2", "https://www.yelp.com/biz/paint-the-world-newport", "https://www.yelp.com/biz/coastline-painting-pacific-city", "https://www.yelp.com/biz/quality-painting-service-otis-3", "https://www.yelp.com/biz/salem-drywall-salem", "https://www.yelp.com/biz/oregon-coast-tree-company-newport", "https://www.yelp.com/biz/townsend-painting-company-newport", "https://www.yelp.com/biz/sfw-construction-llc-portland-3", "https://www.yelp.com/biz/most-wanted-painters-newport-2", "https://www.yelp.com/biz/mcclinton-painting-albany", "https://www.yelp.com/biz/new-day-painting-mcminnville-3"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')






