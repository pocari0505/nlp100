s1="パトカー"
s2="タクシー"
ln=len(s1) if len(s1)<len(s2) else len(s2)
print(s1+' + '+ s2)
print (''.join([s1[i]+s2[i] for i in range(ln)]))
