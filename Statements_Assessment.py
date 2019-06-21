
str1 = 'Print only the words that start with s in this sentence'


ll=  (str1.split(' '))

for i in ll:
    if   i[:1] == 's':
         print (i)


#====================================================

#Use range() to print all the even numbers from 0 to 10.

s = range(0,10)
for s in range(0,10):
    if s%2 ==0:
        print (s)

# ====================================================


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

lst = []
for s in range(1,50):
    if s%3 ==0:
        lst.append(s)

print (lst)

# ====================================================


st = 'Print every word in this sentence that has an even number of letters'
ss = st.split(' ')

for i in ss:
    if (len(i)%2 ==0):
        print (f'This word has even numbers of letters:{i}')

for st in st.split():
    if len(st)%2== 0:
        print ('{} is a even word'.format(st))

# ====================================================


#Write a program that prints the integers from 1 to 25. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,25):
    if i%3 ==0 and i%5==0:
        print ('FizzBuzz')
    elif i%3 == 0:
        print ('Fizz')
    elif  i%5==0:
        print ('Buzz')
    else:
        print (i)





# ====================================================

st = 'Create a list of the first letters of every word in this string'
newlist = st.split(' ')
print('newlist is: {} '  .format(newlist))
nst=[]
for i in newlist:

    nst.append(i[:1])

print ('Final output is: {}' .format(nst))


# ====================================================





# ====================================================

# ====================================================






