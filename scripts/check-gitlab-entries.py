import requests

#
# Check all github projects from libraries.csv: is there also an equivalent gitlab.com project (same token)?
# 

gitlab_session = requests.Session()

libraries = open("libraries.csv", "rt")
lines = libraries.readlines()

gitlab_libraries_result = ""

for line in lines:
    parts = line.split(",")
    country = parts[0]
    city = parts[1]
    name = parts[2]
    githublink = parts[3]
    group_token = githublink.replace('https://github.com/','').replace('\n','')
    gitlab_api_url = "https://gitlab.com/api/v4/groups/" + group_token

    res = gitlab_session.get(url=gitlab_api_url)
    if res.status_code == 200:
        print name + " has existing gitlab entry! " + gitlab_api_url
        gitlab_libraries_result += country + "," + city + "," + name + ",https://gitlab.com/" + group_token + "\n" 
    else:
        print name + " without gitlab entry"

print "\nRESULT:\n\n"
print gitlab_libraries_result
