import jaxnerf.train as train
from flask import Flask, jsonify, request

MODELS_PATH = 'gs://nerf-bucket/models'
CHECKPNT_PATH = 'gs://nerf-bucket/chekpoint'
CONFIG_PATH = 'config/'

app = Flask(__name__)

@app.route('/train/',methods=['POST'])
async def basic_train():
    new_flags={
        "data_dir": MODELS_PATH + request.json['data_dir'],
        "train_dir": CHECKPNT_PATH + request.json['train_dir'],
        "config": CONFIG_PATH + request.json['config']
    }
    try:
       print(new_flags)
       #await train.run_train(new_flags)
       #cambiar el estado del proceso de pending o progress bar a terminado
       print("finish")
    except ValueError:
        print(ValueError)
        #cambiar el estado a error
        #get last step
    return  jsonify({"status":"200",
                     "message": "succes"})

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1',port= 3000)