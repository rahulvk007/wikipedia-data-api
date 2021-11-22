from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


host = "localhost"
user = "root"
password = "rahul3791"
db = "elements"


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
        return render_template('employees.html', result=res, content_type='application/json')
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
