ta = ['aa', 'bb', 'cc', 'dd', 'ee']
ta.append('ff')
ta.append('gg')
print(ta)
del ta[3]
del ta[4]
print(ta)
jk = ['jj', 'll', 'yy']
print(ta + jk)
print(ta * 5)
def list_max(jk):       
	g = jk[0]
	for t in jk:
		if t > g:
			g = t
	return g
   
list_max(jk = ['jj', 'll', 'yy'])
print(list_max(jk = ta))