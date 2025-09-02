from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap  # ✔ صححنا الاستيراد

app = Flask(__name__)
bootstrap = Bootstrap(app)  # تهيئة Flask-Bootstrap  

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response(render_template('index.html', user_agent=user_agent))
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user_page(name):
    mydict = {'fruit': 'Apple'}
    mylist = ['Math', 'Physics', 'Chemistry']
    myindex = 1

    class MyObject:
        def somemethod(self):
            return "Rema"
    myobj = MyObject()

    html_content = "<b>This is bold text!</b>"

    return render_template('user.html', 
                           name=name, 
                           mydict=mydict, 
                           mylist=mylist, 
                           myindex=myindex, 
                           myobj=myobj, 
                           html_content=html_content)

# تحويل إلى موقع خارجي
@app.route('/redirect')
def go():
    return redirect('http://www.example.com')

# صفحة مستخدم بسيطة بالـ ID
@app.route('/user_id/<id>')
def get_user(id):
    if id not in ['1', '2']:
        abort(404)
    name = 'Anas' if id == '1' else 'Rema'
    return f"<h1>Hello, {name}</h1>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
