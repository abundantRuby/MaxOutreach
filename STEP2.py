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
    "https://www.yelp.com/biz/pride-roofing-and-paint-springfield", "https://www.yelp.com/biz/cr-waterproofing-albany", "https://www.yelp.com/biz/gaviotas-painting-eugene", "https://www.yelp.com/biz/nw-mbs-construction-salem", "https://www.yelp.com/biz/carlson-strand-painting-springfield", "https://www.yelp.com/biz/ash-painting-eugene", "https://www.yelp.com/biz/oregon-premire-painting-eugene-3", "https://www.yelp.com/biz/custom-construction-and-concrete-springfield-2", "https://www.yelp.com/biz/a-and-j-construction-eugene", "https://www.yelp.com/biz/servicemen-painting-springfield", "https://www.yelp.com/biz/third-generation-painting-eugene", "https://www.yelp.com/biz/stom-painters-albany", "https://www.yelp.com/biz/way-to-go-painting-eugene", "https://www.yelp.com/biz/all-american-painting-and-construction-springfield-2", "https://www.yelp.com/biz/trick-construction-cottage-grove-2", "https://www.yelp.com/biz/certapro-painters-of-salem-eugene-springfield", "https://www.yelp.com/biz/fitzpatrick-painting-albany-2", "https://www.yelp.com/biz/creative-solutions-painting-springfield", "https://www.yelp.com/biz/harris-painting-eugene-5", "https://www.yelp.com/biz/groovy-painting-and-construction-eugene", "https://www.yelp.com/biz/mr-goodbrush-painting-eugene", "https://www.yelp.com/biz/japaa-cabinets-and-construction-eugene", "https://www.yelp.com/biz/proline-construction-and-remodel-corvallis-2", "https://www.yelp.com/biz/tightline-quality-painting-bend-2", "https://www.yelp.com/biz/thinking-global-painting-eugene-3", "https://www.yelp.com/biz/mcmahons-painting-springfield-2", "https://www.yelp.com/biz/emerald-valley-coatings-springfield", "https://www.yelp.com/biz/kodiak-painting-springfield-4", "https://www.yelp.com/biz/dry-creek-construction-eagle-point", "https://www.yelp.com/biz/home-pride-painting-and-repair-cottage-grove-4", "https://www.yelp.com/biz/jorges-detail-painting-eugene-2", "https://www.yelp.com/biz/house-2-home-construction-eugene-2", "https://www.yelp.com/biz/dantes-contracting-and-construction-veneta", "https://www.yelp.com/biz/cunninghams-painting-sweet-home", "https://www.yelp.com/biz/chalio-fast-pro-construction-albany-2", "https://www.yelp.com/biz/kaminski-construction-eugene-2", "https://www.yelp.com/biz/spades-environmental-and-construction-springfield", "https://www.yelp.com/biz/homestead-structures-eugene-2", "https://www.yelp.com/biz/duffy-painting-junction-city", "https://www.yelp.com/biz/bov-elite-painting-eugene-4", "https://www.yelp.com/biz/ashburn-home-services-roseburg", "https://www.yelp.com/biz/carls-custom-painting-eugene", "https://www.yelp.com/biz/abc-renovation-eugene", "https://www.yelp.com/biz/super-cool-painter-guy-and-construction-albany-2", "https://www.yelp.com/biz/n-w-precision-exteriors-silverton", "https://www.yelp.com/biz/axe-and-hammer-eugene", "https://www.yelp.com/biz/anita-new-look-eugene", "https://www.yelp.com/biz/checkmark-painting-springfield", "https://www.yelp.com/biz/colortech-enterprises-mount-angel", "https://www.yelp.com/biz/gb-home-improvement-medford-2", "https://www.yelp.com/biz/cascade-precision-painting-springfield", "https://www.yelp.com/biz/holden-painting-springfield", "https://www.yelp.com/biz/jesses-superior-painting-grants-pass", "https://www.yelp.com/biz/joe-carroll-painting-and-construction-veneta", "https://www.yelp.com/biz/randall-j-banks-construction-eugene-2", "https://www.yelp.com/biz/wc-finishes-springfield-2", "https://www.yelp.com/biz/willamette-valley-painting-and-construction-lebanon-2", "https://www.yelp.com/biz/harris-painting-eugene-2", "https://www.yelp.com/biz/hartung-coatings-springfield", "https://www.yelp.com/biz/green-peaks-painting-and-remodeling-llc-springfield", "https://www.yelp.com/biz/terra-painting-and-remodeling-eugene", "https://www.yelp.com/biz/future-design-painting-eugene", "https://www.yelp.com/biz/mcclinton-painting-albany", "https://www.yelp.com/biz/belart-construction-salem", "https://www.yelp.com/biz/ace-classic-painting-eugene", "https://www.yelp.com/biz/home-team-construction-and-remodeling-eugene", "https://www.yelp.com/biz/larry-booman-painting-eugene", "https://www.yelp.com/biz/equitz-painting-white-city", "https://www.yelp.com/biz/foshay-contracting-springfield", "https://www.yelp.com/biz/anything-construction-eugene", "https://www.yelp.com/biz/green-earth-refinishing-springfield-2", "https://www.yelp.com/biz/hansen-lee-painting-eugene", "https://www.yelp.com/biz/sir-paints-a-lot-springfield", "https://www.yelp.com/biz/twothree-painting-eugene", "https://www.yelp.com/biz/laser-line-salem", "https://www.yelp.com/biz/precision-paint-pros-eugene", "https://www.yelp.com/biz/mckenzie-taylor-construction-springfield", "https://www.yelp.com/biz/college-pro-junction-city", "https://www.yelp.com/biz/umpqua-painting-roseburg-2", "https://www.yelp.com/biz/all-purpose-painting-and-more-eugene", "https://www.yelp.com/biz/perfect-painting-and-repairs-roseburg", "https://www.yelp.com/biz/equilibrium-painting-corvallis", "https://www.yelp.com/biz/jacks-quality-maintenance-turner", "https://www.yelp.com/biz/saylor-painting-eugene", "https://www.yelp.com/biz/mathis-painting-eugene-4", "https://www.yelp.com/biz/advanced-painting-solutions-salem", "https://www.yelp.com/biz/castleberry-painting-junction-city", "https://www.yelp.com/biz/trust-painting-eugene-6", "https://www.yelp.com/biz/ethan-darcey-painting-salem", "https://www.yelp.com/biz/handy-folks-eugene-2", "https://www.yelp.com/biz/prestons-painting-springfield", "https://www.yelp.com/biz/3-pillars-painting-eugene", "https://www.yelp.com/biz/peralta-enterprises-springfield", "https://www.yelp.com/biz/cascadia-pro-paint-eugene", "https://www.yelp.com/biz/pj-s-precision-painting-albany"
]

for profile_url in profile_urls:
    business_urls = extract_business_url(profile_url)

    if business_urls:
        for url in business_urls:
            print(f'"{url}",')






