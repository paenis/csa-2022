fetch("https://play.cyberstart.com/challenge/W0157/Verify", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
  },
  "referrer": "https://play.cyberstart.com/challenge/W0157",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": `first=27250&second=87889&op=plus&ans=${27250+87889}&act=%2Fflashfast%2Fanswer`, // first=1&second=1&op=plus&ans=2&act=%2Fflashfast%2Fanswer
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then(r=>r.text()).then(t=>console.log(t))
