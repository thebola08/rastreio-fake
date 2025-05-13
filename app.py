from flask import Flask, render_template

app = Flask(__name__)

@app.route("/rastreio/<codigo>")
def rastreio(codigo):
    return render_template("rastreio.html", codigo=codigo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)