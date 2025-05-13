from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/rastreio/NL123456789BR")

@app.route("/rastreio/<codigo>")
def rastreio(codigo):
    return render_template("rastreio.html", codigo=codigo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)