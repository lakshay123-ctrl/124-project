from flask import Flask,request,jsonify
app = Flask(__name__)
contacts = [
   { 
    "id":1,
    "name":u"ok",
    "number":u"123456789",
    "done":False
   },
   {
       "id":2,
       "name":u"yes",
       "number":u"234516789",
       "done":False
   }
]
@app.request("/add-data",methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"


        },400)
    contact = {
     "id":tasks[-1]["id"]+1,
     "name":request.json["name"],
     "contact":request.json.get("conatct","")
     "done":False
    }


    contacts.append(contact)
    return.jsonify({
     "status":"success",
     "message":"contact added"
    })
    
if(__name__=="__main__"):
    app.run(debug = True)


    

