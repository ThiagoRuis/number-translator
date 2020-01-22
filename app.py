from flask import Flask
from NumberDecoder import NumberDecoder

app = Flask(__name__)

@app.route('/<numero>')
def index(numero):
    decoder = NumberDecoder(int(numero))
    decoder.proccess()
    return decoder.json_output()



if __name__ == '__main__':
    app.run()