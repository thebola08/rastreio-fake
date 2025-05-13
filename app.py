from flask import Flask, render_template

app = Flask(__name__)

@app.route("/rastreio/<codigo>")
def rastreio(codigo):
    status_fases = [
        "✅ Pedido Recebido",
        "📦 Separando no Centro de Distribuição",
        "🚚 Enviado para a transportadora",
        "🌎 Em trânsito internacional",
        "📬 Em rota de entrega"
    ]
    return render_template("rastreio.html", codigo=codigo, status=status_fases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)