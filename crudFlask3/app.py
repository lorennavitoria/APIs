from flask import Flask,request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crudSorvetes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sorvete(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(30))
    sabor = db.Column(db.String(30))
    preco = db.Column(db.Float(6))

    def __init__(self, nome, sabor, preco):
        self.nome = nome
        self.sabor = sabor
        self.preco =preco



@app.route('/')
def index():
    sorvetes = Sorvete.query.all()
    return render_template('index.html', sorvetes=sorvetes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        sorvete = Sorvete(request.form['nome'], request.form['sabor'], request.form['preco'])
        db.session.add(sorvete)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>',methods=['GET', 'POST'])
def edit(id):
    sorvete = Sorvete.query.get(id)
    if request.method == 'POST':
        sorvete.nome = request.form['nome']
        sorvete.sabor = request.form['sabor']
        sorvete.preco = request.form['preco']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', sorvete=sorvete)


@app.route('/delete/<int:id>')
def delete(id):

    sorvete = Sorvete.query.get(id)
    db.session.delete(sorvete)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
