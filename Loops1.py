#    1
#   123
#  12345
# 1234567
#123456789
#



minline = 1
maxline = 5
i =1
j =5
numprint = 1
str1 = str(numprint)

a = 1
b = 2

while minline <= maxline:
    while j>=i:
        print (' '*j, end="")
        print( str1)
        while a <= b:

            numprint = numprint +1
            str1 = str1 + str(numprint)
            a=a+1
        j= j-1
        a=1


    minline+=1
    print('')


