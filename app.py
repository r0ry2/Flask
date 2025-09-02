from flask import Flask, request, make_response, redirect, abort, render_template

app = Flask(__name__)

# الصفحة الرئيسية: تعرض user-agent + تضيف cookie + تعرض قالب index.html
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response(render_template('index.html', user_agent=user_agent))
    response.set_cookie('answer', '42')
    return response


# صفحة مستخدم بسيطة بالـ ID
@app.route('/user_id/<id>')
def get_user(id):
    if id not in ['1', '2']:
        abort(404)
    name = 'Anas' if id == '1' else 'Rema'
    return f"<h1>Hello, {name}</h1>"


# تحويل إلى موقع خارجي
@app.route('/redirect')
def go():
    return redirect('http://www.example.com')


# صفحة مستخدم ديناميكية + تمرير بيانات للقالب
@app.route('/user/<name>')
def user(name):
    # dictionary
    mydict = {'fruit': 'Apple'}

    # list
    mylist = ['Math', 'Physics', 'Chemistry']

    # variable index
    myindex = 1

    # simple object مع method
    class MyObject:
        def somemethod(self):
            return "Rema"
    myobj = MyObject()

    # HTML content
    html_content = "<b>This is bold text!</b>"

    return render_template('user.html',
                           name=name,
                           mydict=mydict,
                           mylist=mylist,
                           myindex=myindex,
                           myobj=myobj,
                           html_content=html_content)


if __name__ == '__main__':
    app.run(debug=True)
