import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_domain_information(domain_name):
    """
    Returns a tuple (availabile, current_price, list_price).
    availabile: boolean, whether or not domain name is available
    current_price: string, current (possibly sale) price of domain name. None if available is False.
    current_price: string, list price of domain name. None if available is False.
    """
    # figure out if it's available
    html = load_html(domain_name)
    soup = BeautifulSoup(html, 'html.parser')

    # if there is a message like 'domain is taken' or 'fulldomainnocomma.com is available' then it's not available
    available = None
    current_price = None
    list_price = None
    available = bool(soup.find(string='{} is available'.format(domain_name)))
    if available:
        current_price_tag = soup.select('span.h3.text-primary.m-b-0')[0]
        if current_price_tag:
            current_price = current_price_tag.text
        exact_body = soup.select('div.exact-body')[0]
        if exact_body:
            list_price_tag = exact_body.select('span.title.small.m-b-0')
            if list_price_tag:
                list_price = list_price_tag[0].find('s').text
    return (available, current_price, list_price)


def load_html(domain_name):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    endpoint = 'https://www.godaddy.com/domainsearch/find?domainToCheck={}'.format(domain_name)
    driver.get(endpoint)
    time.sleep(3) # ensure the page loads
    return driver.page_source
