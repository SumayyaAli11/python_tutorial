#while loop is used to execute a set of statements as long as condition is true
i=1
while i<5:       #2<5:      #3<5  #4<5  #5<5
    print(i)#1     #2       #3    #4
    i=i+1#i=2      #i=3     #i=4  #5

#another example using while loop
password = ''
while password != 'password':
    print('What is the password?')
    password = input()

print('Yes, the password is ' + password)