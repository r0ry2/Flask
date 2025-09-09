from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm  # إضافة FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional

app = Flask(__name__)
bootstrap = Bootstrap(app)

# إعداد Secret Key
app.config['SECRET_KEY'] = 'hard_to_guess_string_123'

    
    # ----- تعريف نموذج UserForm -----
class UserForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[NumberRange(min=1, max=120), Optional()])
    subscribe = BooleanField('Subscribe to newsletter?')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    country = SelectField('Country', choices=[('sa', 'Saudi Arabia'), ('ae', 'UAE'), ('eg', 'Egypt')])
    bio = TextAreaField('Short Bio', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Submit')
    
@app.route('/user_form', methods=['GET', 'POST'])
def user_form():
    form = UserForm()
    if form.validate_on_submit():  # تحقق من صحة البيانات و CSRF
        # استلام البيانات من الحقول
        name = form.name.data
        email = form.email.data
        age = form.age.data
        subscribe = form.subscribe.data
        password = form.password.data
        country = form.country.data
        bio = form.bio.data
        
        # مثال: حفظ البيانات أو إعادة توجيه المستخدم
        return redirect(f'/user_summary/{name}')
    return render_template('user_form.html', form=form)

@app.route('/user_summary/<name>')
def user_summary(name):
    return f"<h1>Thank you, {name}! Your form has been submitted.</h1>"




# ----- صفحة المستخدم للنموذج البسيط -----
@app.route('/user_simple/<name>')
def user_simple_page(name):
    return f"<h1>Hello, {name}!</h1>"

# ----- الصفحة الرئيسية -----
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response(render_template('index.html', user_agent=user_agent))
    response.set_cookie('answer', '42')
    return response

# ----- صفحة المستخدم الأصلية مع محتوى أكثر -----
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

# ----- تحويل إلى موقع خارجي -----
@app.route('/redirect')
def go():
    return redirect('http://www.example.com')

# ----- صفحة مستخدم بسيطة بالـ ID -----
@app.route('/user_id/<id>')
def get_user(id):
    if id not in ['1', '2']:
        abort(404)
    name = 'Anas' if id == '1' else 'Rema'
    return f"<h1>Hello, {name}</h1>"

# ----- معالجات الأخطاء -----
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)  
