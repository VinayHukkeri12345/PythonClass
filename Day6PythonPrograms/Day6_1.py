
from flask import Flask,request,render_template

app=Flask(__name__)



@app.route("/getName/<devname>",methods=['GET'])
def getName(devname):

    return render_template("display.html",name=devname)

