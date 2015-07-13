# Test the storage of Key-Value pairs

from re import sub
from markdown import text_to_muse, text_to_markdown, replacer


# Muse, markdown pairs
test_cases = [

    ( '',  ''),

    ( 'This is a **test** for text', 'This is a **test** for text'),

    ( ' * This is a **test** for text',  '* This is a **test** for text'),

    ( 'link [[LinkText]]', 'link [[LinkText]]'),

]

# Text patterns

muse_text     = 'link [[LinkText][linking text]] more text'
muse_link     = r'\[\[([\w ]+)\]\[([\w ]+)\]\]'
muse_subs     = r'[\2](\1)'

markdown_text = 'link [linking text](LinkText) more text'
markdown_link = r'\[([\w ]+)\]\(([\w ]+)\)'
markdown_subs = r'[[\2][\1]]'

muse_repl     = (muse_link,muse_subs)
markdown_repl = (markdown_link,markdown_subs)


# Compare two strings
def same (s1,s2):
    if s1!=s2:
        print 'Mismatch:%s|%s|'%(s1,s2)
        assert(False) 


# Convert muse text to markdown
def to_markdown_test():
    for t in test_cases:
        same (text_to_markdown(t[0]), t[1])


# Convert muse text to markdown
def from_markdown_test():
    for t in test_cases:
        same (text_to_muse(t[1]), t[0])


# Try to substitute text with a REGEX
def substitute_test():
    same (sub(markdown_link, markdown_subs, markdown_text), muse_text)
    same (sub(muse_link, muse_subs, muse_text), markdown_text)


# Replacement tester
def to_muse_test():
    replacements = (muse_repl,)
    assert (replacer(replacements,muse_text) == markdown_text)

def to_markdown_test():
    replacements = (markdown_repl,)
    assert (replacer(replacements,markdown_text) == muse_text)
    assert (replacer(replacements,muse_text) == muse_text)
    
def round_trip_test():
    replacements = (muse_repl,markdown_repl)
    assert (replacer(replacements,muse_text) == muse_text)
    assert (replacer(replacements,markdown_text) != markdown_text)


# Multiple lines in text block
def multi_line_test():
    text1 = '/n'.join ([ muse_text, markdown_text, 'other text' ])
    text2 = '/n'.join ([ muse_text, muse_text, 'other text' ])
    print text1
    print replacer((markdown_repl,), text1)
    assert (replacer((markdown_repl,), text1) == text2)
