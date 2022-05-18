from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/')

def abc():
    return "Homepage"

list=[{
    "Contact": "9987644456",
    "Name": "Raju",
    "done": false,
    "id":2
},{
    "Contact": "9876543222",
    " Name": "Raju",
    "done": false,
    "id":2
}]

@app.route('/DataSet', methods=["POST"])
def xyz():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact', "")
        'done':False

    }
    list.append(contact)
    return jsonify({
        "status":"succesful", "message":"contact_added_succcesfully"
    })

@app.route('/Info')
def fgh():
    return jsonify({
        "data":list
    })
if __name__ =="__main__":
    app.run(debug=True, port=1828)

