from flask import Flask,jsonify,request

app=Flask(__name__)

groceries=[
    {
        "name":"carrot",
        "qty":4
    },
    {
        "name":"potato",
        "qty":5
    },
    {
        "name":"tomato",
        "qty":5
    },
]

@app.route("/groceries",methods=['GET'])
def getAll():

    return jsonify(groceries)

@app.route("/groceries/<name>")
def getByName(name):
    for prod in groceries:
        if name==prod["name"]:
            return jsonify(prod)

    return jsonify({"message":"Not present in dictionary."})


@app.route("/delete/<name>",methods=['DELETE'])
def delItem(name):
    for index in range(len(groceries)):
        if groceries[index]["name"]==name:
            del groceries[index]

    return jsonify(groceries)

@app.route("/add",methods=['POST'])
def addItem():
    name=request.json['name']
    qty=request.json['qty']

    temp={"name":name,"qty":qty}

    groceries.append(temp)

    return jsonify(groceries)