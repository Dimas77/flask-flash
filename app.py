from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        if text == None or text == '':
            flash ("Anda Belum Mengisi Form!")
            return redirect(url_for('index'))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
