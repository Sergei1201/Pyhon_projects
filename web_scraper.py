from bs4 import BeautifulSoup
import requests

# Request a page you want to scraper with beautiful soup
res = requests.get('https://news.ycombinator.com/')
# Instantiate a Beautiful soup class/ create a beautiful soup object
soup = BeautifulSoup(res.text, 'html.parser')

# Find all links with titles
title_links = soup.select('.titleline')
points = soup.select('.score')

print(title_links)
# Create a function that selects titles, points and adds them into a dictionary


def select_info(links, votes):
    # Initialize an empty list
    scraped_info = []
    # Loop through all the title links and get title text for each link
    for index, item in enumerate(links):
        link = links[index].get('href')
        title = links[index].getText()
        scraped_info.append({'link': link, 'title': title})
    return scraped_info


print(select_info(title_links, points))
