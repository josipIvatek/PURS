from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for, g
import MySQLdb

app = Flask("Prva flask aplikacija")

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

temperature = [
    {
        'datum': '21.2.2012',
        'vrijednost': 12
    },
    {
        'datum': '1.2.2021',
        'vrijednost': 5
    },
    {
        'datum': '7.6.2023',
        'vrijednost': 23
    },
    {
        'datum': '5.10.2023',
        'vrijednost': 4
    }
]

vlage = [
     {
        'datum': '21.2.2012',
        'vrijednost': 61
    },
    {
        'datum': '1.2.2021',
        'vrijednost': 55
    },
    {
        'datum': '7.6.2023',
        'vrijednost': 53
    },
    {
        'datum': '5.10.2023',
        'vrijednost': 34
    }
]

@app.get('/')
def index():
    global temperature
    global vlage
    id = request.args.get('id')
    if id == '1' or id == None:
        response = render_template('index.html', naslov='Početna stranica', username=session.get('username').capitalize(), data=temperature, tip='Temperatura')
        return response, 20
    if id == '2':   
        response1 = render_template('index.html', naslov='Početna stranica', username=session.get('username').capitalize(), data=vlage, tip='Vlaga')
        return response1, 200


@app.get('/login')
def login():
    response = render_template('login.html', naslov='Stranica za prijavu')
    return response, 200

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))

@app.post('/login')
def check():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template('login.html', naslov='Stranica za prijavu', poruka='Uneseni su pogresni podaci')

@app.post('/temperatura')
def rect():
    temp = request.json.get('temperatura')
    if temp is not None:
        global temperatura
        temperatura.append(temp)
        return 'Uspješno ste upisali', 201
    else:
        return 'Niste upisali ispravan ključ', 404

@app.get('/temperatura')
def last():
    global temperatura
    json = {
        "temperatura":temperatura[-1]
    }
    resp = make_response(json, 202)
    return resp


@app.before_request
def before_request_func():
    g.connection = MySQLdb.connect(host="localhost", user="app", passwd="1234", db="lvj6")
    g.cursor = g.connection.cursor()
    if request.path == '/login' or request.path.startswith('/static') or request.path == '/temperatura':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))
    
@app.after_request
def after_request_func(response):
    g.connection.commit()
    g.connection.close()

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

