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
    "https://www.yelp.com/biz/carmel-kabash-coatings-brisbane", "https://www.yelp.com/biz/mannys-pro-painting-san-jose", "https://www.yelp.com/biz/craft-plastering-construction-hayward-2", "https://www.yelp.com/biz/loyolas-painting-san-francisco", "https://www.yelp.com/biz/redhill-painting-san-francisco-2", "https://www.yelp.com/biz/painting-and-construction-tony-s-los-gatos-3", "https://www.yelp.com/biz/omni-painting-and-waterproofing-oakland-3", "https://www.yelp.com/biz/velsa-painting-san-francisco", "https://www.yelp.com/biz/aya-homes-san-francisco", "https://www.yelp.com/biz/unique-painting-services-novato-3", "https://www.yelp.com/biz/golden-hill-painting-san-francisco-3", "https://www.yelp.com/biz/aesthete-painting-and-wall-covering-san-francisco", "https://www.yelp.com/biz/prestige-painting-oakland", "https://www.yelp.com/biz/trejo-construction-san-francisco", "https://www.yelp.com/biz/berkeley-painting-berkeley", "https://www.yelp.com/biz/ads-painting-san-francisco-6", "https://www.yelp.com/biz/love-painting-san-francisco", "https://www.yelp.com/biz/pro-touch-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/shirley-painting-san-francisco-2", "https://www.yelp.com/biz/c-g-carrillo-painting-richmond", "https://www.yelp.com/biz/gazo-construction-san-francisco", "https://www.yelp.com/biz/popeyes-handyman-service-san-lorenzo-3", "https://www.yelp.com/biz/mark-bellingham-painting-moraga", "https://www.yelp.com/biz/osorio-painting-richmond-8", "https://www.yelp.com/biz/classic-shades-painting-san-francisco", "https://www.yelp.com/biz/handy-moe-san-francisco", "https://www.yelp.com/biz/larson-brothers-painting-napa", "https://www.yelp.com/biz/total-wood-preservation-redwood-city-3", "https://www.yelp.com/biz/mallon-painting-and-construction-san-francisco", "https://www.yelp.com/biz/tom-abell-painting-san-francisco", "https://www.yelp.com/biz/luis-painting-and-handyman-services-san-francisco-2", "https://www.yelp.com/biz/genes-painting-san-leandro", "https://www.yelp.com/biz/top-shelf-painting-san-francisco", "https://www.yelp.com/biz/a-4-painting-plus-sacramento-3", "https://www.yelp.com/biz/united-pro-handyman-services-san-mateo-4", "https://www.yelp.com/biz/alex-davison-painting-san-francisco", "https://www.yelp.com/biz/excel-painting-and-restoration-san-francisco-3", "https://www.yelp.com/biz/conor-forde-painting-san-francisco-2", "https://www.yelp.com/biz/mcdonough-painting-san-francisco-2", "https://www.yelp.com/biz/s-and-s-painting-and-coating-castro-valley", "https://www.yelp.com/biz/modamas-painting-san-francisco", "https://www.yelp.com/biz/the-color-lady-alameda-2", "https://www.yelp.com/biz/atlas-painting-company-san-francisco", "https://www.yelp.com/biz/antonio-painting-san-mateo-3", "https://www.yelp.com/biz/ken-silva-painting-petaluma", "https://www.yelp.com/biz/tom-lewis-restoration-and-consulting-co-san-francisco", "https://www.yelp.com/biz/tim-schmidt-painting-sausalito", "https://www.yelp.com/biz/milton-painting-san-francisco", "https://www.yelp.com/biz/alvarez-painting-and-drywall-tracy", "https://www.yelp.com/biz/mulderrig-painting-san-francisco-2", "https://www.yelp.com/biz/pure-painter-san-francisco", "https://www.yelp.com/biz/miguels-house-painting-san-mateo-4", "https://www.yelp.com/biz/poinciana-painting-colma-24", "https://www.yelp.com/biz/daisy-s-painting-and-flooring-san-jose-2", "https://www.yelp.com/biz/fine-line-painting-san-francisco", "https://www.yelp.com/biz/colorblast-painting-san-leandro-3", "https://www.yelp.com/biz/benavides-construction-san-jose", "https://www.yelp.com/biz/pedro-alvarado-residential-and-commercial-san-rafael", "https://www.yelp.com/biz/henry-s-carpet-and-painting-san-francisco", "https://www.yelp.com/biz/macssf-san-francisco", "https://www.yelp.com/biz/buckner-painting-san-francisco", "https://www.yelp.com/biz/valencia-enterprise-san-jose", "https://www.yelp.com/biz/sourdough-painting-san-francisco-2", "https://www.yelp.com/biz/arnulfo-handyman-and-painting-san-mateo-3", "https://www.yelp.com/biz/friendly-painting-novato", "https://www.yelp.com/biz/abr-pro-painting-san-francisco", "https://www.yelp.com/biz/fresh-start-painting-daly-city", "https://www.yelp.com/biz/rhapsody-painting-and-environmental-services-san-francisco", "https://www.yelp.com/biz/vincent-powell-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/western-painting-alameda", "https://www.yelp.com/biz/gold-brush-painting-san-francisco-2", "https://www.yelp.com/biz/jugame-quality-painting-albany", "https://www.yelp.com/biz/west-bay-painting-company-san-francisco", "https://www.yelp.com/biz/sinclair-painting-san-francisco-10", "https://www.yelp.com/biz/munoz-painting-walnut-creek", "https://www.yelp.com/biz/riverz-pro-green-landscaping-west-menlo-park", "https://www.yelp.com/biz/rosales-painting-san-francisco", "https://www.yelp.com/biz/faraci-house-painting-redwood-city", "https://www.yelp.com/biz/bay-pro-help-san-francisco", "https://www.yelp.com/biz/teresa-romaine-painting-san-francisco", "https://www.yelp.com/biz/ra-lopez-painting-richmond", "https://www.yelp.com/biz/shannon-geis-murals-san-francisco", "https://www.yelp.com/biz/sf-painting-and-decorating-san-francisco", "https://www.yelp.com/biz/the-precise-touch-painting-san-jose", "https://www.yelp.com/biz/san-francisco-paint-source-san-francisco-2", "https://www.yelp.com/biz/hamerkop-general-contractor-and-plastering-services-san-francisco", "https://www.yelp.com/biz/jesus-henriquez-construction-san-francisco", "https://www.yelp.com/biz/masterplan-painting-san-rafael-3", "https://www.yelp.com/biz/e-custom-design-rohnert-park-2", "https://www.yelp.com/biz/handyman-elfenix-san-francisco", "https://www.yelp.com/biz/r-and-d-tile-and-more-san-francisco-2", "https://www.yelp.com/biz/jp-painting-redwood-city", "https://www.yelp.com/biz/m-z-painting-san-francisco-2", "https://www.yelp.com/biz/house-doctor-painting-san-jose-3", "https://www.yelp.com/biz/garvey-plastering-and-painting-moss-beach", "https://www.yelp.com/biz/doherty-restoration-san-francisco-2", "https://www.yelp.com/biz/alphabet-handyman-service-sunnyvale", "https://www.yelp.com/biz/julios-paint-service-south-san-francisco", "https://www.yelp.com/biz/olguins-painting-and-drywall-daly-city-5", "https://www.yelp.com/biz/zv-professional-painting-and-decorating-co-san-lorenzo", "https://www.yelp.com/biz/honey-do-handyman-services-campbell-2", "https://www.yelp.com/biz/rios-painting-mill-valley-2", "https://www.yelp.com/biz/pablo-landscaping-and-painting-services-san-rafael", "https://www.yelp.com/biz/kanika-design-san-mateo-2", "https://www.yelp.com/biz/shark-painting-modesto", "https://www.yelp.com/biz/mauricia-gandara-san-francisco-6", "https://www.yelp.com/biz/maldonado-painting-inc-santa-rosa", "https://www.yelp.com/biz/ejs-painting-san-francisco", "https://www.yelp.com/biz/mc-fresh-painting-san-francisco-2", "https://www.yelp.com/biz/perry-higgins-painting-morgan-hill", "https://www.yelp.com/biz/adams-handyman-santa-clara-4", "https://www.yelp.com/biz/bouche-painting-san-francisco-3", "https://www.yelp.com/biz/citibay-painting-san-leandro", "https://www.yelp.com/biz/ngd-painting-novato", "https://www.yelp.com/biz/pasion-painting-rodeo", "https://www.yelp.com/biz/lee-family-san-francisco-7", "https://www.yelp.com/biz/bay-area-painting-and-decoration-san-francisco", "https://www.yelp.com/biz/painting-geeks-san-jose", "https://www.yelp.com/biz/community-painters-san-jose", "https://www.yelp.com/biz/yuni-chilel-painting-daly-city-6", "https://www.yelp.com/biz/kent-painting-and-finishing-concord-2", "https://www.yelp.com/biz/bob-antonelli-san-francisco-6", "https://www.yelp.com/biz/deck-preservation-hayward-3", "https://www.yelp.com/biz/sunny-bay-painting-co-san-francisco", "https://www.yelp.com/biz/van-go-painting-inc-pacifica", "https://www.yelp.com/biz/ariel-munoz-painting-san-francisco", "https://www.yelp.com/biz/wall-to-wall-painting-hayward", "https://www.yelp.com/biz/rodas-drywall-and-painting-san-rafael", "https://www.yelp.com/biz/bravo-s-handyman-san-mateo", "https://www.yelp.com/biz/angels-paint-and-epoxy-sunnyvale", "https://www.yelp.com/biz/final-coat-painting-san-mateo"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







