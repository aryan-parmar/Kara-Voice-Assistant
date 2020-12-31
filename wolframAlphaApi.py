import wolframalpha as wra
app_id = 'YOUR API'  # get your own at https://products.wolframalpha.com/api/
client = wra.Client(app_id)
def wraout(a):
    try:
        res = client.query(a)
        return res.get('pod')[1].get('subpod').get("plaintext")
    except Exception as e:
        return e
def wraout1(a,b):
    try:
        res = client.query(a)
        return res.get('pod')[b].get('subpod').get("plaintext")
    except Exception as e:
        return e