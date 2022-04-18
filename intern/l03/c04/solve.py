import requests

get = requests.get(
    'https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
).text + requests.get(
    'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
).text + requests.get(
    'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
).text + requests.get(
    'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
).text + requests.get(
    'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
).text

print(get)

res = requests.post(
    f'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string={get}'
).text

print(res)
