import urllib.request
import fileinput
import datetime

license = '{{ cookiecutter.license.lower()|replace(' ', '_')|replace('-', '_')|replace('.', '_')|trim() }}'
author = '{{ cookiecutter.author_name }}'
gitignore = '{{ cookiecutter.gitignore }}'

def fetchLicense(license, author):
    url = 'https://raw.githubusercontent.com/IQAndreas/markdown-licenses/master/' + license + '.md'
    try:
        with urllib.request.urlopen(url) as u:
            content = u.read().decode('utf8')
            if "<year>" in content:
                content = content.replace("<year>", str(datetime.datetime.now().year))
            if "<copyright holders>" in content:
                content = content.replace("<copyright holders>", author)
            if "<OWNER>" in content:
                content = content.replace("<copyright holders>", author)
            f = open("LICENSE.md", "w")
            f.write(content)
            f.close
    except urllib.error.HTTPError:
        print('No matching license file found! Please provide your own!')


def fetchGitignore(gitignore):
    url = "https://www.toptal.com/developers/gitignore/api/" + gitignore
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'curl/7.54.0'
        }
    )
    try:
        with urllib.request.urlopen(req) as u:
            content = u.read().decode('utf8')
            f = open(".gitignore", "w") 
            f.write(content)
            f.close
    except urllib.error.HTTPError:
        print('Something went wrong fetching your gitignore')    

fetchLicense(license, author)
if gitignore:
    fetchGitignore(gitignore)
print("Post hook completed! 🎉")
