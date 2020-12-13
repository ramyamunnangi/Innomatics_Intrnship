from flask import Flask, render_template , request

app = Flask(__name__)

@app.route('/info')
def info():
    return  render_template('info.html')



if(__name__== '__main__'):
    app.run(debug=True)
