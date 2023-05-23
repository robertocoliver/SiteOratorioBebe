from extensions import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    cor_raca = db.Column(db.String(20))
    reside_com = db.Column(db.String(20))
    outros = db.Column(db.String(100))

class Responsavel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    nome = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)
    situacao = db.Column(db.String(20))
    escolaridade = db.Column(db.String(50))
    estado_civil = db.Column(db.String(20))
    email = db.Column(db.String(100))
    facebook = db.Column(db.String(100))
    orgao_emissor = db.Column(db.String(50))
    profissao = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    numero_nis = db.Column(db.String(20))
    situacao_trabalho = db.Column(db.String(50))
