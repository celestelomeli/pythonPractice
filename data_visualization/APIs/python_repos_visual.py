# import requests module
import requests 

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response 

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # make call to API
print(f"Status code: {r.status_code}")

# Process results
# Store API response in a variable
response_dict = r.json() #return response in json format
repo_dicts = response_dict["items"] #store list of dictionaries
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url'] #pull url for the project
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    #repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


owner = repo_dict['owner']['login'] #pull owner and description 
description = repo_dict['description']
#plotly allows html code within text elements so we use a line break (br)
label = f"{owner}<br />{description}"
labels.append(label)

# Make visualizations
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
              'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
# total number of python repos
#print(f"Total repositories: {response_dict['total_count']}")



