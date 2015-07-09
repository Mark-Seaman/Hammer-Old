#!/usr/bin/env python
# Create a tabbed view of a user document

from os         import chdir
from sys        import argv
from os.path    import join,exists
from re         import compile, IGNORECASE, DOTALL
from subprocess import Popen,PIPE

from util.wiki  import convert_html
from util.files import do_command,read_text
from util.widgets import format_widgets


def group_tabs(text):
    results = []
    groups = text.split('***')
    for i,g in enumerate(groups):
        if i%2>0:
            if i+1<len(groups):
                results.append(groups[i]+groups[i+1])
            else:
                results.append(groups[i])
    return results


# Format one tab of text
def format_tab(text):
    results = ''
    lines   = text.split('\n')
    heading = lines[0]
    body    = lines[1:]
    results += '     <tab heading="%s">\n'%heading
    results +=  '        <div class="page">\n'
    results +=  '        <b>'+heading+'</b>\n'
    results +=  convert_html(body)
    results +=  '        </div>\n'
    results +=  '     </tab>\n'
    return results


# Print all the tabs of text from the file
def format_tabs(text):
    results = ''
    tab_groups = group_tabs(text)
    tabs = text.split('***')
    body = tabs[0].split('\n')
    results += convert_html(body)
    if len(tab_groups)>1:
        results += '<div ng-controller="TabbedViewCtrl">\n'
        results += '  <tabset ng-show="true">\n'
        for g in tab_groups:
            results += format_tab(g)
        results += '  </tabset>\n'
        results += '</div>\n'
    return results


#  Formatter to add tabs to the HTML formatting
def format_doc(filename):
    text = read_text(filename)
    text = format_widgets(filename,text)
    return format_tabs(text)
