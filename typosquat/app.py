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
    augmented_data = []
    for typo in typos:
        available, current_price, list_price = get_domain_information(typo)
        augmented_data.append({
            "domainName": typo,
            "available": available,
            "currentPrice": current_price,
            "listPrice": list_price
        })
    return jsonify(augmented_data)