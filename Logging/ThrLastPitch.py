import time

def Write_User():
    f.write('Username : ' + username)
    f.write('Password : ' + password)
    f.write('Login date {}'.format(time.strftime('%d/%m/%Y %H:%M:%S')))

print('Welcome test logging')
while True:
    username = input('Enter username:')
    password = input('Enter password:')
    if username =='Test' and password == '1234':
        print('Login success')
        f = open('Logging\\DB.txt','a')
        f.write(chr(92)*4+'Login success ////\n')
        Write_User()
        f.write('#'*10 +'\n')
        f.close()
        break
    else:
        print('Login failed')
        f = open('Logging\\DB.txt','a')
        f.write('Login error\n')
        Write_User()
        f.write('*'*10 +'\n')
        f.close()


    