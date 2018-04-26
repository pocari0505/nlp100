def cngram(n,s,t):
t=s.replace(' ','')
num_of_char=len(t)
for i in range(num_of_char):
	u=t[i-n:i]
	print(u)
s='I am an NLPer'
t='string'
cngram(2,s,t)
'''
t=s.replace(' ','')
num_of_char=len(t)
for i in range(num_of_char):
	u=t[i-2:i]
	print(u)
'''
