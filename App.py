from flask import Flask,jsonify,request

app=Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"

tasks=[
    {
        'id':1,
        'title':u'buy groceries',
        'description':u'milk,cheeze,pizza,fruit',
        'done':False
    },
    {
        'id':2,
        'title':u'lern pithon',
        'description':u'mif,sheeze,pizza,fruit',
        'done':False

    }
]
@app.route("/add-data",methods=["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data in correct format"
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description': request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")
def get_tasks():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)
