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
    "https://www.yelp.com/biz/proactive-painting-san-jose", "https://www.yelp.com/biz/cruz-gs-construction-soquel", "https://www.yelp.com/biz/native-design-painting-hayward", "https://www.yelp.com/biz/accolade-home-services-redwood-city-3", "https://www.yelp.com/biz/ayala-painting-and-decorating-san-jose-9", "https://www.yelp.com/biz/smartbuild-construction-dublin", "https://www.yelp.com/biz/tjp-painting-san-jose", "https://www.yelp.com/biz/escobar-painting-san-bruno", "https://www.yelp.com/biz/j-milliman-painting-san-jose", "https://www.yelp.com/biz/advanced-painting-systems-castro-valley", "https://www.yelp.com/biz/zoe-painting-and-decorating-santa-clara", "https://www.yelp.com/biz/army-painting-gilroy", "https://www.yelp.com/biz/valley-home-builders-santa-clara-2", "https://www.yelp.com/biz/yes-painting-services-campbell", "https://www.yelp.com/biz/all-pro-property-maintenance-san-jose", "https://www.yelp.com/biz/all-surface-painting-and-decorating-and-dustless-blasting-oakley-2", "https://www.yelp.com/biz/four-seasons-painting-san-jose", "https://www.yelp.com/biz/great-walls-painting-san-jose", "https://www.yelp.com/biz/golden-gate-painting-redwood-city-3", "https://www.yelp.com/biz/mj-drywall-oakland", "https://www.yelp.com/biz/lohanoco-remarkable-san-jose-2", "https://www.yelp.com/biz/vivid-paint-co-san-jose", "https://www.yelp.com/biz/citibay-painting-san-leandro", "https://www.yelp.com/biz/brightview-painting-morgan-hill-4", "https://www.yelp.com/biz/high-tech-nice-painting-san-carlos", "https://www.yelp.com/biz/hayward-pro-construction-and-painting-hayward", "https://www.yelp.com/biz/jugame-quality-painting-albany", "https://www.yelp.com/biz/ej-painting-menlo-park-11", "https://www.yelp.com/biz/naillon-painting-san-jose-2", "https://www.yelp.com/biz/saratoga-painting-and-home-services-saratoga-2", "https://www.yelp.com/biz/rudy-diaz-painting-san-jose", "https://www.yelp.com/biz/the-bay-painting-san-jose-2", "https://www.yelp.com/biz/accu-colormat-san-jose-2", "https://www.yelp.com/biz/chavira-paint-and-wallpaper-san-jose", "https://www.yelp.com/biz/commercial-painting-san-jose-4", "https://www.yelp.com/biz/amazing-cesars-painting-san-jose", "https://www.yelp.com/biz/bills-brush-works-san-jose", "https://www.yelp.com/biz/z-and-r-general-construction-san-jose-3", "https://www.yelp.com/biz/dasilva-painting-san-francisco", "https://www.yelp.com/biz/kst-handyman-sunnyvale", "https://www.yelp.com/biz/one-piece-painting-san-jose", "https://www.yelp.com/biz/blue-handy-services-santa-clara", "https://www.yelp.com/biz/new-world-painting-san-jose", "https://www.yelp.com/biz/stevens-faux-designs-san-jose", "https://www.yelp.com/biz/a-and-z-handyman-san-carlos", "https://www.yelp.com/biz/faraci-house-painting-redwood-city", "https://www.yelp.com/biz/jesus-painting-san-jose", "https://www.yelp.com/biz/proper-hour-handyman-service-santa-clara-3", "https://www.yelp.com/biz/ed-doyle-eco-painting-ben-lomond", "https://www.yelp.com/biz/j-gomez-painting-san-francisco", "https://www.yelp.com/biz/cabreras-painting-san-francisco", "https://www.yelp.com/biz/think-happy-painters-san-jose-2", "https://www.yelp.com/biz/white-colors-painting-oakland", "https://www.yelp.com/biz/786-construction-cupertino-5", "https://www.yelp.com/biz/hackett-painting-company-menlo-park", "https://www.yelp.com/biz/deck-preservation-hayward-3", "https://www.yelp.com/biz/mv-professional-painting-santa-clara", "https://www.yelp.com/biz/raymundo-painting-vallejo-10", "https://www.yelp.com/biz/northbay-painting-specialist-san-jose-4", "https://www.yelp.com/biz/vazquez-handyman-services-south-san-francisco", "https://www.yelp.com/biz/a-and-r-bentley-painting-san-jose", "https://www.yelp.com/biz/sharon-stone-design-san-jose-2", "https://www.yelp.com/biz/premier-solutions-east-palo-alto-3", "https://www.yelp.com/biz/antique-painting-mountain-view-4", "https://www.yelp.com/biz/kcg-painting-san-jose", "https://www.yelp.com/biz/evergreen-painting-and-texture-san-jose", "https://www.yelp.com/biz/the-color-connection-san-jose-2", "https://www.yelp.com/biz/j-and-r-custom-painting-scotts-valley", "https://www.yelp.com/biz/caspi-handyman-los-gatos-6", "https://www.yelp.com/biz/green-brush-painting-company-santa-clara-3", "https://www.yelp.com/biz/pasion-painting-rodeo", "https://www.yelp.com/biz/tonys-painting-and-remodeling-fremont-3", "https://www.yelp.com/biz/master-s-touch-painting-gilroy", "https://www.yelp.com/biz/jesus-sanchez-painting-san-jose", "https://www.yelp.com/biz/esso-painting-simpsonville-5", "https://www.yelp.com/biz/merlan-drywall-stockton", "https://www.yelp.com/biz/jjc-painting-san-jose", "https://www.yelp.com/biz/partida-drywall-san-jose", "https://www.yelp.com/biz/lb-quality-painting-san-jose-2", "https://www.yelp.com/biz/across-the-bay-painting-san-leandro", "https://www.yelp.com/biz/premier-painting-san-jose", "https://www.yelp.com/biz/alvarez-painting-and-drywall-tracy", "https://www.yelp.com/biz/darios-painting-and-handyman-san-jose-2", "https://www.yelp.com/biz/arandy-painting-union-city", "https://www.yelp.com/biz/bay-area-painting-and-ops-san-jose-2", "https://www.yelp.com/biz/nor-cal-painting-san-jose", "https://www.yelp.com/biz/munoz-painting-walnut-creek", "https://www.yelp.com/biz/wilmar-s-painting-oakland", "https://www.yelp.com/biz/elliotts-elite-painting-san-jose", "https://www.yelp.com/biz/paint-it-california-san-jose", "https://www.yelp.com/biz/mister-paint-fine-bay-area-painting-fremont-3", "https://www.yelp.com/biz/us-creative-builders-san-jose-2", "https://www.yelp.com/biz/vs-renovation-campbell", "https://www.yelp.com/biz/f-and-s-painting-san-jose-2", "https://www.yelp.com/biz/torres-painting-san-jose-3", "https://www.yelp.com/biz/henry-s-carpet-and-painting-san-francisco", "https://www.yelp.com/biz/adams-handyman-santa-clara-4", "https://www.yelp.com/biz/a-perez-construction-san-jose", "https://www.yelp.com/biz/goodfellas-construction-san-jose-3", "https://www.yelp.com/biz/bauhaus-design-and-construction-san-jose", "https://www.yelp.com/biz/3mp-builders-san-jose", "https://www.yelp.com/biz/best-deal-painting-sj-san-jose-10", "https://www.yelp.com/biz/abr-pro-painting-san-francisco", "https://www.yelp.com/biz/mbc-painting-san-jose-3", "https://www.yelp.com/biz/howards-painting-redwood-city", "https://www.yelp.com/biz/melody-painting-santa-clara"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







