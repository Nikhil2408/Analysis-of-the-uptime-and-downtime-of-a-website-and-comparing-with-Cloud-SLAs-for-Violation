from flask import *
import urllib.request as req
import re
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plaintext',methods=["GET"])
def plaintext():
        try:
            paragraph = request.args.get('inputtext')
            paragraph = paragraph.replace(" ","%20")
            print(paragraph)
            words = paragraph.split("%20")
            result = []
            for i in words:
                i=re.sub('[^a-zA-Z]',"",i)
                i=i.lower()
                conn = req.urlopen("http://0.0.0.0:8082/filtered?inputpara="+i)
                if conn.read().decode("utf-8") == "false":
                    result.append(i)
                else:
                    str = ""
                    for i in range(len(i)):
                        str = str + "*"
                    result.append(str)
            filtered_text = ' '.join(result)
            json_result = {"message":filtered_text}
            resp = jsonify(json_result)
            app.logger.warning('server up,1')
            return resp
        except:
            app.logger.warning('server down,0')

    # try:
    #     string = request.args.get('inputtext')
    #     string = string.replace(" ","%20")
    #     conn = req.urlopen("http://0.0.0.0:8080/filtered?inputpara="+string)
    #     print(conn.read())
    #     app.logger.warning('server up 1')
    # except:
    #     print("Server is down")
    #     app.logger.warning('server down 0')
    #     return "server is down"

if __name__ =='__main__':
    logHandler=RotatingFileHandler('info.csv',maxBytes=1000000000,backupCount=1)
    formatter=logging.Formatter("%(asctime)s  ,%(message)s","%Y-%m-%d,%H:%M:%S")
    logHandler.setFormatter(formatter)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(logHandler)
    app.run(port=8092,debug=True)
