from flask import Flask, render_template, request
import prediction as yapayZeka
import os
import requests

app = Flask(__name__)

@app.route("/", methods=['POST',"GET"])
def analizEt():
    array = {
        "result":"",
        "messageType" : ""
    }
        
    
    if request.method == 'POST':
        if request.form["input_text"] == "":
            array["result"] = "Lütfen bir haber giriniz"
            array["messageType"] = "danger"
            return render_template("root.html",array = array)
        else:
            print(request.form["input_text"])
            print(type(request.form["input_text"]))
            array["result"] = yapayZeka.tahminEt(str(request.form["input_text"]))
            if array["result"] == True:
                array["result"] = "Bu haber doğru olarak tahmin edilmiştir."
                array["messageType"] = "success"
            else:
                array["result"] = "Bu haber sahte olarak tahmin edilmiştir."
                array["messageType"] = "danger"
            return render_template("root.html",array = array)
    else:
        return render_template("root.html",array =array)


if __name__ == "__main__":
    app.run()
    