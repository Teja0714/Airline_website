from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pass
    return render_template('search.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/tnc")
def tnc():
    return render_template("tnc.html")

@app.route("/tq")
def tq():
    return render_template("tq.html")

@app.route('/addflight', methods=['GET', 'POST'])
def addflight():
    if request.method == 'POST':
        pass
    return render_template('addflight.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        pass
    return render_template('checkout.html')

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        pass
    return render_template('thankyou.html')
