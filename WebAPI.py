from flask import Flask , jsonify

app = Flask(__name__)

FYP_Task = [{


   "id" :1,
   "title" : "Hello World",




},
{


   "id" :2,
   "title" : "Muhammad Kashan",




},
{


   "id" :3,
   "title" : "Smart Health Consultant",




}


]



@app.route('/',methods = ["GET","POST"])
def get_book():
    return jsonify ({"FYP_Task" : FYP_Task})

if __name__ == "__main__":
    
    app.run()


