dic={'name':'pey','phone':'01023396609','birth':'1210'}
#key= name, phone and birth value=pey,01023396609 and 1210

#dictionory add and delete

#add
a={1:'a'}
a[2]='b'
print(a)

a['name']='pey'
print(a)

a[3]=[1,2,3]

grade={'pey':10, 'juliet':90}
print(grade['pey']) #딕셔너리는 리스트나 튜플에 있는 인덱싱을 사용할 수 없다. 

a={'a':1,'b':2}
print(a['a'])
print(a['b'])

dic={'name':'pey','phone':'010233384','birth':'1122'}
print(dic['name'])
print(dic['birth'])

a={1:'a',1:'b'}
print(a)




#dictionary function
a={'name':'pey','phone':'010222','birth':'1210'}
print(a.keys())
print(a.items())

a={'name':'pey','phone':'0102333','birth':'1210'}
print(a.get('birth'))

a={'name':'pey','phone':'0000','birth':'1210'}
print(a.get('foo','bar'))
print('name' in a)
print('email' in a )



mini_code={'name':'Gauss','birth':'1777','age':'30'}
print(mini_code)
