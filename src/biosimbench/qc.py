def status_for_series(values, label, tolerance=0.10):
    a=[float(x) for x in values if x == x and abs(float(x)) != float("inf")]
    if len(a) < 3: return {"name":label,"status":"WARN","detail":"Insufficient data"}
    q=max(1,int(len(a)*0.2)); first=sum(a[:q])/q; last=sum(a[-q:])/q
    rel=abs(last-first)/(abs(first)+1e-12)
    return {"name":label,"status":"PASS" if rel <= tolerance else "WARN","detail":f"First/last mean change: {rel*100:.1f}%"}

def summary(checks):
    p=sum(x["status"]=="PASS" for x in checks); w=sum(x["status"]=="WARN" for x in checks); f=sum(x["status"]=="FAIL" for x in checks)
    overall="FAIL" if f else ("WARN" if w else "PASS")
    return {"overall":overall,"pass":p,"warn":w,"fail":f}
