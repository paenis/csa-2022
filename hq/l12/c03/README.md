## Account Roulette

briefing basically tells us all we need to know: enumerate cookie values until we have the right user

we can write a simple python script to loop through cookie values and parse out the user until we hit `thedazman`

correct cookie value is `49`, once we have it we can log in with it and refresh to get the flag:
```js
document.cookie = "speek_sess_id=49"
```

the flag is `sztn38EF7s7uhlp0OgHj`, and we're done!
