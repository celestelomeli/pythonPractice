# import requests module
import requests 

# Make an API call and store the response 

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # make call to API
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json() #return response in json format
# total number of python repos
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about repositories 
repo_dicts = response_dict["items"] #store list of dictionaries
print(f"Repositories returned: {len(repo_dicts)}") #print length of dicts to see how many repos

# Examine the first repository
repo_dict = repo_dicts[0] #pull out first item 
print(f"\nKeys: {len(repo_dict)}") # print keys
for key in sorted(repo_dict.keys()):
    print(key)

# Process results
#print(response_dict.keys())


print("\nSelected information about first repository:")
#loop through all dicts and print the following
for repo_dict in repo_dicts: 
    print(f"Name: {repo_dict['name']}") #print name of project
    print(f"Owner:{repo_dict['owner']['login']}") #owner and owner's login name
    print(f"Stars: {repo_dict['stargazers_count']}") # stars recieved 
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}") 
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}") #repo's description