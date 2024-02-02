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
    TO_EMAIL_ADDRESSES = ["dysco712@gmail.com", "iamdylanhoag@gmail.com", "dylan@mgmtwebsites.com", "dylanhoagdigital@gmail.com"]

    for to_address in TO_EMAIL_ADDRESSES:
        # Choose a random template and subject line
        template = random.choice(EMAIL_TEMPLATES)
        subject = random.choice(SUBJECT_LINES)

        # Choose a random sender account
        sender_info = random.choice(SENDER_ACCOUNTS)

        # Send the email
        send_email(to_address, subject, template, sender_info)

        # Random delay between emails (e.g., 30 to 120 seconds)
        delay = random.uniform(3, 12)
        time.sleep(delay)

if __name__ == "__main__":
    main()



