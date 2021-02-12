from flask import Flask , jsonify

app = Flask(__name__)

FYP_Task = [{

    "id":1,
    "title":"Smart Health Consultant",
},
{
    
    "id":2,
    "title":"Hello World",
},
{
    
    "id":3,
    "title":"Muhammad Kashan",

}]

@app.route('/', methods=['GET','POST'])
def get_fyp():

    return jsonify(FYP_Task)
if __name__ == "__main__":
    
    app.run(threaded=True,port=5000)


