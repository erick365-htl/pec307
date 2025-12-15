from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('gene.html')
@app.route('/INFOr')
def INFOñ():
    return render_template('INFOr.html')
@app.route('/INDICE')
def indice():
  return render_template('INDICE.html')
@app.route('/quejas')
def quejas():
  return render_template('/quejas.html')

if __name__ == '__main__':
    app.run(debug=True)