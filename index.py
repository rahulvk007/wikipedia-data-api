from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import sqlite3
app = Flask(__name__)

con = sqlite3.connect('elements.db')

@app.route('/', methods=['GET', 'POST'])
def elements():
    if request.method == "POST":
        details = request.form
        at_no = details['atomic_number']
        con = sqlite3.connect('elements.db')
        cur = con.cursor()
        query = "SELECT name,atomic_number,atomic_weight,symbol,electron_configuration FROM elements where atomic_number = " + str(at_no)
        cur.execute(query)
        result = cur.fetchall()
        res = result
        print(res)
        url = 'https://en.wikipedia.org/wiki/' + result[0][0]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.get_text()
        x = soup.find_all('p')
        data = str()
        for i in x:
            data = data + i.get_text() + '\n'
        return render_template('elements.html', result=res,dt = data,nam = result[0][0], content_type='application/json')
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

