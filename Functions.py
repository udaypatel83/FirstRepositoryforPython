from functools import reduce

def first_fun(a,b,c=10):
    '''
    this function is the first function

    '''
    print (__value__)
    return (a+b+c)

#===========================================================

def dog_check(string1):
     return  string1 in string1.lower()


#===========================================================

lst = ['a','e','i','o','u']
def voweltest(str):
    if str[0] in  lst:
        return str + 'ay'
    else:
        return str[1:] +str[0] +'ay'


#print(voweltest('word')    )
#===========================================================

def fib (*args):
    print (args)
    return sum(args)

#print (fib(10,2,4,4,3,5))


#===========================================================

def func(*args, **kwargs):
    print (args, kwargs)
    if 'fruit' in kwargs:
        print ('my favourite fruit is {} {}'.format(args[0], kwargs['fruit']))
    else:
        print('my favourite veg is {}' .format(kwargs['veg']))

#func(10,20,30, fruit1 = 'apple', veg = 'bhindi', fruit='mango')

#===========================================================

def myfunc(a):
    b=''
    c = len(a)
    cc = 0
    while cc < c:
        if cc%2==0:
            b = b + a[cc].upper()

           # print('even char ' + b)
        else:
            b = b + a[cc]

           # print('odd char ' + b)
        cc +=1

    return (b)

#aa= myfun('udaychandrakantpatel')
#print (aa)

#===========================================================


def myfucs (a):
    b= a.split()
    print (b)

    if b[0][0] == b[1][0]:
        return True
    else:
        return False

#print (myfucs('uday auah'))

#===========================================================

def old_mac (a):
     cc = len(a)
     i = 0
     b =''
     while i < cc:
            if i == 0 or i == 3:
                 b = b + a[i].upper()
            else:
                 b = b + a[i]

            i +=1

     return b

#print(old_mac('macdonald'))

#===========================================================

def rev(a):
    return a[::-1]

#print(rev('uday patel'))


#===========================================================

def withinrange(a):
    if  (a >= 90 and a <= 110):
        return True
    elif  (a>=190 and a <= 210):
        return True
    else:
        return False
#
#print(withinrange(115))

#===========================================================

def has33(a):
  '''
    c = len(a)
    i = 0
    while i< c-1:
        if a[i]== 3:
            if a[i] == a[i+1]:
                return True

        i+=1
'''

  for i in range(0, len(a)-1):
      if a[i:i+2] == [3,3]:
          return True

#print(has33([1,1,3,1,3,3]))



#===========================================================


#===========================================================

def sqr(num):

        if (len(num)>1):
            return True
        else:
             return False

abcd = [2,4,5,6]

#print( reduce(lambda a,b:a+b, abcd))


#===========================================================

#sqr1 = lambda num: num**2
#print( sqr1(73))

#===========================================================

def ulstr (str):
    low = 0
    hig = 0
    for i in str:
        if i == i.lower():
            low +=1
        else:
            hig +=1

    return low,hig

str1 = 'Hello Mr Patel, how are you today? Its Friday..'
#a,b = ulstr(str1)

#print (f' Number of low and high characters in the string are: {a} & {b}' )

#===========================================================

def unq (l):
      return set(l)

lis = [1,1,1,3,4,5,3,4,2,1,2]
#print (list(unq(lis)))

#===========================================================

l = [1,2,3,4,5]

#print (reduce(lambda a,b: a*b, l))


#===========================================================

def pal(s):
     n =s [::-1]
     if s ==n:
        return True
     else:
        return False

ss = 'madam'

#print (pal(ss))

#===========================================================

def palspace(ss):
    n = ss.replace(' ','')
    m = n[::-1]
    print ('n is: ' + n)
    print ('m is: ' + m)
    if n ==m:
        return True
    else:
        return False

pal_str = 'nurses run'

#print (palspace(pal_str))

#===========================================================

import string

def ispangram (str):
    print ('Ascii letter are ' +string.ascii_lowercase)
    print  (str.lower().replace(' ',''))
    for i in str.lower():
         if i in string.ascii_lowercase:
              return  True
         else:
              return False

ss = 'The quick brown fox jumps over the lazy dog'

#print (ispangram(ss))



#===========================================================

def ispangram (str1, alph=string.ascii_lowercase):
    alph = set(alph)
    return alph <= set (str1.lower())

#print (ispangram('The quick brown fox jumps over the lazy dog'))
#===========================================================
#print (round(3.4))


#===========================================================

d = {'k1':'value1','k2':'value2'}

print (d.viewitems())



#===========================================================



#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================




#===========================================================
