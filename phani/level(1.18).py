#WAP CREATE A RANDOM LIST OF LENGTH 10 AND PRINT ALL THE ELEMENTS EXCEPT THE
#ELEMENTS WHICH ARE DIVISIBLE BY 4



r=[1,2,3,4,5,6,7,8,9,10]
for i in r:
    if i%4!=0:
        print(i)