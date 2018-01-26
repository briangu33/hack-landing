from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def index(): 
	return render_template("index.html")

app.run(host="0.0.0.0", port=80)