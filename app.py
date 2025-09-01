from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/pagos')
def pagos():
    return render_template('pagos.html')

@app.route('/examen')
def examen():
    return render_template('examen.html')

@app.route('/registro')
def pagos():
    return render_template('registro.html')

@app.route('/panel')
def panel():
    return render_template('panel.html')



@app.route('/ta')
def ta():
    return render_template('ta.html')





@app.route('/repositorio_examenes')
def repositorio_examenes():
    return render_template('repositorio_examenes.html')

@app.route('/transicion')
def transicion():
    return render_template('transicion.html')

@app.route('/examenes')
def examenes():
    return render_template('examenes.html')

@app.route('/logout')
def logout():
    # No hay sesión, solo redirige
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True)

