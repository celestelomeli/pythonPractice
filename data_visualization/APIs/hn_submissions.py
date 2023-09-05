from operator import itemgetter

import requests

# Make an API call adn store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json() #python list containing IDs

submission_dicts = [] #use IDs to build set of dictionaries
for submission_id in submission_ids[:5]:
    # Make a separate API call for each submision
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}") #print id along with status 
    response_dict = r.json()

    # Build a dictionary for each article with title, link, and comments
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
# pass itemgetter comments and it sorts in reverse order to place most commented stories first 
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) 
 
 #loop through list and print out title, link to discussion page, and number of comments submission currently has
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
