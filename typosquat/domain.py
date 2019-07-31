import requests
import whois


def get_domain_information(domain_name):
    """
    Returns a tuple (availabile, current_price, list_price).
    availabile: boolean, whether or not domain name is available
    current_price: string, current (possibly sale) price of domain name. None if available is False.
    current_price: string, list price of domain name. None if available is False.
    """
    endpoint = 'https://entourage.prod.aws.godaddy.com/domainsapi/v1/search/exact?q={}'.format(domain_name)
    r = requests.get(endpoint)
    available = r.json()['ExactMatchDomain']['IsAvailable']
    current_price = r.json()['ExactMatchDomain']['SolutionSet']['CurrentPriceDisplay'] if available else None
    list_price = r.json()['ExactMatchDomain']['SolutionSet']['ListPriceDisplay'] if available else None
    return (available, current_price, list_price)


def get_domain_availability(domain_name):
    """
    Slightly janky way to get domain availability using a third party tool.
    Return True if domain name is available, False otherwise.
    """
    try:
        w = whois.whois(domain_name)
    except whois.parser.PywhoisError: # domain name not found
        return False
    return not bool(w['registrar']) # if registrar field is None, it's not registered
