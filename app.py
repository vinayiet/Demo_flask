from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route with a form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and dynamic response
@app.route('/hello', methods=['POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
