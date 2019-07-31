function setEntry(entry, index, domainName) {
    actualHref = "http://" + domainName;
    entry.setAttribute("id", "r1-" + String(index));
    entry.setAttribute("class", "result results_links_deep highlight_d result--url-above-snippet");
    entry.setAttribute("data-domain", domainName);
    entry.setAttribute("data-hostname", domainName);
    entry.setAttribute("data-nir", "1");

    let resultBody = document.createElement('div');
    resultBody.setAttribute("class", "result__body links_main links_deep");

    let resultTitle = document.createElement('h2');
    resultTitle.setAttribute("class", "result__title");

    let resultA = document.createElement('a');
    resultA.setAttribute("class", "result__a");
    resultA.setAttribute("rel", "noopener");
    resultA.setAttribute("href", actualHref);
    resultA.innerHTML = domainName;
    resultTitle.appendChild(resultA);
    resultBody.appendChild(resultTitle);

    let resultExtras = document.createElement('div');
    resultExtras.setAttribute("class", "result__extras js-result-extras");

    let resultExtrasURL = document.createElement('div');
    resultExtras.setAttribute("class", "result__extras__url");

    // let resultIcon = document.createElement('span');
    // resultIcon.setAttribute("class", "result__icon");

    let resultHref = document.createElement('a');
    resultHref.setAttribute("href", actualHref);
    resultHref.setAttribute("rel", "noopener");
    resultHref.setAttribute("class", "result__url js-result-extras-url");

    let resultURLDomain = document.createElement('span');
    resultURLDomain.setAttribute("class", "result__url__comain");
    resultURLDomain.innerHTML = domainName

    let resultURLFull = document.createElement('span');
    resultURLDomain.setAttribute("class", "result__url__full");

    resultHref.appendChild(resultURLDomain);
    resultHref.appendChild(resultURLFull);

    resultExtrasURL.appendChild(resultHref);

    resultExtras.appendChild(resultExtrasURL);

    let resultSnippet = document.createElement('div');
    resultSnippet.setAttribute("class", "result__snippet js-result-snippet");
    resultSnippet.innerHTML = "This domain has not yet been bought."; // TODO: actually make this

    resultBody.appendChild(resultExtras);
    resultBody.appendChild(resultSnippet);

    entry.appendChild(resultBody);
}

function jeff() {
    let domainName = document.getElementById('search_form_input_homepage').value;
    fetch('/result', {
        method: 'POST',
        body: domainName
    }).then(response => {
        response.json().then(data => {
            let resultContainer = document.getElementById('links');
            resultContainer.innerHTML = '';
            var eachDomainName = data;
            var numDomains = eachDomainName.length;
            for (var i = 0; i < numDomains; i++) {
                let result = document.createElement('div');

                setEntry(result, i, eachDomainName[i]);
                resultContainer.appendChild(result);
            }
        })
    });
}
