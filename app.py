from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:masterkey@localhost/postgres'
app.config['SECRET_KEY'] = '659_!si#47sjqc2*r8e2lt6t1u^co^7v1e+pknxy4tim1mu=@c'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from controllers.permissoes import *
from controllers.usuarios import *
from controllers.produtos import *
from controllers.auth import *
from controllers.agulha import *
from controllers.categoria import *

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')