from flask import Flask, render_template, request
import pymysql
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


host = "sql6.freemysqlhosting.net"
user = "sql6453018"
password = "qn3tbANMvd"
db = "sql6453018"


@app.route('/', methods=['GET', 'POST'])
def employees():
    if request.method == "POST":
        details = request.form
        at_no = details['atomic_number']
        con = pymysql.connect(host=host, user=user, password=password,
                              db=db, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        cur.execute(
            "SELECT name,atomic_number,atomic_weight,symbol,electron_configuration FROM elements where atomic_number in (%s)",(at_no,))
        result = cur.fetchall()
        res = result
        url = 'https://en.wikipedia.org/wiki/' + result[0]['name']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.get_text()
        x = soup.find_all('p')
        data = str()
        for i in x:
            data = data + i.get_text() + '\n'
        print(data)
        return render_template('employees.html', result=res,dt = data,nam = result[0]['name'], content_type='application/json')
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

