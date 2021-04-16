import requests

# http://host:port/context/rest/api-name/api-version/path/to/resource

username = input("Please enter your admin username: ")
password = input("Please enter your admin password: ")

jira_url = "http://localhost:8080/JIRA/rest/api/2/project"
bitbucket_url = "http://localhost:7990/Bitbucket/rest/api/1.0/projects"

request_jira = requests.get(jira_url, auth=(username, password))
jira_projects = request_jira.json()

for project in jira_projects:
    print("Project name: {}".format(project['name']))

    payload = {"key": project['key'], "name": project['name']}

    request_bitbucket = requests.post(bitbucket_url, auth=(username, password), json=payload)

    if request_bitbucket.status_code == 201:
        print("Project Created")
    else:
        print("Project Couldn't Created")
        print(request_bitbucket.json())

    print()
