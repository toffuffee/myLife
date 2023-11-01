from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import secrets

secret_key = secrets.token_urlsafe(16)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY']=secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'


db = SQLAlchemy(app)
app.app_context().push()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Login : {self.first_name}, Password: {self.password}"


isLogged=False

def returnError(errorStr):
    return render_template('login.html',error=errorStr)

@app.route('/')
def index():
    if isLogged == True:
        return render_template('main.html')
    else:
        return render_template('login.html')

@app.route('/admin/exit', methods=['POST', 'GET'])
def adminExit():
    if request.method=='POST':
        global isLogged
        isLogged = False
        return redirect('/')

@app.route('/admin/login', methods=['POST', 'GET'])
def adminLogin():
    if request.method == 'POST':
        loginRequest = request.form['login']
        passwordRequest = request.form['password']
        try:
            users = db.session.query(Profile).filter(Profile.first_name == loginRequest).one()
            if users.password == passwordRequest:
                    global isLogged
                    isLogged = True
                    return redirect('/main')
            else:
                return returnError('Неверный пароль!')
        except NoResultFound:
            return returnError('Такого пользователя не существует!')
        
@app.route('/main', methods=['POST', 'GET'])
def adminka():
    if isLogged==True:
        return render_template('main.html')
    else:
        return returnError('Сначала нужно пройти авторизацию')


with app.app_context(): 
    db.create_all()

if __name__ == '__main__':
    app.run(port='9000')