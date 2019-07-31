function setEntry(entry, index, domainName, available, currentPrice, listPrice) {
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
    console.log(available);
    let availableSpan = 'Available: ' + ( available === true ? '<span style="color:green">Yes</span>' : '<span style="color:red">No</span>' );
    let currentPriceSpan = available ? `<span style="color:#3fb54f">${currentPrice}</span>` : '';
    let listPriceSpan = available ? `<span><s>${listPrice}</s></span>` : '';
    resultSnippet.innerHTML = availableSpan + ' ' + currentPriceSpan + ' ' + listPriceSpan;

    resultBody.appendChild(resultExtras);
    resultBody.appendChild(resultSnippet);

    entry.appendChild(resultBody);
}

function isAlphaNumeric(str) {
  var code, i, len;

  for (i = 0, len = str.length; i < len; i++) {
    code = str.charCodeAt(i);
    if (!(code > 47 && code < 58) && // numeric (0-9)
        !(code > 64 && code < 91) && // upper alpha (A-Z)
        !(code > 96 && code < 123)) { // lower alpha (a-z)
      return false;
    }
  }
  return true;
};

function jeff() {
    let loadingContainer = document.getElementById('links');
    loadingContainer.innerHTML = '<div class="box"><div class="loader-03"></div></div>';
    let subDomain = document.getElementById('search_form_input_homepage').value;
    if (isAlphaNumeric(subDomain)) {
        console.log("test");
        let tld_drop_down = document.getElementById('tld_drop_down');
        let tld = tld_drop_down.options[0].value;
        if (tld_drop_down.selectedIndex !== -1) {
            tld = tld_drop_down.options[tld_drop_down.selectedIndex].value;
        }
        let domainName = subDomain + tld;
        fetch('/result', {
            method: 'POST',
            body: domainName
        }).then(response => {
            response.json().then(data => {
                console.log(data);
                let resultContainer = document.getElementById('links');
                resultContainer.innerHTML = '';
                var numDomains = data.length;
                for (var i = 0; i < numDomains; i++) {
                    let result = document.createElement('div');
                    let { domainName, available, currentPrice, listPrice } = data[i];
                    setEntry(result, i, domainName, available, currentPrice, listPrice);
                    resultContainer.appendChild(result);
                }
            })
        });
    } else {
        loadingContainer.innerHTML = '';
        alert("Please enter an alphanumeric domain name.");
    }
}
