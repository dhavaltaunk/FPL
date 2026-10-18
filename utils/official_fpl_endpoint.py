'''
https://dev.to/odeeb/fpl-api-endpoints-complete-reference-for-202627-5g3d
'''

import time
import requests

API = 'https://fantasy.premierleague.com/api/'
s = requests.Session()
s.headers['User-Agent'] = 'fpl-endpoint-check/1.0 (personal script)'

def get(path: str):
    r = s.get(API + path, timeout=30)
    return r.status_code, (r.json() if r.headers.get('content-type', '').startswith('application/json') else None)

def run_path(path: str) -> dict:
    status, body = get(path)
    return {'Status': status, 'Data': body}

def main():
    run_path('fixtures/')

if __name__ == '__main__':
    main()


'''
'bootstrap-static/',
'fixtures/',
f'fixtures/?event={gw}',
f'element-summary/{player}/',
f'event/{gw}/live/',
'event-status/',
f'dream-team/{gw}/',
f'entry/{manager}/',
f'entry/{manager}/history/',
f'entry/{manager}/event/{gw}/picks/',
f'entry/{manager}/transfers/',
'leagues-classic/314/standings/?page_standings=2',
'team/set-piece-notes/',
'regions/',
'stats/most-valuable-teams/',
'my-team/1/',
'''
