import re
from urllib.parse import urlparse

def extract_features(url):

    features = {}

    # URL length
    features['length_url'] = len(url)

    # Number of dots
    features['nb_dots'] = url.count('.')

    # Number of hyphens
    features['nb_hyphens'] = url.count('-')

    # HTTPS token
    features['https_token'] = 1 if "https" in url else 0

    # Digits ratio
    digits = sum(c.isdigit() for c in url)
    features['ratio_digits_url'] = digits / len(url)

    # Domain age (dummy for now)
    features['domain_age'] = 1

    # Web traffic (dummy)
    features['web_traffic'] = 1000

    return features