function jeff() {
    let domainName = document.getElementById('search_form_input_homepage').value;
    fetch('/result', {
        method: 'POST',
        body: domainName
    }).then(response => {
        response.json().then(data => {
            let resultContainer = document.getElementById('search_form_homepage');
            resultContainer.innerHTML = '';
            let result = document.createElement('div');
            result.innerHTML = data;
            resultContainer.appendChild(result);
        })
    });
}
