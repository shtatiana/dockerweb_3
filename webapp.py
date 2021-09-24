import flask
import sqlite3
import uptime

con = sqlite3.connect('web_app.db')
cur = con.cursor()
check = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
if len(check.fetchall()) == 0:
    cur.execute("CREATE TABLE counter (c1 integer)")
    cur.execute("INSERT INTO counter VALUES (0)")
    con.commit()
    con.close()


app = flask.Flask(__name__)


@app.route("/")
def static_counter():
    con = sqlite3.connect('web_app.db')
    cur = con.cursor()
    query = "SELECT c1 FROM counter"
    html = "<h2>{counter}</h2>"
    a = cur.execute(query)
    return html.format(counter=str(a.fetchall()[0][0]))
    

@app.route("/stat")
def stat():
    con = sqlite3.connect('web_app.db')
    cur = con.cursor()
    incr = "UPDATE counter SET c1 = c1 + 1"
    cur.execute(incr)
    query = "SELECT c1 FROM counter"
    html = "<h2>{counter}</h2>"
    a = cur.execute(query)
    con.commit()
    return html.format(counter=str(a.fetchall()[0][0]))


@app.route("/about")
def about():
    html = "<h3>Hello, Tatiana!</h3>" \
    "<b>Uptime:</b> {uptime}<br/>"
    return html.format(uptime=str(uptime.uptime()))


   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

