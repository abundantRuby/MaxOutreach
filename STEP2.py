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
    "https://www.yelp.com/biz/divine-pro-finishes-painting-lathrop-2", "https://www.yelp.com/biz/francisco-painting-corp-san-francisco", "https://www.yelp.com/biz/gerson-bustillo-san-francisco-2", "https://www.yelp.com/biz/clayton-hubbard-painting-san-francisco", "https://www.yelp.com/biz/jdf-home-solutions-san-jose-5", "https://www.yelp.com/biz/fares-painting-inc-richmond-2", "https://www.yelp.com/biz/palacios-painting-san-ramon-2", "https://www.yelp.com/biz/handlify-san-francisco", "https://www.yelp.com/biz/paintzen-san-francisco-san-francisco", "https://www.yelp.com/biz/mccartney-painting-san-francisco-2", "https://www.yelp.com/biz/abraham-lopez-painting-san-francisco", "https://www.yelp.com/biz/legend-derry-painting-san-francisco", "https://www.yelp.com/biz/tom-lawless-painting-san-francisco-2", "https://www.yelp.com/biz/miracle-method-of-san-francisco-brisbane", "https://www.yelp.com/biz/diablo-valley-painting-concord", "https://www.yelp.com/biz/miguels-professional-painting-antioch", "https://www.yelp.com/biz/kmans-kreations-san-francisco", "https://www.yelp.com/biz/robert-jasso-painting-san-francisco", "https://www.yelp.com/biz/m-d-s-quality-painting-first-coat-plus-santa-rosa", "https://www.yelp.com/biz/flying-colors-san-francisco", "https://www.yelp.com/biz/paint-and-paperman-sausalito-2", "https://www.yelp.com/biz/mejia-nery-painting-san-francisco-2", "https://www.yelp.com/biz/escobar-painting-san-bruno", "https://www.yelp.com/biz/a2z-home-improvement-brunswick-2", "https://www.yelp.com/biz/juan-pablo-escalante-painting-san-francisco", "https://www.yelp.com/biz/color-renaissance-san-francisco", "https://www.yelp.com/biz/o-brien-painted-to-last-oakland", "https://www.yelp.com/biz/bob-buckter-color-consultant-san-francisco-2", "https://www.yelp.com/biz/neil-cudden-painting-petaluma", "https://www.yelp.com/biz/lr-bros-painting-petaluma-3", "https://www.yelp.com/biz/sanchez-painting-and-handyman-san-francisco", "https://www.yelp.com/biz/gandara-s-construction-company-antioch-2", "https://www.yelp.com/biz/eddy-s-painting-san-rafael", "https://www.yelp.com/biz/julio-construction-handyman-sunnyvale", "https://www.yelp.com/biz/jees-painting-and-maintenance-san-bruno", "https://www.yelp.com/biz/tg-harris-painting-vacaville", "https://www.yelp.com/biz/jlm-painting-petaluma", "https://www.yelp.com/biz/the-rock-handyman-specialist-san-pablo-3", "https://www.yelp.com/biz/pearl-painting-san-francisco", "https://www.yelp.com/biz/michael-butler-painting-san-francisco", "https://www.yelp.com/biz/rhino-shield-san-francisco", "https://www.yelp.com/biz/guatex-painting-san-francisco", "https://www.yelp.com/biz/green-oak-painting-san-francisco-7", "https://www.yelp.com/biz/ad-painting-san-francisco", "https://www.yelp.com/biz/garcia-fencing-and-gates-services-oakland-10", "https://www.yelp.com/biz/g-and-r-quality-painting-south-san-francisco-2", "https://www.yelp.com/biz/dwell-painting-san-francisco", "https://www.yelp.com/biz/amigos-painting-sunnyvale-2", "https://www.yelp.com/biz/top-quality-painting-san-bruno", "https://www.yelp.com/biz/white-colors-painting-oakland", "https://www.yelp.com/biz/gomez-service-san-mateo", "https://www.yelp.com/biz/stroke-and-kote-painting-san-rafael-3", "https://www.yelp.com/biz/miguel-painting-san-francisco-2", "https://www.yelp.com/biz/3-fingers-painting-san-francisco", "https://www.yelp.com/biz/albo-movers-san-francisco", "https://www.yelp.com/biz/solutec-handyman-services-phoenix-2", "https://www.yelp.com/biz/coastal-west-painting-berkeley-3", "https://www.yelp.com/biz/j-wood-painting-and-restoration-san-francisco", "https://www.yelp.com/biz/goveas-painting-san-francisco-5", "https://www.yelp.com/biz/metro-painting-san-francisco", "https://www.yelp.com/biz/druzeta-painting-san-francisco", "https://www.yelp.com/biz/godinez-painting-san-francisco", "https://www.yelp.com/biz/santana-painting-woodside-2", "https://www.yelp.com/biz/shu-ji-professional-painting-san-francisco", "https://www.yelp.com/biz/luis-interior-painting-san-francisco", "https://www.yelp.com/biz/ridea-painting-san-francisco-2", "https://www.yelp.com/biz/master-sheet-metal-san-francisco-2", "https://www.yelp.com/biz/ferreira-painting-company-vallejo", "https://www.yelp.com/biz/mj-drywall-oakland", "https://www.yelp.com/biz/jrw-painting-danville-2", "https://www.yelp.com/biz/royal-bay-scaffold-piedmont", "https://www.yelp.com/biz/level-five-painting-richmond", "https://www.yelp.com/biz/j-e-carpentry-and-handy-man-san-francisco", "https://www.yelp.com/biz/clarks-painting-company-san-francisco", "https://www.yelp.com/biz/authority-painting-fremont-2", "https://www.yelp.com/biz/rob-finn-fine-painting-and-design-san-francisco", "https://www.yelp.com/biz/florentino-galicia-constructions-san-francisco", "https://www.yelp.com/biz/roger-incorporated-painting-vallejo", "https://www.yelp.com/biz/usv-painting-el-cerrito", "https://www.yelp.com/biz/jh-painting-san-francisco", "https://www.yelp.com/biz/oliveira-painters-san-pablo-4", "https://www.yelp.com/biz/mvn-painting-san-jose-2", "https://www.yelp.com/biz/octo-painting-san-mateo-2", "https://www.yelp.com/biz/fabians-fine-finishes-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/simons-painting-san-francisco", "https://www.yelp.com/biz/estradas-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/robert-bernhard-coatings-san-francisco-4", "https://www.yelp.com/biz/mcateer-painting-san-francisco", "https://www.yelp.com/biz/mata-painting-and-decorating-san-francisco-3", "https://www.yelp.com/biz/heather-and-french-painting-san-francisco", "https://www.yelp.com/biz/napco-painting-contractors-inc-napa", "https://www.yelp.com/biz/c-and-c-painting-san-francisco", "https://www.yelp.com/biz/e-c-o-fine-painting-san-francisco", "https://www.yelp.com/biz/ken-s-painting-and-handy-works-san-francisco-4", "https://www.yelp.com/biz/first-coat-pro-painting-san-francisco", "https://www.yelp.com/biz/canseco-painting-san-francisco", "https://www.yelp.com/biz/next-level-painting-oakland", "https://www.yelp.com/biz/carlos-handyman-oakland-2", "https://www.yelp.com/biz/rays-straight-line-painting-hayward-3", "https://www.yelp.com/biz/professional-painting-solutions-oakland-2", "https://www.yelp.com/biz/vazquez-handyman-services-south-san-francisco", "https://www.yelp.com/biz/a-and-f-all-bay-painting-oakland-5", "https://www.yelp.com/biz/fog-city-painting-san-francisco", "https://www.yelp.com/biz/bayarea-painters-exterior-and-interior-san-francisco", "https://www.yelp.com/biz/rayco-painting-oakland", "https://www.yelp.com/biz/chateau-painting-san-francisco-2", "https://www.yelp.com/biz/cydney-ortzow-painting-oakland", "https://www.yelp.com/biz/fas-painting-daly-city", "https://www.yelp.com/biz/san-francisco-renaissance-painting-san-francisco-3", "https://www.yelp.com/biz/california-mural-art-danville", "https://www.yelp.com/biz/jovel-quality-painting-san-francisco", "https://www.yelp.com/biz/westerlund-custom-painting-hayward", "https://www.yelp.com/biz/resurrection-painting-san-francisco", "https://www.yelp.com/biz/jdm-painting-staining-specialists-healdsburg", "https://www.yelp.com/biz/ms-painting-vacaville-2", "https://www.yelp.com/biz/blue-puzzle-painting-san-francisco", "https://www.yelp.com/biz/steve-tingley-painting-san-francisco", "https://www.yelp.com/biz/j-p-painting-and-decorating-vacaville-2", "https://www.yelp.com/biz/color-flow-painting-san-francisco-2"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







