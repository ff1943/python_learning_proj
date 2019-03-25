import requests

#operate api 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#store and convert json to python dsictionary
response_dict = r.json() 

#print response of dictionary format
#print(response_dict)

#print the value of  key-total_cout
print("Total repositories:", response_dict['total_count'])

#items is a key of dictionary list
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#print first element of the list repo_dicts 
#repo_dict0 = repo_dicts[0]
#print("\nThe first element of the list items: ",repo_dict0)

#print second element of the list repo_dicts and the keys
#repo_dict1 = repo_dicts[1]
#print("\nThe second element of the list items: ",repo_dict1)
#print("\nKeys of the second elemet:", len(repo_dict1))
#for key in sorted(repo_dict1.keys()):
 #   print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
   print("\nName:", repo_dict['name'])
   print("Owner:", repo_dict['owner']['login'])
   print("Stars:", repo_dict['stargazers_count'])
   print("Repository:", repo_dict['html_url'])
   print("Created:", repo_dict['created_at'])
   print("Updated:", repo_dict['updated_at'])
   print("Description:", repo_dict['description'])

