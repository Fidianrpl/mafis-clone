from flask import Flask
from flask_cors import CORS
import os   # ➕ necesario para leer el puerto de Render

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return {"mensaje": "Backend funcionando"}

# ---------- REGISTRO DE BLUEPRINTS ----------
from auth import bp as auth_bp
from activos import bp as activos_bp
from reportes import bp as reportes_bp
from usuarios import bp as usuarios_bp
from ordenes import bp as ordenes_bp

app.register_blueprint(auth_bp)
app.register_blueprint(activos_bp)
app.register_blueprint(reportes_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(ordenes_bp)

# 🔧 IMPORTANTE para entornos como Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)