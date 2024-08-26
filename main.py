import os
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime

app = Flask(__name__)

# Configuración de la base de datos con ruta absoluta
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'caja.db')
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Caja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    descripcion = db.Column(db.String(255), unique=True, nullable=False)
    pista = db.Column(db.String(255), nullable=False)
    intentos = db.Column(db.Integer, nullable=False, default=0)
    contrasenya = db.Column(db.String(255), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('contador'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/contador')
@login_required
def contador():
    countdown_date = datetime.datetime(2024, 9, 15)
    if datetime.datetime.now() > countdown_date:
        return redirect(url_for('index'))
    return render_template('contador.html')

@app.route('/')
@login_required
def index():
    countdown_date = datetime.datetime(2024, 9, 15)
    if datetime.datetime.now() > countdown_date:
        cajas = Caja.query.all()
        print(f"Cajas recuperadas: {cajas}")  # Esto imprimirá las cajas en la consola
        return render_template('index.html', cajas=cajas)
    return redirect(url_for('contador'))

@app.route('/abrir_caja/<int:caja_id>', methods=['POST'])
@login_required
def abrir_caja(caja_id):
    password = request.form['contrasenya']
    caja = Caja.query.get(caja_id)

    if not caja:
        flash('Caja no encontrada')
        return jsonify({'success': False})

    if password == caja.contrasenya:
        caja.abierta = True
        db.session.commit()

        # Seleccionar la imagen del regalo en función del ID de la caja
        image_filename = f"img/regalo{caja_id}.png"
        return jsonify({
            'success': True, 
            'image_url': url_for('static', filename=image_filename),
            'caja_id': caja_id
        })
    else:
        flash('Contraseña incorrecta')
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True)
