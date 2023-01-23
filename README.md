# WebScrapeTutorial
<br>
Just me following the Beautiful Soup tutorial at https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping

### Step 1: Inspecting the Data Source
- What kinds of changes happen to the URL when you follow different paths?
    #### For the [Fake Python](https://realpython.github.io/fake-jobs/) URLs, we have:
  - The main site: https://realpython.github.io/fake-jobs/
  - A site per position, after clicking 'Apply': https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
    
  #### For the Fake Python page [DOMs](view-source:https://realpython.github.io/fake-jobs/), we have:
  - The main page: each job is stored on a "card", which has "card-content" class that contains:
    - Inside "media" → "media-content":
      - Job title stored in class "title is-5"
      - Company stored in class "subtitle is-6 company"
    - Inside "card" → "card-content" → "content":
      - Location inside "location" - City_Name, Country_Abbreviation
      - Date posted inside "is-small has-text-grey" → "time"
  - A job page:
    - Job Title - h1 class "title is-2"
    - Job Company - h2 class "subtitle is-4 company"
    - in class "content":
      - Description - first paragraph
      - Location - id "location"
      - Date Posted - id "date"


### Future Improvements:
- I would like to add a small CI/CD pipeline to dynamically account for website changes