import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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

#print("\nSelected information about first repository:")
#for repo_dict in repo_dicts:
#   print("\nName:", repo_dict['name'])
#   print("Owner:", repo_dict['owner']['login'])
#   print("Stars:", repo_dict['stargazers_count'])
#   print("Repository:", repo_dict['html_url'])
#   print("Created:", repo_dict['created_at'])
#   print("Updated:", repo_dict['updated_at'])
#   print("Description:", repo_dict['description'])
names = []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

#visual
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names 
chart.add('', plot_dicts) 
chart.render_to_file('python_repos4.svg') 
