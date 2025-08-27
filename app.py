from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f"""
        <h1>Salam!</h1>
        <p>Your browser is: {user_agent}</p>
    """

@app.route('/user/<name>')
def user(name):
    return f"<h1>Salam, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
