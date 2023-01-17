#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    response = r.text

    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
