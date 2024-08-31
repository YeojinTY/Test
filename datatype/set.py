s1=set([1,2,3])
print(s1)

s2=set('hello')
print(s2)

#교집합 intersection
s1=set([1,2,3,4,5])
s2=set([4,5,6,7,8,9])
print(s1.intersection(s2))

#합집합 union
print(s1.union(s2))

#차집합 difference 
print(s1.difference(s2))

s1=set([1,2,3])
print(s1.add(4))

#remove
s1=set([1,2,3])
s1.remove(2)
print(s1)

