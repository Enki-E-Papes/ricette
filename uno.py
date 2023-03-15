from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def ricetteHomeuno():
    return render_template('./ricette.html')

@app.route('/CosceDiPolloGratinate', methods=['GET'])
def CosceDiPolloGratinate():
    return render_template('./CosceDiPolloGratinate.html')

@app.route('/MedaglioniDiFormaggio', methods=['GET'])
def MedaglioniDiFormaggio():
    return render_template('./MedaglioniDiFormaggio.html')

@app.route('/platessaPanata', methods=['GET'])
def platessaPanata():
    return render_template('./platessaPanata.html')

@app.route('/PolpetteDiCarne', methods=['GET'])
def PolpetteDiCarne():
    return render_template('./PolpetteDiCarne.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)    #fà partire il programma