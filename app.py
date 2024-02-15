from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, 
     resources={r"/*": {"origins": "*"}}, 
     methods=['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'], 
     allow_headers=['Content-Type', 'Authorization'])



app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://postgres:masterkey@127.0.0.1/postgres')
app.config['SECRET_KEY'] = os.environ.get('659_!si#47sjqc2*r8e2lt6t1u^co^7v1e+pknxy4tim1mu=@c')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from controllers.agulha import *
from controllers.auth import *
from controllers.categoria import *
from controllers.classe import *
from controllers.composicao import *
from controllers.especieAgulha import *
from controllers.maquinaAgulha import *
from controllers.marcaAgulha import *
from controllers.marcaElastico import *
from controllers.permissoes import *
from controllers.produtos import *
from controllers.tipoElastico import *
from controllers.tipoLinha import *
from controllers.unidade import *
from controllers.usuarios import *

if __name__ == "__main__":
    app.run(port=266, host='0.0.0.0', debug=True)
