from multiprocessing import Process, Manager

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
    with Manager() as manager:
        augmented_data = manager.list()
        processes = []
        for typo in typos:
            p = Process(target=append_domain_information, args=(augmented_data,typo))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        return jsonify(list(augmented_data))

def append_domain_information(data, typo):
    available, current_price, list_price = get_domain_information(typo)
    data.append({
        "domainName": typo,
        "available": available,
        "currentPrice": current_price,
        "listPrice": list_price
    })