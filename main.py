from flask import Flask
from bs4 import BeautifulSoup
import requests
import sys

app = Flask(__name__)

@app.route('/<x>')
def home(x):
    url = 'https://en.wikipedia.org/wiki/' + x
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.get_text()
    x = soup.find_all('p')
    data = str()
    for i in x:
        data = data + i.get_text() + '\n'
    return  data

if __name__ == "__main__":
    app.run()