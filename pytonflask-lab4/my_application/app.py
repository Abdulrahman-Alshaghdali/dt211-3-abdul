from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


@app.route("/listfile")
def files():
	path = "./uploads"
	dircs = os.listdir(path)


	for each_file in dircs:
		files = str(files + each_file + " ")
	return files
