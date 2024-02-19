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
    "https://www.yelp.com/biz/affordable-painting-kennewick", "https://www.yelp.com/biz/badger-mountain-painting-pasco", "https://www.yelp.com/biz/remodeling-and-painting-homes-kennewick", "https://www.yelp.com/biz/the-painting-bees-pasco-2", "https://www.yelp.com/biz/atomic-painting-kennewick", "https://www.yelp.com/biz/m-and-m-painting-west-richland", "https://www.yelp.com/biz/l-and-l-painting-kennewick", "https://www.yelp.com/biz/kirbyworks-painting-kennewick-2", "https://www.yelp.com/biz/spt-kennewick", "https://www.yelp.com/biz/garage-and-closet-solutions-kennewick", "https://www.yelp.com/biz/poseidon-painting-west-richland-2", "https://www.yelp.com/biz/reality-painting-kennewick", "https://www.yelp.com/biz/college-pro-painters-tri-cities-richland", "https://www.yelp.com/biz/desert-painting-richland", "https://www.yelp.com/biz/first-quality-kennewick", "https://www.yelp.com/biz/matheson-painting-pasco-2", "https://www.yelp.com/biz/blue-mountain-valley-contracting-walla-walla-2", "https://www.yelp.com/biz/d-and-s-drywall-and-paint-pasco-2", "https://www.yelp.com/biz/smile-a-mile-painting-kennewick-3", "https://www.yelp.com/biz/nates-painting-services-richland", "https://www.yelp.com/biz/l-b-painters-kennewick", "https://www.yelp.com/biz/bjj-painting-kennewick", "https://www.yelp.com/biz/antonios-painting-pasco-3", "https://www.yelp.com/biz/a-and-g-coatings-benton-city-3", "https://www.yelp.com/biz/all-american-quality-coatings-richland", "https://www.yelp.com/biz/patriot-painting-pasco", "https://www.yelp.com/biz/a-fields-painting-pasco-2", "https://www.yelp.com/biz/juniors-painting-pasco", "https://www.yelp.com/biz/chavez-painting-kennewick", "https://www.yelp.com/biz/all-point-painters-kennewick", "https://www.yelp.com/biz/phils-building-maintenance-kennewick-3", "https://www.yelp.com/biz/pyramid-painting-and-construction-richland-2", "https://www.yelp.com/biz/3-cities-paint-kennewick", "https://www.yelp.com/biz/dickinson-construction-and-specialty-coating-kennewick", "https://www.yelp.com/biz/project-pros-kennewick", "https://www.yelp.com/biz/jeffs-color-chart-kennewick", "https://www.yelp.com/biz/paintmaster-services-richland-3", "https://www.yelp.com/biz/integrity-painting-company-pasco", "https://www.yelp.com/biz/renaissance-roofing-kennewick", "https://www.yelp.com/biz/espana-enterprises-mesa", "https://www.yelp.com/biz/kevins-handyman-services-kennewick", "https://www.yelp.com/biz/thorn-works-pasco", "https://www.yelp.com/biz/certapro-painters-yakima-2", "https://www.yelp.com/biz/belza-painting-and-resurfacing-kennewick-2", "https://www.yelp.com/biz/moon-painting-service-and-finishes-west-richland"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')






