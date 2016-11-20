from jdong import KeyList, Good

k = KeyList("茶叶")
print(k.get_relist())
print(k.get_relist(2))

g = Good(url = "https://item.jd.com/339997.html")
g = Good("339997")

print(g.get_comments())