from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response(f"""
        <h1>Salam!</h1>
        <p>Your browser is: {user_agent}</p>
        <p>Document with cookie!</p>
    """)
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return f"<h1>Salam, {name}!</h1>"

@app.route('/redirect')
def go():
    return redirect('http://www.example.com')

@app.route('/user_id/<id>')
def get_user(id):
    if id not in ['1', '2']:
        abort(404)
    name = 'Anas' if id == '1' else 'Rema'
    return f"<h1>Hello, {name}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
