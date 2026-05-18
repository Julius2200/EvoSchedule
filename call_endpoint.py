import urllib.request
import urllib.error

req = urllib.request.Request('http://127.0.0.1:5000/run_ga', method='POST')
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print('STATUS', resp.status)
        print(resp.read().decode())
except urllib.error.HTTPError as e:
    print('HTTP ERROR:', e.code)
    print(e.read().decode())
except Exception as e:
    print('ERROR:', type(e).__name__, str(e))
