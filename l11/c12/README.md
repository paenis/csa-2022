## Open Box

fake browser url is static, so probably js/cookie/other injection. `SQL_SESSuser` is unusual ("hinted" in challenge.js)

sql injection is the first guess here, so we try to do it through the cookie ([reference](https://resources.infosecinstitute.com/topic/cookie-based-sql-injection/)):
```js
document.cookie = "SQL_SESSuser=342423961827' OR 1=1;"
```

this works and we're in! the flag is billy's user, `billy_goats_gruff`

there's also an admin bypass found in `/assets/challenge/W0121/assets/js/challenge.dc792968.js`:
```js
if (eval(e)) {
  const W = n(435, "Ftd(")
    , c = ["user", n(427, "LGKA"), n(418, "zC[m"), n(444, "N[#u")]
    , o = n(442, "#V[L") + c[2] + W + "=" + document[n(433, "U53!")](n(425, "Sw%q"))[n(437, "NH!q")].jscode
    , t = n(416, "LGKA") + (10 * document[n(432, "4I$j")](n(441, "zAMg"))[n(420, "Ep(Q")].jscode - 42) / 1337;
  window[n(445, "VkX(")] = "" + o + t
}
```
deobfuscating the above reveals that solving the challenge will set the url parameters to `?adminMode=9882259200&ref=73913681.3448018`; we can change this manually to bypass the injection
