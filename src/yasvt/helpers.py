from urllib.parse import urlparse
import re

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

def contains_cyrillic(x):
    return bool(re.search('[\u0400-\u04FF]', x))