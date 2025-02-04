from main import app, db
from flask import request, redirect, render_template, url_for, flash
from form.pokedex_form import PokedexForm

@app.route('/')
def index():
    return render_template('pokedex.html', titulo="Pokemons capturados")

@app.route('/add')
def create():
    form = PokedexForm()

    return render_template('add.html', titulo="Adicionar Pokemon", form=form)

@app.route('/add', methods=['POST'])
def store():
    form = PokedexForm(request.form)
    
    if not form.validate_on_submit():
        flash('Erro ao enviar formulário, tente denovo.')
        return redirect(url_for('create'))
    
    return redirect(url_for('index'))