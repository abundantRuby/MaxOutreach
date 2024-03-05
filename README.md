# Email Lead Generation and Outreach Automation

## Overview

Hey There 👋

This program automates the process of lead generation and email outreach. It scrapes Yelp data using their API to find their web address, scrapes the company website for their contact info, and then sends personalized emails using predefined templates. The goal is to streamline the initial communication with potential clients in a scalable and efficient manner.

## Features

- **Yelp Data Scraping**: Gathers company info from their Yelp page
- **Company Website Scraping**: Gathers email addresses from the business' website
- **Email Template Variability**: Utilizes a variety of email templates, ensuring a more natural and personalized outreach experience.
- **Automated Email Sending**: Sends the emails from multiple addresses using a remote access code and SMTP servers

## Configuration

1. **Yelp API Key**: Replace the placeholder `pMIqEfqQPOncD...` with your Yelp API key in the `get_listing_urls` function.
2. **SMTP Configuration**: Configure your SMTP server settings and Gmail account credentials in the `SMTP_CONFIG` section.
3. **Email Templates and Subjects**: Customize the email templates and subject lines in the `EMAIL_TEMPLATES` and `SUBJECT_LINES` sections.

## Usage

1. Run the `yelp_lead_generation.py` script to collect business profile URLs and website URLs.
2. Run the `email_outreach.py` script to send personalized emails to the extracted contacts.

## Important Notes

- Be mindful of Yelp's API usage policies to avoid any issues. Make sure not to get IP banned.
- Adjust the delay between emails in the `main` function to comply with email service provider limits and to not get shut down

## Other

Your comments or suggestions are extremely appreciated, so please reach out!  
Email 📧: iamdylanhoag@gmail.com  
-Dylan Hoag 😊  
