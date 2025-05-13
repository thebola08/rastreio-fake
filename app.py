from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        codigo = request.form.get("codigo")
        if codigo:
            return redirect(f"/rastreio/{codigo}")
    return render_template("home.html")

@app.route("/rastreio/<codigo>")
def rastreio(codigo):
    return render_template("rastreio.html", codigo=codigo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)