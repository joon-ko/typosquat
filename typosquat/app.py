from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import url_for

from typosquat.domain import get_domain_information
from typosquat.similar_domains import get_similar_domain_names

app = Flask(__name__)

@app.route('/')
def ping():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    domain_name = request.data.decode('utf-8')
    typos = get_similar_domain_names(domain_name)
    print(typos)
    augmented_data = []
    for typo in typos:
        available, valuation = get_domain_information(typo)
        augmented_data.append({
            "available": available,
            "valuation": valuation
        })
    print(augmented_data)
    return jsonify(augmented_data)