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
    "https://www.yelp.com/biz/a-coatings-antioch-3", "https://www.yelp.com/biz/lionel-eco-painting-redwood-city-2", "https://www.yelp.com/biz/cora-s-painting-san-jos%C3%A9", "https://www.yelp.com/biz/luis-interior-painting-san-francisco", "https://www.yelp.com/biz/honey-do-handyman-services-campbell-2", "https://www.yelp.com/biz/jos%C3%A9-handyman-hayward-2", "https://www.yelp.com/biz/lawn-care-and-wood-care-san-jose-6", "https://www.yelp.com/biz/artsem-karniayenka-san-jose-2", "https://www.yelp.com/biz/j-r-painting-turlock-5", "https://www.yelp.com/biz/ta-painting-san-jose-2", "https://www.yelp.com/biz/shine-painting-newark-2", "https://www.yelp.com/biz/davey-painting-morgan-hill", "https://www.yelp.com/biz/craft-plastering-construction-hayward-2", "https://www.yelp.com/biz/km-construction-east-palo-alto-2", "https://www.yelp.com/biz/final-coat-painting-san-mateo", "https://www.yelp.com/biz/3-brothers-handyman-services-san-jose-5", "https://www.yelp.com/biz/brother-and-brother-builders-san-jose-3", "https://www.yelp.com/biz/kaiwi-construction-palo-alto-3", "https://www.yelp.com/biz/everado-painting-san-jose", "https://www.yelp.com/biz/jcc-painting-san-jose", "https://www.yelp.com/biz/cp-pro-painting-san-jose-3", "https://www.yelp.com/biz/a-o-renovation-and-demolition-san-jose-2", "https://www.yelp.com/biz/mr-ungers-kitchen-and-bathroom-remodeling-south-san-francisco", "https://www.yelp.com/biz/friendly-painting-novato", "https://www.yelp.com/biz/arturos-custom-painting-hollister-3", "https://www.yelp.com/biz/master-painting-san-jose", "https://www.yelp.com/biz/h-v-quality-painting-santa-clara", "https://www.yelp.com/biz/perry-higgins-painting-morgan-hill", "https://www.yelp.com/biz/camacho-painting-milpitas-7", "https://www.yelp.com/biz/superior-image-painting-co-san-jose", "https://www.yelp.com/biz/sh-painting-service-santa-clara", "https://www.yelp.com/biz/pe%C3%B1a-drywall-campbell", "https://www.yelp.com/biz/finishes-unlimited-campbell", "https://www.yelp.com/biz/on-time-painting-san-francisco", "https://www.yelp.com/biz/arnulfo-handyman-and-painting-san-mateo-3", "https://www.yelp.com/biz/vedder-painting-boulder-creek", "https://www.yelp.com/biz/next-level-painting-oakland", "https://www.yelp.com/biz/permacoat-painting-and-construction-san-jose", "https://www.yelp.com/biz/mora-painting-san-jose", "https://www.yelp.com/biz/bustamante-painting-salinas", "https://www.yelp.com/biz/brothers-painting-company-san-jose", "https://www.yelp.com/biz/inside-out-painting-san-francisco-3", "https://www.yelp.com/biz/salvador-painting-san-jose-3", "https://www.yelp.com/biz/picasso-painting-el-granada", "https://www.yelp.com/biz/rc-painting-san-jose", "https://www.yelp.com/biz/bravo-s-handyman-san-mateo", "https://www.yelp.com/biz/craft-team-palo-alto", "https://www.yelp.com/biz/jlo-painting-mountain-view", "https://www.yelp.com/biz/vgp-painting-san-jose", "https://www.yelp.com/biz/aria-build-and-construction-san-jose-2", "https://www.yelp.com/biz/robbies-painting-san-jose-2", "https://www.yelp.com/biz/unlimited-murals-oakland", "https://www.yelp.com/biz/john-melendez-paint-company-san-jose", "https://www.yelp.com/biz/mannys-pro-painting-san-jose", "https://www.yelp.com/biz/wise-painting-east-palo-alto-2", "https://www.yelp.com/biz/total-wood-preservation-redwood-city-3", "https://www.yelp.com/biz/white-painting-morgan-hill", "https://www.yelp.com/biz/the-precise-touch-painting-san-jose", "https://www.yelp.com/biz/durans-handyman-east-palo-alto-2", "https://www.yelp.com/biz/j-p-painting-san-jose", "https://www.yelp.com/biz/painting-and-construction-tony-s-los-gatos-3", "https://www.yelp.com/biz/santana-painting-woodside-2", "https://www.yelp.com/biz/garvey-painting-aptos", "https://www.yelp.com/biz/nu-life-painting-services-san-jose-2", "https://www.yelp.com/biz/unique-quality-painting-san-jose", "https://www.yelp.com/biz/baltazar-painting-san-jose", "https://www.yelp.com/biz/lebaron-painting-aptos", "https://www.yelp.com/biz/advance-gtc-painting-san-jose-3", "https://www.yelp.com/biz/zavalas-painting-sunnyvale-5", "https://www.yelp.com/biz/aq-finish-carpenter-santa-clara", "https://www.yelp.com/biz/painting-in-the-bay-area-sunnyvale-3", "https://www.yelp.com/biz/j-master-koatings-hayward", "https://www.yelp.com/biz/egh-rainbow-painting-san-jose", "https://www.yelp.com/biz/gerson-bustillo-san-francisco-2", "https://www.yelp.com/biz/vladimir-starchenko-san-jose-9", "https://www.yelp.com/biz/jeff-burgess-painting-and-decorating-morgan-hill", "https://www.yelp.com/biz/leading-edge-construction-san-jose-5", "https://www.yelp.com/biz/victors-custom-painting-and-handyman-services-san-jose", "https://www.yelp.com/biz/ellzeys-painting-san-jose-5", "https://www.yelp.com/biz/a-r-painting-san-jose", "https://www.yelp.com/biz/proficient-painting-san-jose", "https://www.yelp.com/biz/jarquin-painting-antioch-5", "https://www.yelp.com/biz/zv-professional-painting-and-decorating-co-san-lorenzo", "https://www.yelp.com/biz/personal-impressions-painting-and-deck-restoration-gilroy-2", "https://www.yelp.com/biz/chavas-painting-san-jose", "https://www.yelp.com/biz/green-leaf-painting-san-jose", "https://www.yelp.com/biz/spray-technology-santa-clara", "https://www.yelp.com/biz/linear-tech-striping-san-jose-3", "https://www.yelp.com/biz/painting-geeks-san-jose", "https://www.yelp.com/biz/n-style-painting-san-jose", "https://www.yelp.com/biz/affordable-painting-graphics-west-painting-san-jose-5", "https://www.yelp.com/biz/castillos-painting-san-jose-2", "https://www.yelp.com/biz/north-pacific-painting-sunnyvale-2", "https://www.yelp.com/biz/rainbow-painting-san-jose", "https://www.yelp.com/biz/thane-waldo-painting-mountain-view-2", "https://www.yelp.com/biz/gruber-painting-san-jose", "https://www.yelp.com/biz/farmor-painting-ben-lomond", "https://www.yelp.com/biz/big-league-painting-san-jose", "https://www.yelp.com/biz/kennyman-the-handyman-san-francisco-5", "https://www.yelp.com/biz/cjp-painting-san-jose-2", "https://www.yelp.com/biz/jdj-painting-and-restoration-san-jose", "https://www.yelp.com/biz/crow-painting-fremont-2", "https://www.yelp.com/biz/waltmen-painting-services-san-jose", "https://www.yelp.com/biz/rays-straight-line-painting-hayward-3", "https://www.yelp.com/biz/lc-painting-sunnyvale", "https://www.yelp.com/biz/i-and-i-painting-company-inc-mountain-view", "https://www.yelp.com/biz/jdf-home-solutions-san-jose-5", "https://www.yelp.com/biz/artistech-painting-san-jose", "https://www.yelp.com/biz/alarcon-premier-painting-san-jose", "https://www.yelp.com/biz/pablos-general-remodeling-oakland", "https://www.yelp.com/biz/gomez-service-san-mateo", "https://www.yelp.com/biz/pena-family-san-jose", "https://www.yelp.com/biz/rc-royals-painting-vacaville", "https://www.yelp.com/biz/ph-handyman-service-palo-alto-2", "https://www.yelp.com/biz/certapro-painters-of-san-mateo-ca-san-mateo", "https://www.yelp.com/biz/precision-remodeling-san-jose", "https://www.yelp.com/biz/escamillas-painting-newark-9", "https://www.yelp.com/biz/color-pros-inc-milpitas", "https://www.yelp.com/biz/squad-g-san-jose", "https://www.yelp.com/biz/new-impression-painting-redwood-city-2", "https://www.yelp.com/biz/kevin-johnson-painting-san-jose"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







