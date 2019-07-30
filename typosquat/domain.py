import requests
import whois


def get_domain_information(domain_name):
    """
    Returns a tuple (availabile, valuation).
    availabile: boolean, whether or not domain name is available
    valuation: number, price of domain name. None if available is False.
    """
    endpoint = 'https://entourage.dev.aws.godaddy.com/domainsapi/v1/search/exact?q={}'.format(domain_name)
    r = requests.get(endpoint)
    available = r.json()['ExactMatchDomain']['IsAvailable']
    valuation = r.json()['ExactMatchDomain']['Price'] if available else None
    return (available, valuation)


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
