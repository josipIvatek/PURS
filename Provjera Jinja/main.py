from flask import Flask, url_for, redirect, request, make_response, render_template, session
import jinja2

app = Flask("Prva flask aplikacija")

lista = [ 'jedan', 'dva', 'tri', 'cetiri']
test = 'testiram'

@app.get('/')
def jinja():
    global lista
    response = render_template('jinja.html', naslov='Jinja', test = test, data=lista)
    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
