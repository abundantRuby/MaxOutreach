import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time
import datetime
import pytz

desired_time_zone = 'America/New_York'
current_date = datetime.datetime.now(pytz.timezone(desired_time_zone))
day_name = current_date.strftime("%A")
CURRENT_DAY = day_name

# Gmail SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Gmail account credentials for each sender
SENDER_ACCOUNTS = [
    {"username": "dysco712@gmail.com", "password": "zlqc jiro aneg oddt"},
    {"username": "iamdylanhoag@gmail.com", "password": "hwys aypg refe luea"},
    {"username": "dylanhoagdigital@gmail.com", "password": "alqi ngon mayg wnfy"}
]

# Email templates
EMAIL_TEMPLATES = [
    "Hello!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I build websites and run digital ads. I've helped a handful of businesses increase their online presence, and was wondering if I could do the same for your business.\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nBest,\n\nDylan Hoag",
    f"Happy {CURRENT_DAY}!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I build websites and run digital ads. I've helped a handful of businesses increase their online presence, and was wondering if I could do the same for your business.\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nBest,\n\nDylan Hoag",
    "Hello!\n\nJust a heads-up, not your usual email.\n\nMy name's Dylan, I develop websites and tinker with digital ads. I've boosted a few businesses' online game and thought, 'Hey, maybe I can do the same for yours.'\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nCheers,\n\nDylan Hoag",
    f"Happy {CURRENT_DAY}!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I develop websites and tinker with digital ads. I've boosted a few businesses' online game and thought, 'Hey, maybe I can do the same for yours.'\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nCheers,\n\nDylan Hoag\n\n",
    "Hey there!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I develop websites and build digital ad campaigns, and was wondering if my services could be of value for your business.\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nCheers,\n\nDylan Hoag\n\n",
    f"Happy {CURRENT_DAY}!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I develop websites and build digital ad campaigns, and was wondering if my services could be of value for your business.\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nCheers,\n\nDylan Hoag\n\n",
    f"Happy {CURRENT_DAY}!\n\nI'll keep it brief as I appreciate you're busy.\n\nMy name's Dylan, I develop websites and tinker with digital ads. I've boosted a few businesses' online game and thought, 'Hey, maybe I can do the same for yours.'\n\nIf you're up for it, I can shoot over some examples of my work and results from my clients!\n\nCheers,\n\nDylan Hoag\n\n",
]

# Subject lines
SUBJECT_LINES = [
    "Quick Question for You!",
    "Quick Question",
    "Quick Question",
    "Boost Your Business", 
    "Digital Magic",
    "Online Potential"
]

def send_email(to_address, subject, body, sender_info):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_info["username"]
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(sender_info["username"], sender_info["password"])

        # Send the email
        server.sendmail(sender_info["username"], to_address, msg.as_string())

    print(f"Email Sent from: {sender_info['username']} to: {to_address}")

def main():
    # Email addresses to send to
    TO_EMAIL_ADDRESSES = ['moonpainting@msn.com', 'premier_paint@comcast.net', 'wetworkspnw@gmail.com', 'agemma3715@gmail.com', 'pvyconstruction@gmail.com', 'budgetpaintersonline@gmail.com', 'realitypaintingllc@gmail.com', 'jeff@kusterhomes.com', 'office@thebrushmasters253.com', 'jacks@cwprllc.com', 'Painters@SmileAMilePainting.Com', 'joshcooley@colorcoatedpaintingllc.com', 'denalipaintingllc@gmail.com', 'thebrushmasters253@gmail.com', 'info@westexteriorconstruction.com', 'Vince.king1968@gmail.com', 'harbertgreg4@gmail.com', 'Elitefreedompainters@gmail.com', 'reese@flyguysconstruction.com', 'llfamilypainting@gmail.com', 'evergreenpaintllc@gmail.com', 'thehomepros16@gmail.com', 'topgradedevelopment@gmail.com', 'Derek@AllServicesRealEstateWhatcom.com', 'leshiggins291@gmail.com', 'info@OlympiaPaintingCo.com', 'Contact@simplyinstallations.com', 'JStar.Services16@gmail.com', 'cprinclacey@gmail.com', 'finalfinishetc@gmail.com', 'info@remodelingandpainting.us', 'raleighjohnson174@gmail.com', 'info@richardspainting.net', 'timhpllc@aol.com', 'Info@OlympiaPaintingCo.com', 'richardspaintingbellingham@gmail.com', 'info@northpinepainting.com', 'dandrpaintingwa@gmail.com', 'office@mathesonpainting.com', 'procoverroofing360@gmail.com', 'info@northwestconstruction.coop', 'renee@jlinderpainting.com', 'enchristollc@gmail.com', 'DecoPaintingDesign@gmail.com', 'Tim.desertpainting@gmail.com', 'allinconstruction@outlook.com', '20acguerrero211@gmail.com', 'info@ampainting.com', 'sdcleaning8@gmail.com', 'prpwright@msn.com', 'davidsddrywall@gmail.com', 'truecolors5761@gmail.com', 'info@indec-company.com', 'INFO@ITHROOFING.COM', 'Painterpro2@gmail.com', 'newera04.21@outlook.com', 'KellyExteriorPainting@gmail.com', 'info@all-painting.com', 'sddrywalloffice@gmail.com', 'topcaliberpainting@gmail.com', 'paintingkellyandsons@gmail.com', 'acguerrero211@gmail.com', 'service@apexpaintandremodel.com', 'jeffnelson@ridge-painting.com', 'mark@destinypaintingwa.com', 'bids@gracepointcontracting.com', 'preferredbuildingcontractors@gmail.com', 'contact@imconstructionpdx.com', 'prolinecandroffice@gmail.com', 'info@sullivanpainting.com', 'admin@tracysqualitypainting.com', 'support@unk.com', 'Office@oregonexcellence.com', 'info@actionpaintandcontracting.com', 'pintalamore@gmail.com', 'highlandspaintingllc@gmail.com', 'westlandhomeconstruction@gmail.com', 'paulnewtonpaintingllc@gmail.com', 'Simplesolutionspaint@gmail.com', 'fernando14sddrywall@gmail.com', 'andre@eapaintingllc.com', 'indeccompany@gmail.com', 'juansddrywall@gmail.com', 'evergreenpropainting1@gmail.com', 'info@edmastersllc.com', 'curbappealpaintingcompany@gmail.com', 'TransferHands@gmail.com', 'simplypainting@mail.com', 'info@brickhousepropertymgmt.com', 'barbellpainting@gmail.com', '3pillarspainting@gmail.com', 'abcrenovationeugene@gmail.com', 'marlonspaint@yahoo.com', 'equilibriumpainting@gmail.com', 'ashburnhomeservices@gmail.com', 'delsdrywallandremodeling@gmail.com', 'bill45gm@gmail.com', 'office@paintprosoregon.com', 'painterjorge@gmail.com', 'sunriverpainting@gmail.com', 'waytogopainting@msn.com', 'castleberrypainting@gmail.com', 'greenpeaksllc@gmail.com', 'russellreed2962@gmail.com', 'mike@hamptonpaintinginc.com', 'dale@luomapainting.com', 'mbsconstruction@nwmbspainting.com', 'Tirrelldante@gmail.com', 'info@goldencrestpainting.com', 'info@walgamuthpainting.com', 'JoeCarrollPainting@Yahoo.com', 'lmntpainting41@gmail.com', 'marc@halcyonpainting.com', 'James@hardie-finishes.com', 'TrinityHandymanServicesCA@gmail.com', 'jasinek@reddoorpaint.com', 'info@halcyonpainting.com', 'pjsprecisionpaints@gmail.com', 'contact@morsepaint.com', 'gaviotas@gaviotaspainting.com', 'futuredesignpainting@gmail.com', 'luxurycolordesign@gmail.com', 'Anita@anitanewlooknow.com', 'mikesamuelsensons@gmail.com', 'jcremodelllc@outlook.com', 'bert@breachbuilders.com', 'riverfrontpainting@icloud.com', 'ashpainting2010@gmail.com', 'scottadaniel@gmail.com', 'info@trustpaintingllc.com', 'info@valleyroofcare.com', 'info@alliedpaintnow.com', 'tim@talbotpaintingservices.com', 'rjpainting4you@gmail.com', 'davidz@prestonspainting.com', 'info@hartungcoatings.com']

    for to_address in TO_EMAIL_ADDRESSES:
        # Choose a random template and subject line
        template = random.choice(EMAIL_TEMPLATES)
        subject = random.choice(SUBJECT_LINES)

        # Choose a random sender account
        sender_info = random.choice(SENDER_ACCOUNTS)

        # Send the email
        send_email(to_address, subject, template, sender_info)

        # Random delay between emails (e.g., 30 to 90 seconds)
        delay = random.uniform(60, 120)
        time.sleep(delay)

if __name__ == "__main__":
    main()



