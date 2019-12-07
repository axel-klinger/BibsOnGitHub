import re
import json
import requests
import sys

gitlab_session = requests.Session()

libraries = open("libraries-gitlab.csv", "rt")
lines = libraries.readlines()
json_result_string ='''
{
  "organisations" : [
'''
for line in lines:
    json_result_string += "    {\n"
    parts = line.split(",")
    country = parts[0]
    city = parts[1]
    name = parts[2]
    link = parts[3]
    json_result_string += "      \"name\": \"" + name + "\",\n"
    json_result_string += "      \"country\": \"" + country + "\",\n"
    json_result_string += "      \"city\": \"" + city + "\",\n"
    json_result_string += "      \"url\": \"" + link.replace("\n","") + "\",\n"
    json_result_string += "      \"repositories\": "
    gitlab_orga = re.findall("\/([^\/^$]+)$", link)[0].replace("\n","")
    print(country + "   " + city + "   " + gitlab_orga)

    api_url = "https://gitlab.com/api/v4/groups/" + gitlab_orga + "/projects?include_subgroups=true"

    res = gitlab_session.get(url=api_url)
    repo_data = res.json()
    # while 'next' in res.links.keys():
    #     res=requests.get(res.links['next']['url'])
    #     repo_data.extend(res.json())

    json_result_string += json.dumps(repo_data, indent=4, ensure_ascii=0) + "\n"
    json_result_string += "    },\n"

json_result_string = json_result_string[:-2]
json_result_string += '''
  ]
}
'''

with open("all-libs-gitlab.json", "w") as json_file:
    json_file.write(json_result_string)
