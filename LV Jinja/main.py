from flask import Flask, url_for, redirect, request, make_response, render_template, session

app = Flask("Prva flask aplikacija")


temperatura = []

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.before_request
def before_request_func():
    if request.path == '/login':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))

@app.get('/')
def index():
    response = render_template('index.html')
    return response, 200

@app.get('/login')
def login():
    response = render_template('login.html')
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
        return redirect(url_for('login'))


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)