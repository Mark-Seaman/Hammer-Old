# Observe a list of counters to watch for growth

from dictdiff import dict_diff
from tracker import previous_counts,next_counts,changes

# Test data
past = '''
561 alert_active
369313 alert_change
472267 alert_report
3703 emailer_message
76 market_market
10737 money_collection
23510 money_daily
23511 vend_totalvendcount
23517 vend_vendcount
'''

current = '''
561 alert_active
305682 alert_change
385571 alert_report
2703 emailer_message
13 market_market
10720 money_collection
19080 money_daily
105532 money_export
19081 money_total
19087 vend_vendcount
'''

# Test record compare function
def test_dictdiff():
    x = dict_diff(current,past)
    assert(387==len(x))
    print x


# Test collection persistance
def test_record_counts():
    collection = 'test_tracker/records'
    previous_counts(collection,past)
    next_counts(collection,current)
    x = changes(collection)
    assert(387==len(x))
    print x


