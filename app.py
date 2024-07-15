from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')
# ROUTING ///
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', products=products)

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
    app.run(debug=True)