from flask import Flask , jsonify

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
   
   
   return "<h1>Smart Health Consultant</h1><p>Hello World..!</p>"
if __name__ == "__main__":
   
   
    
   app.run(threaded=True,port=5000)


