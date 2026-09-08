from biosimbench.qc import status_for_series, summary

def test_stable_series():
    r=status_for_series([1,1.01,0.99,1.0], 'test')
    assert r['status']=='PASS'

def test_summary():
    assert summary([{'status':'PASS'},{'status':'WARN'}])['overall']=='WARN'
