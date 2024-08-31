a=[1,2,3,4]
del a[2:]
print(a)

a=[1,2,3]
a.append(4)
print(a)

a=[1,2,3]
a.append([1,2])
print(a)

#append 는 더하다 덧붙이다의 의미가 있음. 

#리스트 정렬 sort
a=[1,4,3,2]
a.sort() # sort() takes no positional arguments
print(a)

#list 뒤집기 reverse
a=['a','b','c']
a.reverse()
print(a)

#위치 반환 index
a=[1,2,3]
a.index(3) #3은 리스트 a의 세 번째 요소(a[2])
print(a)

#리스트에 요소 삽입
a.insert(0,4) #0에다가 4를 입력하라
print(a)

#요소 제거 remove
a=[1,2,3,1,2,3]
a.remove(3) #why plus 1 ????????
print(a)

#리스트 요소 끄집어 내기 pop
a=[1,2,3]
a.pop()
print(a)# 리스트의 맨 마지막 요소를 돌려주고 나머지는 삭제한다. 결과=> [1,2]

#리스트에 포함된 요소 x의 개수 세기 count
a=[1,2,3,1]
print(a.count(1))

#리스트 확장 extend
a=[1,2,3]
b=[6,7]
a.extend(b)
print(a)