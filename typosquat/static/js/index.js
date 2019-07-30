function jeff() {
    let domainName = document.getElementById('domain-name').value;
    fetch('/result', {
        method: 'POST',
        body: domainName
    }).then(response => {
        let resultContainer = document.getElementById('result-container');
        resultContainer.innerHTML = '';
        let result = document.createElement('div');
        result.innerHTML = 'hello world';
        resultContainer.appendChild(result);
    });
}
