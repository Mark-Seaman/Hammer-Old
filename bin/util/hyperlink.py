import re


# Convert the url in a string to an HTML anchor
def muse_double_anchor(url):
    s = r"\[\[([\/\w\.\:\-\_]*)\]\[([ \w\.\-\_\,\?\%]*)\]\]"
    pat = re.compile(s, re.IGNORECASE | re.DOTALL)
    return pat.sub(r' <a href="\1">\2</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_single_anchor(url):
    s = r"\[\[([\/\w\.\-\_]*)\]\]"
    pat = re.compile(s, re.IGNORECASE | re.DOTALL)
    return  pat.sub(r' <a href="\1">\1</a> ', url)

# Convert the url in a string to an HTML anchor
def muse_anchor(url):
    url = muse_double_anchor(url)
    return muse_single_anchor(url)

# Convert the url in a string to an HTML anchor
def url_to_anchor(url):
    s = r"(^|[\n ])(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)"
    pat = re.compile(s, re.IGNORECASE | re.DOTALL)
    return pat.sub(r'\1<a href="\2" target="_blank">\2</a>', url)

# Convert the url in a string to an HTML image tag
def url_to_image(url):
    s = r"\[\[images/(([\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)\]\]"
    pat = re.compile(s, re.IGNORECASE | re.DOTALL)
    return pat.sub(r'<img src="/media/mybook/images/\1" alt="\1">', url)

# Convert the Wiki Words to hyperlinks
def wiki_words(text):
    s = r"[^A-Za-z\"\']*([A-Z][a-z]+[A-Z][a-z]+([A-Z][a-z]+)*)[^A-Za-z\'\"]*"
    pat = re.compile(s, re.DOTALL)
    return muse_anchor(pat.sub(r'[[\1]]', text))

# Convert a single line of muse to html
def convert_links(text1):
    text = text1
    text = url_to_image(text)
    text = url_to_anchor(text)
    text = muse_anchor(text)
    if text==text1: text = wiki_words(text)
    return text
