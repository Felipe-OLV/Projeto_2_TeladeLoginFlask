from turtle import title
from flask import render_template, session, request, url_for, flash
from app import app, db, bcrypt
from .tables import User
from .forms import RegistrationForm

@app.route('/cadastro', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, 
            username=form.username.data, 
            email=form.email.data,
            password=form.hash_password.data)
        db_session.add(user)
        flash('Registro de conta realizado com sucesso.')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form,title= "Pagina de cadastro")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login")
