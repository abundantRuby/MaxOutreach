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
    "https://www.yelp.com/biz/morones-painting-san-francisco", "https://www.yelp.com/biz/chris-the-painter-san-francisco", "https://www.yelp.com/biz/bigler-universal-painting-san-francisco", "https://www.yelp.com/biz/lemus-construction-san-francisco-2", "https://www.yelp.com/biz/crew-color-painting-oakland-4", "https://www.yelp.com/biz/adf-painting-services-cruz-san-francisco-2", "https://www.yelp.com/biz/a-and-z-handyman-san-carlos", "https://www.yelp.com/biz/pablos-general-remodeling-oakland", "https://www.yelp.com/biz/omega-construction-san-mateo", "https://www.yelp.com/biz/across-the-bay-painting-san-leandro", "https://www.yelp.com/biz/ezekiels-drywall-services-san-jose", "https://www.yelp.com/biz/prado-pro-painting-richmond", "https://www.yelp.com/biz/j-master-koatings-hayward", "https://www.yelp.com/biz/mv-professional-painting-santa-clara", "https://www.yelp.com/biz/precision-painting-and-handyman-svcs-alameda-5", "https://www.yelp.com/biz/prism-colors-daly-city", "https://www.yelp.com/biz/vlahos-painting-contractor-san-francisco", "https://www.yelp.com/biz/unlimited-murals-oakland", "https://www.yelp.com/biz/chaojun-home-improvement-service-alameda", "https://www.yelp.com/biz/marble-handyman-services-san-mateo-2", "https://www.yelp.com/biz/billinger-painting-company-daly-city", "https://www.yelp.com/biz/o-malley-painting-san-bruno", "https://www.yelp.com/biz/yacoub-sadan-san-francisco", "https://www.yelp.com/biz/baran-painting-san-francisco", "https://www.yelp.com/biz/divas-painting-san-rafael", "https://www.yelp.com/biz/architectural-masters-painting-pleasanton", "https://www.yelp.com/biz/jb-hernandez-painting-marin-city", "https://www.yelp.com/biz/joseph-clancy-painting-san-francisco", "https://www.yelp.com/biz/butler-painting-and-construction-vallejo", "https://www.yelp.com/biz/brophy-painting-company-san-francisco", "https://www.yelp.com/biz/welington-handyman-and-painter-san-bruno", "https://www.yelp.com/biz/handy-helper-san-francisco-5", "https://www.yelp.com/biz/armstrong-emeryville", "https://www.yelp.com/biz/fdz-painting-san-francisco", "https://www.yelp.com/biz/fugnai-construction-san-francisco-2", "https://www.yelp.com/biz/platypus-painting-inc-oakland", "https://www.yelp.com/biz/gomez-home-services-oakland-15", "https://www.yelp.com/biz/carlos-aa-construction-novato-3", "https://www.yelp.com/biz/pop-painting-and-drywall-san-francisco-3", "https://www.yelp.com/biz/napa-valley-handyman-st-helena", "https://www.yelp.com/biz/sal-painting-san-francisco-13", "https://www.yelp.com/biz/astoria-construction-san-francisco", "https://www.yelp.com/biz/city-west-construction-san-francisco", "https://www.yelp.com/biz/anacletos-painters-san-francisco-4", "https://www.yelp.com/biz/kst-handyman-sunnyvale", "https://www.yelp.com/biz/merlan-drywall-stockton", "https://www.yelp.com/biz/miztint-painting-company-san-francisco-3", "https://www.yelp.com/biz/little-red-truck-painting-south-san-francisco", "https://www.yelp.com/biz/fix-formula-painting-oakland", "https://www.yelp.com/biz/quality-painting-and-construction-san-francisco-6", "https://www.yelp.com/biz/tara-pro-painting-san-francisco-3", "https://www.yelp.com/biz/don-buckter-painting-san-francisco", "https://www.yelp.com/biz/atlani-painting-berkeley-4", "https://www.yelp.com/biz/color-home-services-san-francisco-peninsula-2", "https://www.yelp.com/biz/daniel-t-cray-painting-burlingame", "https://www.yelp.com/biz/dm-painting-san-francisco", "https://www.yelp.com/biz/ambar-handyman-services-oakland-6", "https://www.yelp.com/biz/california-house-painting-colma", "https://www.yelp.com/biz/terrell-painting-tracy-7", "https://www.yelp.com/biz/the-vintage-owl-benicia", "https://www.yelp.com/biz/cabreras-painting-san-francisco", "https://www.yelp.com/biz/olsons-painting-alameda", "https://www.yelp.com/biz/gonzalez-painting-berkeley-3", "https://www.yelp.com/biz/moura-and-borges-painting-san-francisco", "https://www.yelp.com/biz/rodas-painting-daly-city", "https://www.yelp.com/biz/dragon-werks-san-francisco-8", "https://www.yelp.com/biz/coyados-painting-san-francisco-2", "https://www.yelp.com/biz/prees-professional-painting-concord-2", "https://www.yelp.com/biz/milton-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/lewis-restoration-and-consulting-san-francisco", "https://www.yelp.com/biz/reliable-remodeling-and-renovation-san-rafael-4", "https://www.yelp.com/biz/rojas-painting-petaluma-5", "https://www.yelp.com/biz/alex-garcia-painting-martinez", "https://www.yelp.com/biz/bay-bros-painting-san-francisco", "https://www.yelp.com/biz/kofman-painting-san-francisco", "https://www.yelp.com/biz/real-painting-benicia", "https://www.yelp.com/biz/ronaldo-taping-mud-hang-framing-paint-house-and-comercial-richmond-5", "https://www.yelp.com/biz/earley-painting-concord", "https://www.yelp.com/biz/level-carpentry-colma", "https://www.yelp.com/biz/freddy-s-handyman-san-francisco", "https://www.yelp.com/biz/willys-painting-oakland-2", "https://www.yelp.com/biz/edgar-d-painting-san-francisco-3", "https://www.yelp.com/biz/nor-cal-wood-restoration-and-painting-san-rafael", "https://www.yelp.com/biz/meza-painting-walnut-creek-4", "https://www.yelp.com/biz/fay-construction-and-restoration-san-francisco", "https://www.yelp.com/biz/alonso-painting-san-francisco-4", "https://www.yelp.com/biz/indigo-painting-san-francisco-2", "https://www.yelp.com/biz/blue-beret-painting-san-pablo", "https://www.yelp.com/biz/toms-painters-san-francisco-2", "https://www.yelp.com/biz/golden-gate-painting-redwood-city-3", "https://www.yelp.com/biz/moose-pro-painting-san-francisco", "https://www.yelp.com/biz/rafael-silva-professional-painting-san-francisco-2", "https://www.yelp.com/biz/greenwin-san-francisco", "https://www.yelp.com/biz/antovia-painting-redwood-city-2", "https://www.yelp.com/biz/best-deal-painting-san-francisco-2", "https://www.yelp.com/biz/native-design-painting-hayward", "https://www.yelp.com/biz/jml-painting-services-san-francisco", "https://www.yelp.com/biz/super-home-builders-san-francisco-3", "https://www.yelp.com/biz/speciallystone-el-cerrito-2", "https://www.yelp.com/biz/hugo-handyman-remodeling-san-francisco-2", "https://www.yelp.com/biz/vision-lh-services-san-francisco", "https://www.yelp.com/biz/smartbuild-construction-dublin", "https://www.yelp.com/biz/sean-o-reilly-painting-san-francisco-4", "https://www.yelp.com/biz/dasilva-painting-san-francisco", "https://www.yelp.com/biz/mc-painting-and-drywall-services-pleasanton", "https://www.yelp.com/biz/rc-royals-painting-vacaville", "https://www.yelp.com/biz/jc-pro-painting-union-city-6", "https://www.yelp.com/biz/mr-ungers-kitchen-and-bathroom-remodeling-south-san-francisco", "https://www.yelp.com/biz/carlos-painting-and-handyman-san-francisco", "https://www.yelp.com/biz/on-time-painting-san-francisco", "https://www.yelp.com/biz/castle-painting-san-francisco-2", "https://www.yelp.com/biz/sky-painting-and-construction-south-san-francisco-5"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







