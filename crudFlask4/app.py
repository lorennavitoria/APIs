from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:{senha}@localhost/crudAnimais'
app.config['SQL_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Animais(db.Model): #dentro do MySQL será criado uma tabela chamada "animais" (pega de Animais (nome da classe), mas coloca em letra minuscula).
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(70))
    cor = db.Column(db.String(15))

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor


@app.route("/")
def index():
    animais = Animais.query.all()
    return render_template('index.html', animais=animais)


@app.route('/add', methods=['GET', 'POST'])
def addAnimais():
    if request.method == 'POST':
        animal = Animais(request.form['nome'], request.form['cor'])
        db.session.add(animal)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET','POST'])
def editAnimais(id):
    animal = Animais.query.get(id)
    if request.method == 'POST':
        animal.nome = request.form['nome']
        animal.cor = request.form['cor']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', animal=animal)


@app.route('/delete/<int:id>')
def deleteAnimais(id):
    animal = Animais.query.get(id)
    db.session.delete(animal)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
