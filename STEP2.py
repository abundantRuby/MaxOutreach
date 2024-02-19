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
    "https://www.yelp.com/biz/bonilla-painting-san-jose", "https://www.yelp.com/biz/future-vision-remodeling-san-jose-4", "https://www.yelp.com/biz/amigos-painting-sunnyvale-2", "https://www.yelp.com/biz/edgar-d-painting-san-francisco-3", "https://www.yelp.com/biz/uniat-painting-los-gatos", "https://www.yelp.com/biz/ha-painting-santa-clara", "https://www.yelp.com/biz/mvn-painting-san-jose-2", "https://www.yelp.com/biz/project-handyman-san-jose", "https://www.yelp.com/biz/brc-home-services-sunnyvale-4", "https://www.yelp.com/biz/the-professionals-painting-san-jose-3", "https://www.yelp.com/biz/larry-wells-painting-aptos", "https://www.yelp.com/biz/otovo-handyman-santa-clara-3", "https://www.yelp.com/biz/sydney-boyle-paint-san-jose", "https://www.yelp.com/biz/c-and-s-painting-san-jose", "https://www.yelp.com/biz/guevaras-painting-san-jose-3", "https://www.yelp.com/biz/john-b-signs-san-jose", "https://www.yelp.com/biz/jrw-painting-danville-2", "https://www.yelp.com/biz/benavides-construction-san-jose", "https://www.yelp.com/biz/all-purpose-painting-and-restoration-fremont", "https://www.yelp.com/biz/a-plus-painting-co-pittsburg-4", "https://www.yelp.com/biz/hl-construction-san-jose-2", "https://www.yelp.com/biz/renovo-home-solutions-san-jose", "https://www.yelp.com/biz/cj-painting-and-renovation-san-jose", "https://www.yelp.com/biz/arc-painting-santa-clara", "https://www.yelp.com/biz/spectrum-bay-painting-san-jose", "https://www.yelp.com/biz/drs-stairs-san-jose-2", "https://www.yelp.com/biz/renovation-in-your-home-san-jose", "https://www.yelp.com/biz/shalom-handyman-redwood-city-4", "https://www.yelp.com/biz/rjl-painting-menlo-park", "https://www.yelp.com/biz/pmr-painting-and-decorating-san-jose", "https://www.yelp.com/biz/wall-to-wall-painting-hayward", "https://www.yelp.com/biz/rj-painting-palo-alto-3", "https://www.yelp.com/biz/cartwright-painters-san-jose-2", "https://www.yelp.com/biz/amex-painting-inc-san-jose", "https://www.yelp.com/biz/ramos-painting-san-mateo", "https://www.yelp.com/biz/m-z-painting-san-francisco-2", "https://www.yelp.com/biz/alvarenga-painting-sunnyvale-2", "https://www.yelp.com/biz/aidens-quality-painting-santa-clara", "https://www.yelp.com/biz/reynaga-s-painting-services-san-jose", "https://www.yelp.com/biz/high-point-services-santa-clara-3", "https://www.yelp.com/biz/wt-painting-san-jose", "https://www.yelp.com/biz/ms-construction-and-service-san-jose", "https://www.yelp.com/biz/hernandez-painter-san-jose", "https://www.yelp.com/biz/dominguez-painting-east-palo-alto", "https://www.yelp.com/biz/meraz-painting-san-jose-2", "https://www.yelp.com/biz/saez-painting-hollister", "https://www.yelp.com/biz/edy-handyman-san-mateo", "https://www.yelp.com/biz/fine-line-painting-los-gatos", "https://www.yelp.com/biz/angels-paint-and-epoxy-sunnyvale", "https://www.yelp.com/biz/motivated-movers-san-jose", "https://www.yelp.com/biz/kelly-painting-san-jose-2", "https://www.yelp.com/biz/jr-quality-painting-san-jose-2", "https://www.yelp.com/biz/madrids-painting-san-jose-3", "https://www.yelp.com/biz/a-and-a-brothers-painting-san-jose", "https://www.yelp.com/biz/arellanos-painting-santa-clara-4", "https://www.yelp.com/biz/jp-painting-redwood-city", "https://www.yelp.com/biz/tran1-painting-san-jose", "https://www.yelp.com/biz/gopro-painters-san-jose", "https://www.yelp.com/biz/anytime-handyman-san-jose-2", "https://www.yelp.com/biz/referred-painting-san-jose-2", "https://www.yelp.com/biz/marble-handyman-services-san-mateo-2", "https://www.yelp.com/biz/all-united-painting-san-jose-3", "https://www.yelp.com/biz/urban-pacific-builders-san-jose", "https://www.yelp.com/biz/gs-painting-mountain-view-2", "https://www.yelp.com/biz/basurto-painting-palo-alto", "https://www.yelp.com/biz/united-pro-handyman-services-san-mateo-4", "https://www.yelp.com/biz/rr-pro-painting-san-jose", "https://www.yelp.com/biz/carlos-construction-daly-city", "https://www.yelp.com/biz/ambar-handyman-services-oakland-6", "https://www.yelp.com/biz/rise-group-campbell-6", "https://www.yelp.com/biz/picky-painting-campbell", "https://www.yelp.com/biz/lincoln-builders-san-jose", "https://www.yelp.com/biz/paint911-painting-service-santa-clara", "https://www.yelp.com/biz/prosperety-santa-clara", "https://www.yelp.com/biz/j-e-carpentry-and-handy-man-san-francisco", "https://www.yelp.com/biz/alphabet-handyman-service-sunnyvale", "https://www.yelp.com/biz/bluestone-painting-san-jose-2", "https://www.yelp.com/biz/two-men-and-a-brush-painting-san-jose", "https://www.yelp.com/biz/valencia-enterprise-san-jose", "https://www.yelp.com/biz/miguel-painting-san-francisco-2", "https://www.yelp.com/biz/npm-painting-redwood-city-12", "https://www.yelp.com/biz/target-painting-san-jose-5", "https://www.yelp.com/biz/fresh-coat-painters-of-central-valley-tracy"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







