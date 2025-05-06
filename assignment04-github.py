# Program that takes a file from a repo, replaces strings in that file, and then commits the updated file back to the repo
# Author: Finbar Dennehy

# To use this install package, pip install PyGithub

from github import Github
from config import config as cfg # config file containing API key, not pushed to git.
import requests

# Github API key
apikey = cfg["githubkey"]
g = Github(apikey)

# set variables for repository and file.
repo = g.get_repo("fdennehy/wsaa-assignments")
filename = "Andrew.txt"
fileInfo = repo.get_contents(filename)
urlOfFIle = fileInfo.download_url

# use requests module to store contents of file.
response = requests.get(urlOfFIle)
contentOfFile = response.text
# print(contentOfFile)

# Set string to be replaced (string1) and it's replacement (string2)
string1 = 'Andrew'
string2 = 'Finbar'

# Update the content of the file using string replace
# https://docs.python.org/3/library/stdtypes.html#str.replace
newContents = contentOfFile.replace(string1,string2)
# print(newContents)

# Update the contents of the file on git up by using the function: update_file(path, message, content, sha, branch=NotSet, committer=NotSet, author=NotSet)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents,fileInfo.sha)
print(f"'{string1}' has been replaced by '{string2}' in github.com/{repo.full_name}/{filename}. Github response:") 
print(gitHubResponse)
