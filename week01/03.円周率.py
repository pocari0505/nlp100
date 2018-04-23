s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

l = s.replace(',','').replace('.','').split(' ')
num_of_char = [len(i) for i in l]
print(num_of_char)
