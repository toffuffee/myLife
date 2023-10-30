from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

users = {
    'toffuffee': 'Paul2003!!!',
    'lizzkai': 'QWERasdf12345!',
}

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
        if loginRequest in users:
            if users[loginRequest] == passwordRequest:
                global isLogged
                isLogged = True
                return redirect('/main')
            else:
                return returnError('Неверный логин или пароль!')
        else:
            return returnError('Такого пользователя не существует!')
        
@app.route('/main', methods=['POST', 'GET'])
def adminka():
    if isLogged==True:
        return render_template('main.html')
    else:
        return returnError('Сначала нужно пройти авторизацию')

if __name__ == '__main__':
    app.run(debug=True, port='9000')