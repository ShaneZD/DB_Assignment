from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import inspect
from config import Config
from models import db, User, Email, Role, Address, UserRoles

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    if not Role.query.filter_by(name='Admin').first():
        db.session.add(Role(name='Admin'))
    if not Role.query.filter_by(name='User').first():
        db.session.add(Role(name='User'))
    db.session.commit()
    inspector = inspect(db.engine)
    print("Tables created: ", inspector.get_table_names())  # Updated debug statement

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_management')
def user_management():
    user_data = User.query.all()
    print("Users: ", user_data)  # Debug statement
    return render_template('user_management.html', users=user_data)

@app.route('/user', methods=['GET'])
def user_form():
    roles = Role.query.all()
    return render_template('user_form.html', roles=roles)

@app.route('/user_edit/<int:user_id>', methods=['GET', 'POST'])
def user_edit(user_id):
    user_data = User.query.get_or_404(user_id)
    roles = Role.query.all()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        roles = request.form.getlist('roles')
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']

        if Email.query.filter(Email.email == email, Email.user_id != user_id).first():
            flash('Email already exists. Please use another one.')
            return redirect(url_for('user_edit', user_id=user_id))

        user_data.username = username
        user_data.password = password
        user_data.emails[0].email = email
        user_data.addresses[0].street = street
        user_data.addresses[0].city = city
        user_data.addresses[0].state = state
        user_data.addresses[0].zip_code = zip_code

        user_data.roles = []
        for role_id in roles:
            role = Role.query.get(role_id)
            if role:
                user_data.roles.append(role)

        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('user_management'))

    return render_template('user_edit.html', user=user_data, roles=roles)

@app.route('/user', methods=['POST'])
def user_insert():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    roles = request.form.getlist('roles')
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
    print(f"Received data - Username: {username}, Email: {email}, Password: {password}")  # Debug statement

    if User.query.filter_by(username=username).first():
        flash('Username already exists. Please choose another one.')
        return redirect(url_for('user_form'))

    if Email.query.filter_by(email=email).first():
        flash('Email already exists. Please use another one.')
        return redirect(url_for('user_form'))

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()  
    print(f"New user ID: {new_user.id}")  

    new_email = Email(email=email, user_id=new_user.id)
    new_address = Address(street=street, city=city, state=state, zip_code=zip_code, user_id=new_user.id)
    db.session.add(new_email)
    db.session.add(new_address)

    for role_id in roles:
        role = Role.query.get(role_id)
        if role:
            user_role = UserRoles(user_id=new_user.id, role_id=role.id)
            db.session.add(user_role)

    db.session.commit()

    flash('User created successfully!')
    return redirect(url_for('user_management'))

@app.route('/user_delete/<int:user_id>')
def user_delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('user_management'))

@app.route('/user_update/<int:user_id>', methods=['POST'])
def user_update(user_id):
    user = User.query.get_or_404(user_id)
    user.username = request.form['username']
    user.emails[0].email = request.form['email']
    user.password = request.form['password']
    db.session.commit()
    flash('User updated successfully!')
    return redirect(url_for('user_management'))

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/build')
def build():
    return render_template('build.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

