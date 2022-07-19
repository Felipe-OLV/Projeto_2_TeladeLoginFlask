from turtle import title
from flask import render_template, session, request, url_for, flash
from app import app

from .forms import RegistrationForm

@app.route('/', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
        #           form.password.data)
        #db_session.add(user)
        flash('Registro de conta realizado com sucesso.')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form,title= "Pagina de cadastro")

