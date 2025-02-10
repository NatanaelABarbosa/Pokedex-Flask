from main import app
from models.trainers import Trainers
from flask import request, redirect, session, render_template, url_for, flash, send_from_directory
from form import PokedexForm, LoginForm, RegisterForm
from repository import PokedexRepository, TrainersRepository
from helpers import get_image, remove_image
import time

@app.route('/')
def index():
    pokemons = PokedexRepository.searchAll()
    return render_template('pokedex.html', title="Pokemons capturados", pokemons=pokemons)

@app.route('/pokemon/<id>')
def show_status(id):
    pokemon = PokedexRepository.search(id)
    status = PokedexRepository.getStatus(id)
    
    return render_template('status.html', title=pokemon.name, pokemon=pokemon, status=status)

@app.route('/add')
def create():
    form = PokedexForm()

    if not session['usuario']:
        flash('Faça login para entrar nessa página!')
        return redirect(url_for('login', proxima=url_for('create')))
    
    return render_template('add.html', title="Adicionar Pokemon", form=form)

@app.route('/add', methods=['POST'])
def store():
    form = PokedexForm(request.form)
    
    if not form.validate_on_submit():
        flash('Erro ao enviar formulário, tente denovo.')
        return redirect(url_for('create'))
    
    data = getData(form)
    status = getStatus(form)
    
    pokemon = PokedexRepository.create(data, status)
    
    
    image = request.files['image']
    if (image):
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        image.save(f'{upload_path}/capa_{pokemon.id}-{timestamp}.jpg')
        
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    form = PokedexForm()
    
    if not session['usuario']:
        flash('Faça login para entrar nessa página!')
        return redirect(url_for('login', proxima=url_for('edit', id=id)))
    
    pokemon = PokedexRepository.search(id)
    status = PokedexRepository.getStatus(id)
    
    form.name.data = pokemon.name
    form.type_1.data = pokemon.type_1
    form.type_2.data = pokemon.type_2
    form.ability.data = pokemon.ability

    form.hp.data = status.hp
    form.atk.data = status.atk
    form.def_.data = status.def_
    form.spatk.data = status.spatk
    form.spdef.data = status.spdef
    form.spd.data = status.spd
    
    image = get_image(id)

    return render_template('edit.html', title="Adicionar Pokemon", form=form, id=id, image=image)

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
    status = PokedexRepository.getStatus(pokemon.id)
    data = getData(form)
    status_dict = getStatus(form)
    
    PokedexRepository.update(pokemon, status, data, status_dict)
    
    image = request.files['image']
    
    if image:
        remove_image(pokemon.id)
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        image.save(f'{upload_path}/capa_{pokemon.id}-{timestamp}.jpg')
    
    flash(f'Pokemon {pokemon.name} editado com sucesso')
    return redirect(url_for('index'))
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id: int):
        if not session['usuario']:
            flash('Faça log-in para liberar um pokemon!')
            return redirect(url_for('login'))
    
        if request.form.get('_method') != 'DELETE':
            flash('Erro ao liberar pokemon!')
            return redirect(url_for('index')) 
        
        pokemon_name = PokedexRepository.search(id).name
        PokedexRepository.delete(id)
    
        flash(f'Pokemon {pokemon_name} liberado com sucesso!')
        return redirect(url_for('index'))
    

def getData(form: PokedexForm):
    return {
        'name': form.name.data,
        'type_1': form.type_1.data,
        'type_2': form.type_2.data,
        'ability': form.ability.data
    }
    
def getStatus(form: PokedexForm):
    return {
        'hp': form.hp.data,
        'atk': form.atk.data,
        'def': form.def_.data,
        'spatk': form.spatk.data,
        'spdef': form.spdef.data,
        'spd': form.spd.data
    }

@app.route('/register')
def register_form():
    form = RegisterForm()
    
    return render_template('register.html', title="Registre-se", form=form)

@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    trainers_repo = TrainersRepository()

    if form.validate_on_submit():  
        name = form.name.data
        nickname = form.nickname.data
        password = form.password.data

    if trainers_repo.check_if_nickname_exists(nickname):
        flash(f'Erro: O nickname {nickname} já existe! Tente novamente.')
        return redirect(url_for('register'))
    
    trainer = Trainers(name=name, nickname=nickname, password=password)
    trainers_repo.register(trainer)
    
    flash(f'Usuário {name} registrado com sucesso!')
    return redirect(url_for('index'))

@app.route('/login')
def login_form():
    form = LoginForm()
    
    proxima = '/'
    if request.args.get('proxima'):
        proxima = request.args.get('proxima')
    
    return render_template('login.html', title="Faça seu login", form=form, proxima=proxima)

@app.route('/login', methods=['POST'])
def login():
    
    form = LoginForm(request.form)
    trainers_repo = TrainersRepository()
    
    if form.validate_on_submit():  
        nickname = form.nickname.data
        password = form.password.data
        
    error_msg = f'Erro: nickname ou senha incorretos! Tente novamente.'
    if not trainers_repo.check_if_nickname_exists(nickname):
        flash(error_msg)
        return redirect(url_for('login'))
    
    if not trainers_repo.check_password(nickname, password):
        flash(error_msg)
        return redirect(url_for('login')) 
    
    trainers_repo.login(nickname)
    
    flash(f'Usuário {nickname} logado com sucesso!')
    return redirect(request.form.get('proxima'))

@app.route('/logout')
def logout():
    TrainersRepository.logout()
    
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)