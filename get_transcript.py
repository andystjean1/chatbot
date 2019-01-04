
import re
import requests
from bs4 import BeautifulSoup


#get the transcript for step brothers
def step_brothers():
    response = requests.get("http://www.script-o-rama.com/movie_scripts/s/step-brothers-script-transcript.html")
    if(response.status_code != 200):
        print("bad response step brothers")
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')
    script = soup.find("pre").text.lower()
    script = re.sub(r'\s', r" ", script)
    script = re.sub(r'-', r'', script)
    return script

#get the transcript for super bad
def super_bad():
    response = requests.get("http://www.allreadable.com/mv1bf8aHn9E")
    if(response.status_code != 200):
        print("bad response super bad")
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')
    blockquote = soup.find("div", {"class", "detranscript"})

    quotes = blockquote.find_all("span")[3:]
    script = "".join([q.text+" " for q in quotes])
    script = re.sub("\n", r" ", script)
    return script

#get the transcript for anchormna
def anchorman():
    response = requests.get("http://www.script-o-rama.com/movie_scripts/a/anchorman-script-transcript-anchor-man.html")
    if(response.status_code != 200):
        print("bad response super bad")
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')
    soup = BeautifulSoup(response.content, 'html.parser')
    script = soup.find("pre").text.lower()
    script = re.sub(r'(\n)\1+', r" ", script)
    return script

def get_scripts():
    step_bros = step_brothers()
    sup_bad = super_bad()
    anchor = anchorman()

    return step_bros + " " + sup_bad + " " + anchor
