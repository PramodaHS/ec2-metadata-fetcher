from flask import Flask

app = Flask(__name__)

@app.route('/latest/meta-data/instance-id')
def instance_id():
    return "i-1234567890abcdef0"

@app.route('/latest/meta-data/instance-type')
def instance_type():
    return "t2.micro"

@app.route('/latest/meta-data/placement/availability-zone')
def az():
    return "us-east-1a"

@app.route('/latest/api/token', methods=['PUT'])
def token():
    return "mock-token"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
