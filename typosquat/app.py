from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

from typosquat.similar_domains import get_similar_domain_names

app = Flask(__name__)

@app.route('/')
def ping():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    domain_name = request.data.decode('utf-8')
    return jsonify(get_similar_domain_names(domain_name))
