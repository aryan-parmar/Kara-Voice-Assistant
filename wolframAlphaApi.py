import wolframalpha as wra
app_id = "23WQ52-7AWUQT5U7P" #----------# get your own at https://products.wolframalpha.com/api/
client = wra.Client(app_id)
def wraout(a):
    try:
        res = client.query(a)
        return res.get('pod')[1].get('subpod').get("plaintext")
    except:
        return "sorry"
def wraout1(a,b):
    try:
        res = client.query(a)
        return res.get('pod')[b].get('subpod').get("plaintext")
    except:
        return "sorry "
