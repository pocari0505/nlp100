s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

l = s.split(' ')
t = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
keys = [l[i][0] if i + 1 in t else l[i][:2] for i in range(len(l))]
for i, x in enumerate(keys):
    dict[x] = i + 1
print(dict)
