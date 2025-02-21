from flask import Flask
from flask_migrate import Migrate
from extensions import db
from config import Config
from routes import api

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Registrar las rutas
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
