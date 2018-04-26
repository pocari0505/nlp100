s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
t = s.replace('.','').split(' ')
g1=[1,5,6,7,8,9,15,16,19]
num_of_char=len(t)
dict={}
for i in range(num_of_char):
	if i+1 in g1:
		u=t[i][0:1]
	else:
		u=t[i][0:2]
	dict[u]=i+1

print(dict)
