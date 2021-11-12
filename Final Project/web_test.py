from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return"Hello! Please go to the '/form' URL to input your information."

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f'The URL /data is accessed directly. Try going to "/form" to submit the form'
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data = form_data)

 


    
