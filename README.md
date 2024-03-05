# Email Lead Generation and Outreach Automation

## Overview

Hey There 👋

This Python script automates the process of email outreach for lead generation. It leverages Yelp data to identify potential business leads, extracts contact information from their websites, and then sends personalized emails using predefined templates. The goal is to streamline the initial communication with potential clients in a scalable and efficient manner.

## Features

- **Yelp Data Extraction**: Gathers business profile URLs from Yelp search results for a specified location and business type.
- **Contact Information Extraction**: Extracts business website URLs from Yelp profiles and further extracts email addresses from those websites.
- **Email Template Variability**: Utilizes a variety of email templates, ensuring a more natural and personalized outreach experience.
- **Time Zone Consideration**: Accounts for the recipient's time zone when sending emails to enhance engagement.

## Prerequisites

- Python 3.x
- Required Python packages can be installed using `pip install -r requirements.txt`.

## Configuration

1. **Yelp API Key**: Replace the placeholder `pMIqEfqQPOncWCYTIDUD...` with your Yelp API key in the `get_listing_urls` function.
2. **SMTP Configuration**: Configure your SMTP server settings and Gmail account credentials in the `SMTP_CONFIG` section.
3. **Email Templates and Subjects**: Customize the email templates and subject lines in the `EMAIL_TEMPLATES` and `SUBJECT_LINES` sections.

## Usage

1. Run the `yelp_lead_generation.py` script to collect business profile URLs and website URLs.
2. Run the `email_outreach.py` script to send personalized emails to the extracted contacts.

## Important Notes

- Be mindful of Yelp's API usage policies to avoid any issues.
- Adjust the delay between emails in the `main` function to comply with email service provider limits.

## Contributors

- [Your Name]

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The script uses the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) library for web scraping.
