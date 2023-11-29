from flask import Flask, Response, render_template, request, make_response, session, redirect, url_for

app = Flask("Prva flask aplikacija")

@app.get('/')
def home_page():
    response = render_template('login1.html')

    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)