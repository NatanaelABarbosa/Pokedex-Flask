from main import app
from flask import request, redirect, render_template, url_for, flash
from form.pokedex_form import PokedexForm
from repository.pokedex_repository import PokedexRepository

@app.route('/')
def index():
    pokemons = PokedexRepository.fetchAll()
    return render_template('pokedex.html', titulo="Pokemons capturados", pokemons=pokemons)

@app.route('/add')
def create():
    form = PokedexForm()

    return render_template('add.html', titulo="Adicionar Pokemon", form=form)

@app.route('/add', methods=['POST'])
def store():
    form = PokedexForm(request.form)
    
    data = {
        'nome': form.nome.data,
        'tipo': form.tipo.data,
        'abilidade': form.abilidade.data
    }
    status = {}
    
    PokedexRepository.create(data, status)
    
    if not form.validate_on_submit():
        flash('Erro ao enviar formulário, tente denovo.')
        return redirect(url_for('create'))
    
    return redirect(url_for('index'))