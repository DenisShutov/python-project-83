from bs4 import BeautifulSoup


def parsing(response_data):
    soup = BeautifulSoup(response_data, 'html.parser')
    h1_tag = soup.h1
    if h1_tag:
        h1 = cut(h1_tag.get_text())
    else:
        h1 = None
    title_tag = soup.title
    if title_tag:
        title = cut(title_tag.get_text())
    else:
        title = None
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    if meta_tag:
        description = cut(meta_tag.get('content'))
    else:
        description = None
    parsing_data = {
        'h1': h1,
        'title': title,
        'description': description
    }
    return parsing_data


def cut(text):
    text = text.strip()
    if len(text) > 200:
        text = text[:200] + '...'
    return text