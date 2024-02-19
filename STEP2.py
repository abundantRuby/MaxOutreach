import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

def extract_business_url(profile_url):
    try:
        response = requests.get(profile_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {profile_url}: {e}")
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

# Example usage with a list of profile URLs
profile_urls = [
    "https://www.yelp.com/biz/new-hope-painting-bend", "https://www.yelp.com/biz/a-flock-of-painters-bend", "https://www.yelp.com/biz/two-guys-painting-bend-2", "https://www.yelp.com/biz/rohr-painting-and-construction-bend", "https://www.yelp.com/biz/callaway-contracting-bend", "https://www.yelp.com/biz/aquarela-construction-and-painting-bend", "https://wacting-madras", "https://www.yelp.com/biz/dale-luoma-painting-and-design-bend", "https://www.yelp.com/biz/its-just-jt-painting-redmond", "https://www.yelp.com/biz/towne-and-country-painting-bend", "https://www.yelp.com/biz/rt-painting-and-construction-prineville", "https://www.yelp.com/biz/west-rivers-painting-bend", "https://www.yelp.com/biz/almog-construction-redmond-2", "https://www.yelp.com/biz/hardie-finishes-painting-fairfax-2", "https://www.yelp.com/biz/ejb-construction-bend", "https://www.yelp.com/biz/allied-painting-and-renovations-bend", "https://www.yelp.com/biz/crystal-lake-maintenance-bend", "https://www.yelp.com/biz/oak-and-pine-renovations-bend", "https://www.yelp.com/biz/brick-house-property-management-bend", "https://www.yelp.com/biz/my-painter-bend-4", "https://www.yelp.com/biz/a-1-painters-and-builders-bend-3", "https://www.yelp.com/biz/perfection-enterprises-bend-2", "https://www.yelp.com/biz/gator-done-painting-bend", "https://www.yelp.com/biz/red-door-paint-bend", "https://www.yelp.com/biz/jerry-harris-painting-central-oregon", "https://www.yelp.com/biz/rise-painting-round-rock-2", "https://www.yelp.com/biz/k-and-k-painting-specialists-bend", "https://www.yelp.com/biz/paint-pros-central-oregon-redmond", "https://www.yelp.com/biz/luxury-color-design-bend", "https://www.yelp.com/biz/cj-painting-and-custom-finishes-bend", "https://www.yelp.com/biz/eco-plus-painting-bend", "https://www.yelp.com/biz/optimum-painting-and-general-contracting-bend", "https://www.yelp.com/biz/tightline-quality-painting-bend-2", "https://www.yelp.com/biz/barbell-painting-redmond", "https://www.yelp.com/biz/travis-knight-art-bend-3", "https://www.yelp.com/biz/lime-painting-of-bend-bend-2", "https://www.yelp.com/biz/northwest-painting-and-restoration-bend", "https://www.yelp.com/biz/derocks-painting-bend", "https://www.yelp.com/biz/sundance-custom-painting-bend", "https://www.yelp.com/biz/dels-drywall-and-paint-bend-6", "https://www.yelp.com/biz/justin-newman-painting-bend", "https://www.yelp.com/biz/morse-paint-and-design-redmond", "https://www.yelp.com/biz/olmos-construction-and-remodeling-bend-2", "https://www.yelp.com/biz/elite-construction-contracting-bend-2", "https://www.yelp.com/biz/riverfront-painting-bend-2", "https://www.yelp.com/biz/college-pro-painters-bend-bend", "https://www.yelp.com/biz/44-northwest-bend", "https://www.yelp.com/biz/cascade-crest-painting-bend-2", "https://www.yelp.com/biz/billionfold-paint-company-la-pine", "https://www.yelp.com/biz/pierce-painting-bend", "https://www.yelp.com/biz/around-the-bend-paint-and-woodcare-bend", "https://www.yelp.com/biz/bill-sizemore-painting-redmond-2", "https://www.yelp.com/biz/coating-solutions-redmond", "https://www.yelp.com/biz/newman-brothers-painting-bend-2", "https://www.yelp.com/biz/that-one-painter-bend", "https://www.yelp.com/biz/full-moon-painting-and-design-prineville-3", "https://www.yelp.com/biz/daniel-james-kahlo-painting-fountain-hills"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







