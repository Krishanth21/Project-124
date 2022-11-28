from flask import Flask,render_template as rt
from flask import jsonify, request

app = Flask(__name__)

tasks = [{
        "id" : 1,
        "name" : "Go For A Walk",
        "done" : "Not Completed",
        "contact": "050123456"
    },{
        "id" : 2,
        "name" : "Bake A Cake",
        "done" : "Not Completed",
        "contact": "050123456"
    }]



@app.route('/')
def index():
    return rt("index.html")

@app.route("/test", methods=["POST"])
def add_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json.get("name",""),
        'done': request.json.get("done",""),
        'contact': request.json.get("contact",""),
        
    }
    tasks.append(task)
    return jsonify({
       "data" : tasks
    })





@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 
    
    
app.run(debug = True)