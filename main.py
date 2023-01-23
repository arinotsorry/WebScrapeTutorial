"""
Author: Ari WIsenburn
Date: January 22, 2023
"""

import requests
from bs4 import BeautifulSoup

# store constants for website
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get( URL )

# store parsed website
soup = BeautifulSoup( page.content, "html.parser" )

# get IDs from the website
results_container = soup.find( id = "ResultsContainer" )
job_elements = results_container.find_all( "div", class_ = "card-content" )

# for each job we get, get the title, company, and location
list_of_jobs = [ ]
for job_element in job_elements:
    title = (job_element.find( "h2", class_ = "title" )).text.strip()
    company = (job_element.find( "h3", class_ = "company" )).text.strip()
    location = (job_element.find( "p", class_ = "location" )).text.strip()
    list_of_jobs.append( { "title": title, "company": company, "location": location } )

# find jobs including a specific keyword
python_jobs = results_container.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

"""  Before
python_job_elements = []
for h2_element in python_jobs:
    python_job_elements.append(h2_element.parent.parent.parent)
"""

python_job_elements = [ h2_element.parent.parent.parent for h2_element in python_jobs ]

# find links
for job_element in python_job_elements:
    links = job_element.find_all("a")  # html anchors
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
