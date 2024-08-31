pocket=['paper','card','candy']
if 'money' in pocket:
    print('taxi')
else:
    print('bus')

pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print('taxi')
else:

    print('walk')

#다중조건판단
pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print('taxi')
elif card:
    print('taxi')
else:
    print('걸어가라')