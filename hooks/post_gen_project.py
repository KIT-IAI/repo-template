import urllib.request
import fileinput
import datetime

license = '{{ cookiecutter.license.lower()|replace(' ', '_')|replace('-', '_')|replace('.', '_')|trim() }}'
author = '{{ cookiecutter.author_name }}'

print('fetch license file for ' + license)

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
