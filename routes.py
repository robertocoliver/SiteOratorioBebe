from datetime import datetime
from model import db, Aluno
from flask import Blueprint, request, render_template, redirect, url_for

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/cadastro_aluno', methods=['POST', 'GET'])
def cadastro_aluno():
    def calcular_idade(data_nascimento):
        hoje = datetime.now().date()
        idade = hoje.year - data_nascimento.year

        # Verificar se o aniversário já ocorreu neste ano
        if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
            idade -= 1

        return idade

    if request.method == 'POST':
        # Obter os valores do formulário
        form = request.form

        # Calcular a idade a partir da data de nascimento
        data_nascimento = datetime.strptime(form['data_nascimento'], '%Y-%m-%d').date()
        idade = calcular_idade(data_nascimento)

        # Salvar a idade no banco de dados
        aluno = Aluno(
            nome=form['nome'],
            data_nascimento=data_nascimento,
            sexo=form['sexo'],
            cor_raca=form['cor_raca'],
            idade=idade
        )

        # Salvar o aluno no banco de dados (exemplo de código a seguir)
        db.session.add(aluno)
        db.session.commit()

        # Redirecionar para a rota 'cadastro_pai'
        return redirect(url_for('routes.cadastro_pai'))
    else:
        if request.method == 'GET':
            return render_template('cadastro_aluno.html')






@bp.route('/cadastro_pai', methods=['POST', 'GET'])
def cadastro_pai():
    if request.method == 'POST':
        # Obter os valores do formulário
        nome = request.form.get('nome')
        data_nascimento = request.form.get('data_nascimento')
        idade = request.form.get('idade')
        sexo = request.form.get('sexo')
        cor_raca = request.form.get('cor_raca')
        reside_com = request.form.get('reside_com')
        outros_reside = request.form.get('outros_reside')
        return redirect(url_for('routes.cadastro_pai'))
    else:
        if request.method == 'GET':
            return render_template('cadastro_pai.html')
