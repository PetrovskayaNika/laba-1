from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v1/contact", methods=["POST", "GET", "PUT", "DELETE"])
def contact_handler():
    contact_stub = {
        "ID": 0,
        "Username": "",
        "GivenName": "",
        "FamilyName": "",
        "Phone": [
            {
                "TypeID": 0,
                "CountryCode": 0,
                "Operator": 0,
                "Number": 0
            }
        ],
        "Email": [""],
        "Birthdate": ""
    }
    return jsonify(contact_stub)

@app.route("/api/v1/group", methods=["POST", "GET", "PUT", "DELETE"])
def group_handler():
    group_stub = {
        "ID": 0,
        "Title": "",
        "Description": "",
        "Contacts": []
    }
    return jsonify(group_stub)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
