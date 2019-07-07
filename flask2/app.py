from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form_input.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        result = request.form
        print(type(result))
        return render_template('form_result.html',result=result)

if __name__ == "__main__" :
# app.debug = True
    app.run(debug=True)