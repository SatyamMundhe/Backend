import re
from urllib.request import urlopen

# Get the website URL from the user
url = "https://ful.io"

# Fetch the website's HTML content
html = urlopen(url).read().decode("utf-8")

# Initialize sets to store the social links, email addresses, and contact information
social_links = set()
emails = set()
contact = None

# Use a regular expression to find all social links in the HTML content
social_link_pattern = re.compile(r"(https?://)?(www\.)?(\w+\.)?(facebook|twitter|linkedin|instagram)\.com/[A-Za-z0-9_.-]+")
social_link_matches = social_link_pattern.finditer(html)
for match in social_link_matches:
    social_links.add(match.group())
    
# Use a regular expression to find all email addresses in the HTML content
email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}")
email_matches = email_pattern.finditer(html)
for match in email_matches:
    emails.add(match.group())
    
# Use a regular expression to find the contact information in the HTML content
contact_pattern = re.compile(r"<a href=[^>]*tel:[^>]*>([^<]+)</a>")
contact_match = contact_pattern.search(html)
if contact_match:
    contact = contact_match.group(1)
    
# Print the results
print("Social links -")
for social_link in social_links:
    print(social_link)
print("\nEmail/s -")
for email in emails:
    print(email)   
print("\nContact: -")
print(contact)
