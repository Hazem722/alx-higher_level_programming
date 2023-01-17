#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv

    value = {'email': argv[2]}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
