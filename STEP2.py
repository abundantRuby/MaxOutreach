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
    "https://www.yelp.com/biz/carvajal-painting-redwood-city", "https://www.yelp.com/biz/kanika-design-san-mateo-2", "https://www.yelp.com/biz/pride-painting-san-jose", "https://www.yelp.com/biz/artisan-builders-group-san-jose", "https://www.yelp.com/biz/neighborhood-construction-san-jose-2", "https://www.yelp.com/biz/ortiz-painting-and-refinishing-san-jose", "https://www.yelp.com/biz/crown-painters-los-angeles", "https://www.yelp.com/biz/mj-painting-san-jose-3", "https://www.yelp.com/biz/mp-painting-livermore-4", "https://www.yelp.com/biz/cydney-ortzow-painting-oakland", "https://www.yelp.com/biz/wilber-wood-work-sunnyvale-3", "https://www.yelp.com/biz/gamaliel-villatoro-painting-san-lorenzo", "https://www.yelp.com/biz/ezekiels-drywall-services-san-jose", "https://www.yelp.com/biz/veter-construction-menlo-park-3", "https://www.yelp.com/biz/faith-painting-san-jose", "https://www.yelp.com/biz/moura-and-borges-painting-san-francisco", "https://www.yelp.com/biz/creative-wall-designs-morgan-hill", "https://www.yelp.com/biz/aac-painters-patterson", "https://www.yelp.com/biz/burdick-painting-santa-clara", "https://www.yelp.com/biz/a-and-j-handyman-service-freedom-2", "https://www.yelp.com/biz/the-ultimate-drywall-san-jose-4", "https://www.yelp.com/biz/chief-s-painting-san-jose", "https://www.yelp.com/biz/justfaux-san-jose", "https://www.yelp.com/biz/cali-handyman-services-san-jose", "https://www.yelp.com/biz/guacamaya-painting-inc-san-jose-2", "https://www.yelp.com/biz/garcia-fencing-and-gates-services-oakland-10", "https://www.yelp.com/biz/cervantes-painting-san-jose", "https://www.yelp.com/biz/n-j-kann-painting-san-jose", "https://www.yelp.com/biz/julio-construction-handyman-sunnyvale", "https://www.yelp.com/biz/james-painting-san-jose", "https://www.yelp.com/biz/miguels-house-painting-san-mateo-4", "https://www.yelp.com/biz/watercolors-aptos", "https://www.yelp.com/biz/fernando-the-neat-painting-and-decorating-san-carlos", "https://www.yelp.com/biz/more-than-handy-morgan-hill-2", "https://www.yelp.com/biz/silicon-valley-builders-group-san-jose", "https://www.yelp.com/biz/mural-project-san-jose", "https://www.yelp.com/biz/bay-areas-paint-and-special-coatings-san-jose", "https://www.yelp.com/biz/icon-construction-san-jose-2", "https://www.yelp.com/biz/dubon-painting-san-jose-3", "https://www.yelp.com/biz/el-gato-painting-san-jose-2", "https://www.yelp.com/biz/handlify-san-francisco", "https://www.yelp.com/biz/mj-painting-san-jose-20", "https://www.yelp.com/biz/fredy-handyman-san-jose-2", "https://www.yelp.com/biz/catrux-wallpaper-painting-and-handyman-san-francisco", "https://www.yelp.com/biz/smart-painting-sunnyvale", "https://www.yelp.com/biz/futbol-painting-and-repair-san-jose", "https://www.yelp.com/biz/golden-colors-painting-richmond-3", "https://www.yelp.com/biz/daniel-pelaez-painting-san-jose-5", "https://www.yelp.com/biz/best-bros-painting-modesto", "https://www.yelp.com/biz/jc-pro-painting-union-city-6", "https://www.yelp.com/biz/francisco-the-painter-san-jose", "https://www.yelp.com/biz/alexanders-painting-san-jos%C3%A9-3", "https://www.yelp.com/biz/rolling-sea-painting-san-mateo-3", "https://www.yelp.com/biz/ncm-painting-and-construction-santa-clara-2", "https://www.yelp.com/biz/the-wright-way-painting-vacaville", "https://www.yelp.com/biz/serrato-s-home-upgrades-san-jose-2", "https://www.yelp.com/biz/east-bay-handyman-services-walnut-creek", "https://www.yelp.com/biz/mayorga-handyman-services-daly-city-3", "https://www.yelp.com/biz/allied-roofing-and-contracting-san-jose", "https://www.yelp.com/biz/carlos-handyman-oakland-2", "https://www.yelp.com/biz/tonys-painting-san-jose-2", "https://www.yelp.com/biz/done-right-builders-and-remodeling-santa-clara-2", "https://www.yelp.com/biz/cutting-edge-painting-santa-cruz", "https://www.yelp.com/biz/rh-painting-and-remodeling-stockton-20", "https://www.yelp.com/biz/stanford-painting-mountain-view", "https://www.yelp.com/biz/carranzas-painting-san-jose", "https://www.yelp.com/biz/antioch-haro-paint-antioch-2", "https://www.yelp.com/biz/sunnyvale-painting-sunnyvale-2", "https://www.yelp.com/biz/jgo-painting-san-jose", "https://www.yelp.com/biz/sierra-azul-painting-aptos-2", "https://www.yelp.com/biz/hamerkop-general-contractor-and-plastering-services-san-francisco", "https://www.yelp.com/biz/arceo-epoxy-concrete-coatings-santa-clara-2", "https://www.yelp.com/biz/pro-cabinet-painting-san-jose", "https://www.yelp.com/biz/j-and-r-services-concord-2", "https://www.yelp.com/biz/chavez-painting-and-flooring-san-jose", "https://www.yelp.com/biz/california-mural-art-danville", "https://www.yelp.com/biz/sunwest-painting-san-jose-2", "https://www.yelp.com/biz/clark-painters-san-jose", "https://www.yelp.com/biz/lux-painting-san-jose", "https://www.yelp.com/biz/willys-painting-oakland-2", "https://www.yelp.com/biz/happiness-painting-san-jose", "https://www.yelp.com/biz/pimentels-painting-san-jose", "https://www.yelp.com/biz/professional-painting-solutions-oakland-2", "https://www.yelp.com/biz/mendez-painting-san-francisco", "https://www.yelp.com/biz/good-bye-old-paint-painting-campbell"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







