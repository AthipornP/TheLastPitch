import time
def write_user(f,username,password,isSuccess):
    f.write('Username : ' + username + '\n')
    f.write('password : ' + password + '\n')
    f.write('Login time : {} \n'.format(time.strftime("%d/%m/%Y %H:%M:%S")))
    if isSuccess:
        f.write('Login successfully\n')
    else:
        f.write('Login failed\n')
    f.write('#'*10 +'\n')      

print('Welcome to Test LOGFile')
while True:
    f = open('Logging\\DB.txt','a')
    username = input('Enter username: ')
    password = input('Enter password: ')  
    if username == 'Test' and password == '1234':
        print('Login successfully')    
        write_user(f,username,password,True)
        f.close()
    else:
        print('Your username or passsword is incorrect, try again')
        write_user(f,username,password,False)
        f.close()
        