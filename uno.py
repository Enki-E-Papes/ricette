from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def ricetteHomeuno():
    return render_template('./ricette.html')

@app.route('/CosceDiPolloGratinate', methods=['GET'])
def CosceDiPolloGratinate(niam):
    return render_template('./CosceDiPolloGratinate.html',testo="E ora di preparare il pranzo!")

@app.route('/MedaglioniDiFormaggio', methods=['GET'])
def MedaglioniDiFormaggio(niam):
    return render_template('./MedaglioniDiFormaggio.html',testo="E ora di preparare il pranzo!")

@app.route('/platessaPanata', methods=['GET'])
def platessaPanata(niam):
    return render_template('./platessaPanata.html',testo="E ora di preparare il pranzo!")

@app.route('/PolpetteDiCarne', methods=['GET'])
def PolpetteDiCarne(niam):
    return render_template('./PolpetteDiCarne.html',testo="E ora di preparare il pranzo!")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)    #fà partire il programma