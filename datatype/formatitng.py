a='i eat %d apples' %3
print(a)
b='i eat %s apples' %"tree"
print(b)
number=1
a='i eat %d apple' %number
print(a)
number=10
day='three'
a='i ate %d apples so i was sick for %s days.' %(number,day)
print(a)
# %s string , %c is chatacter, %d is integer and %f Floating-number. 

a='Error is %d%%' %98
print(a)

a= 'i eat {0} mangoes.' .format(3)
print(a)

a='i eat {0} mangoes.' .format('five')
print(a)

number= 3
a='i eat {0} slice of pizzas' .format(number)
print(a)

number=10
day='three'
a='i ate {0} apples. so i was sick for {1}days.' .format(number,day)
print(a)

a='i ate {number} apples. so i was sick for {day} days. ' .format(number=10, day=3)
print(a)

#왼쪽정렬
range='{0:<10}' .format('hi')
print(range)

#오른쪽 정렬
rightRange='{0:>10}' .format('hi')
print(rightRange)

#중간정렬
middle='{0:^10}' .format('hi')
print(middle)

#채우기
plug="{0:=^10}" .format('hi')
print(plug)

#소수점표현
y=3.42134234
floating="{0:0.4f}" .format(y)
print(floating)

a='{{ and }}' .format()
print(a)

#f문자열 포매팅
name='Gauss'
age=30
sentence=f'my name is {name} and i am {age} years old.'
print(sentence)

name='Carl'
age=19
sentence2=f'nice 2 meet you!! my name is {name} and i\'m {age} years old. '
print(sentence2)

age=30
sentence3=f'I will turn {age+1} next year'
print(sentence3)

#문자열 관련 function
a='hobby'
print(a.count('b'))

a='python is the best choice'
print(a.find('b'))

a='life is too short'
print(a.index('t'))

