# to use this install package
# pip install PyGithub

from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)

# Get my own repos
#for repo in g.get_user().get_repos():
    #print(repo.name)

# Get some else's (public) repos
#for repo in g.get_user("fdennehy")
    #print(repo.name)

repo = g.get_repo("fdennehy/aprivateone")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFIle = fileInfo.download_url
#print(fileInfo)
#print(urlOfFIle)

response = requests.get(urlOfFIle)
contentOfFile = response.text
print(contentOfFile)

# Append the text more stuff (with a newline character) to the contents of the file
newContents = contentOfFile + " more stuff \n"
print(newContents)

# Update the contents of the file on git up by using the function 
# update_file(path, message, content, sha, branch=NotSet, committer=NotSet, author=NotSet)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents,fileInfo.sha)
print (gitHubResponse)