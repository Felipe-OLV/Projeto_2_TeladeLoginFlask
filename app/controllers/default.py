from turtle import title
from flask import render_template, session, request, url_for, flash, redirect
from app import app, db, bcrypt
from .tables import User
from .forms import RegistrationForm, LoginForm
import os


@app.route('/')
def index():
    return render_template('teste.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, name=form.name.data, email=form.email.data,
        password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Usuário {form.name.data} cadastrado com sucesso.','sucess')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form,title="Pagina de cadastro")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Email: {form.email.data} logado')
            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash(f'ERRO, NÃO FOI POSSIVEL REALIZAR LOGIN')
    return render_template('login.html',form=form , title="Login")
