from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        "message":"welcome to simple ToDo List API",
        "status":"online",
        "version":"1.0.0",
        "created_by":"s.k mulwa",
        "inspected_by":"Slyvester Musyoki"
    })
if __name__ == '__ main_':
    db.create_all()
    app.run(debug=True)

    