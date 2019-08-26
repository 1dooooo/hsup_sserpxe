import execjs
ctx = execjs.compile(open("./js/tme.js", 'r').read())
mi = ctx.call("api", "JDX000484862692", "jd")
print(mi)