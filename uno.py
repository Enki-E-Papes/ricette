from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def ricetteHomeuno():
    return render_template('./ricette.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma