from urllib.parse import urlparse


def normalize(url):
    parsed = urlparse(url)
    return f'{parsed.scheme}://{parsed.netloc}'.lower()