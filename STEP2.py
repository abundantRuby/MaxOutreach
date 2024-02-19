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
"https://www.yelp.com/biz/mr-fix-bay-area-santa-clara-4", "https://www.yelp.com/biz/authority-painting-fremont-2", "https://www.yelp.com/biz/r-and-g-painting-san-jose-2", "https://www.yelp.com/biz/smart-quality-painting-and-drywall-san-jose", "https://www.yelp.com/biz/f-and-g-handymen-san-jose-5", "https://www.yelp.com/biz/colors-by-zoltan-redwood-city", "https://www.yelp.com/biz/paradise-painting-san-jose", "https://www.yelp.com/biz/huy-s-painting-hayward", "https://www.yelp.com/biz/mb-artistico-hayward", "https://www.yelp.com/biz/b-and-a-homes-remodel-north-highlands-2", "https://www.yelp.com/biz/sunseri-painting-company-gilroy", "https://www.yelp.com/biz/martin-s-painter-mountain-view", "https://www.yelp.com/biz/octo-painting-san-mateo-2", "https://www.yelp.com/biz/riverz-pro-green-landscaping-west-menlo-park", "https://www.yelp.com/biz/wise-builders-san-jose", "https://www.yelp.com/biz/solis-painting-service-san-jose", "https://www.yelp.com/biz/kevin-copley-painting-campbell", "https://www.yelp.com/biz/custom-painting-livermore-2", "https://www.yelp.com/biz/fresh-coats-painting-san-jose", "https://www.yelp.com/biz/sierra-painting-fremont-6", "https://www.yelp.com/biz/ac-painting-sunnyvale", "https://www.yelp.com/biz/smart-home-construction-san-jose", "https://www.yelp.com/biz/sebastian-painting-san-jose", "https://www.yelp.com/biz/blue-beret-painting-san-pablo", "https://www.yelp.com/biz/douglas-service-handyman-san-jose-5", "https://www.yelp.com/biz/house-doctor-painting-san-jose-3", "https://www.yelp.com/biz/palacios-painting-san-ramon-2", "https://www.yelp.com/biz/r-and-r-painting-services-san-jose-2", "https://www.yelp.com/biz/divine-pro-finishes-painting-lathrop-2", "https://www.yelp.com/biz/willow-glen-painting-san-jose", "https://www.yelp.com/biz/d-and-h-painting-union-city", "https://www.yelp.com/biz/real-painting-benicia", "https://www.yelp.com/biz/kb-handyman-services-gilroy", "https://www.yelp.com/biz/olguins-painting-and-drywall-daly-city-5", "https://www.yelp.com/biz/wow-1-day-painting-san-jose-morgan-hill-2", "https://www.yelp.com/biz/jennifer-davis-painting-san-jose", "https://www.yelp.com/biz/madera-finishes-san-jose-5", "https://www.yelp.com/biz/mb-jessee-painting-oakland-4", "https://www.yelp.com/biz/paint-and-power-wash-company-san-francisco-4", "https://www.yelp.com/biz/certapro-painters-palo-alto-palo-alto", "https://www.yelp.com/biz/romanov-painting-palo-alto", "https://www.yelp.com/biz/ads-painting-san-francisco-6", "https://www.yelp.com/biz/fine-line-painting-san-francisco", "https://www.yelp.com/biz/most-creative-painting-redwood-city", "https://www.yelp.com/biz/sg-handyman-service-santa-clara", "https://www.yelp.com/biz/peters-painting-company-campbell", "https://www.yelp.com/biz/futbol-painting-san-jose", "https://www.yelp.com/biz/tonys-painting-san-jose-5", "https://www.yelp.com/biz/rossi-painting-and-construction-san-carlos-11", "https://www.yelp.com/biz/hernandez-painting-san-jose", "https://www.yelp.com/biz/urbinas-painting-company-san-jose", "https://www.yelp.com/biz/architectural-masters-painting-pleasanton", "https://www.yelp.com/biz/mike-moody-painting-san-jose", "https://www.yelp.com/biz/bay-area-design-and-construction-campbell", "https://www.yelp.com/biz/shark-painting-modesto", "https://www.yelp.com/biz/a-painting-san-jose-2", "https://www.yelp.com/biz/genes-painting-san-leandro", "https://www.yelp.com/biz/javiar-custom-paint-san-jose", "https://www.yelp.com/biz/the-painting-pros-los-gatos-3", "https://www.yelp.com/biz/daisy-s-painting-and-flooring-san-jose-2", "https://www.yelp.com/biz/choo-paints-santa-clara-2", "https://www.yelp.com/biz/style-painting-palo-alto", "https://www.yelp.com/biz/delta-painting-san-jose-4", "https://www.yelp.com/biz/meza-painting-walnut-creek-4", "https://www.yelp.com/biz/sandino-painting-santa-clara", "https://www.yelp.com/biz/agh-painting-san-jose", "https://www.yelp.com/biz/lorenzos-painters-san-jose", "https://www.yelp.com/biz/antovia-painting-redwood-city-2", "https://www.yelp.com/biz/aarons-painting-vallejo", "https://www.yelp.com/biz/marvelous-painters-san-jose-5", "https://www.yelp.com/biz/mr-fix-campbell", "https://www.yelp.com/biz/stars-painting-san-francisco-4", "https://www.yelp.com/biz/community-painters-san-jose", "https://www.yelp.com/biz/figueroas-painting-san-jose", "https://www.yelp.com/biz/narvaez-painting-san-jose", "https://www.yelp.com/biz/woods-painting-scotts-valley", "https://www.yelp.com/biz/just-n-time-painting-san-jose", "https://www.yelp.com/biz/pri-premiere-roofing-livermore-7", "https://www.yelp.com/biz/ronaldo-taping-mud-hang-framing-paint-house-and-comercial-richmond-5", "https://www.yelp.com/biz/quality-painting-and-construction-san-francisco-6", "https://www.yelp.com/biz/r-brothers-san-jose-4", "https://www.yelp.com/biz/gg-painting-and-handyman-service-mountain-view-3", "https://www.yelp.com/biz/zak-of-all-trades-livermore", "https://www.yelp.com/biz/high-tech-painting-san-jose-3", "https://www.yelp.com/biz/antonio-painting-san-mateo-3", "https://www.yelp.com/biz/ehr-san-jose-3", "https://www.yelp.com/biz/green-remodeling-solutions-sj-san-jose", "https://www.yelp.com/biz/fernandos-painting-san-jose", "https://www.yelp.com/biz/blue-spade-construction-san-jose", "https://www.yelp.com/biz/designed-walls-mountain-view", "https://www.yelp.com/biz/aaron-bradley-construction-repair-and-painting-san-jose", "https://www.yelp.com/biz/j-rodriguez-painting-san-jose", "https://www.yelp.com/biz/superior-painting-company-san-jose", "https://www.yelp.com/biz/dan-pe%C3%B1a-drywall-san-jose-5", "https://www.yelp.com/biz/moras-painting-santa-clara-8", "https://www.yelp.com/biz/westerlund-custom-painting-hayward", "https://www.yelp.com/biz/juan-carlos-handyman-san-mateo-4", "https://www.yelp.com/biz/g-and-r-quality-painting-south-san-francisco-2", "https://www.yelp.com/biz/djs-painting-san-jose", "https://www.yelp.com/biz/olympic-painting-san-jose-2", "https://www.yelp.com/biz/robert-saenz-los-gatos", "https://www.yelp.com/biz/golden-state-roofing-and-painting-san-jose", "https://www.yelp.com/biz/guzman-handyman-services-fremont", "https://www.yelp.com/biz/pacific-drywall-and-painting-campbell", "https://www.yelp.com/biz/piazza-painting-san-jose"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')







