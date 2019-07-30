function jeff() {
    let domainName = document.getElementById('domain-name').value;
    fetch('/result', {
        method: 'POST',
        body: domainName
    }).then(response => {
        response.json().then(data => {
            let resultContainer = document.getElementById('result-container');
            resultContainer.innerHTML = '';
            let result = document.createElement('div');
            result.innerHTML = data;
            resultContainer.appendChild(result);
        })
    });
}
