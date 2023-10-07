from flask import*


#初始化 flask 伺服器
app=Flask(
    __name__,
    static_folder="assets",
    static_url_path="/assets"
)
app.secret_key="any string"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/finish")
def finish():
    return render_template("finish.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")

@app.route("/delay")
def delay():
    return render_template("delay.html")

@app.route("/customers_profile")
def customers_profile():
    return render_template("customers_profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__=='__main__':
    app.run(port=5500,debug=True)