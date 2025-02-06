from main import app
from flask import request, redirect, render_template, url_for, flash
from form import PokedexForm, LoginForm, RegisterForm
from repository.pokedex_repository import PokedexRepository

@app.route('/')
def index():
    pokemons = PokedexRepository.searchAll()
    return render_template('pokedex.html', title="Pokemons capturados", pokemons=pokemons)

@app.route('/add')
def create():
    form = PokedexForm()

    return render_template('add.html', title="Adicionar Pokemon", form=form)

@app.route('/add', methods=['POST'])
def store():
    form = PokedexForm(request.form)
    
    if not form.validate_on_submit():
        flash('Erro ao enviar formulário, tente denovo.')
        return redirect(url_for('create'))
    
    data = getData(form)
    status = getStatus(form)
    
    PokedexRepository.create(data, status)
    
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    form = PokedexForm()
    
    pokemon = PokedexRepository.search(id)
    
    form.name.data = pokemon.name
    form.type_1.data = pokemon.type_1
    form.type_2.data = pokemon.type_2
    form.ability.data = pokemon.ability

    return render_template('edit.html', title="Adicionar Pokemon", form=form, id=id)

@app.route('/edit', methods=['POST'])
def update():
    form = PokedexForm(request.form)
    if not form.validate_on_submit():
        flash('Erro ao enviar formulário, tente denovo.')
        return redirect(url_for('create'))
    
    if request.form.get('_method') != 'PUT':
        flash('Erro ao editar arquivo')
        return redirect(url_for('index')) 
    
    pokemon = PokedexRepository.search(request.form['id'])
    data = getData(form)
    status = getStatus(form)
    
    PokedexRepository.update(pokemon, data, status)
    flash(f'Pokemon {pokemon.name} editado com sucesso')
    return redirect(url_for('index'))
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id: int):
        if request.form.get('_method') != 'DELETE':
            flash('Erro ao deletar arquivo')
            return redirect(url_for('index')) 
        
        pokemon_name = PokedexRepository.search(id).name
        PokedexRepository.delete(id)
    
        flash(f'Pokemon {pokemon_name} removido com sucesso!')
        return redirect(url_for('index'))
    

def getData(form: PokedexForm):
    return {
        'name': form.name.data,
        'type_1': form.type_1.data,
        'type_2': form.type_2.data,
        'ability': form.ability.data
    }
    
def getStatus(form: PokedexForm):
    return {}

@app.route('/register')
def register_form():
    form = RegisterForm()
    render_template('register.html', title="Registre-se", form=form)