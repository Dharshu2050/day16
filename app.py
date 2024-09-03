from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    # it will run in local ip 
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)