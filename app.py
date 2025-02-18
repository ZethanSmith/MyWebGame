from flask import Flask, render_template, jsonify

app = Flask(__name__)

resources = {"Wood": 0, "Apple": 0}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/collect/<resource>')
def collect(resource):
    if resource in resources:
        resources[resource] += 1
    return jsonify(resources)

if __name__ == '__main__':
    app.run(debug=True)
