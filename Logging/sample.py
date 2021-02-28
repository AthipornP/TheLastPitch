import time
def write_user():
    f.write('Username : ' + username + '')
    f.write('password : ' + password + '')
    f.write('Login date : {}/{}/{} '.format(time.strftime('%d'),time.strftime('%m'),int(time.strftime('%Y'))+543))
    f.write('Login time : {}/{}/{} '.format(time.strftime('%H'),time.strftime('%M'),time.strftime('%S')))
print('Welcome to Test LOGFile')
while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == 'Test' and password == '1234':
        print('Login successfully')
        f = open('Logging\DB.txt','a')
        f.write(chr(92)*4 +'Login Success ////')
        write_user()
        f.write('#######################')
        f.close()
        break
    else:
        print('Your username or passsword is incorrect, try again')
        f = open('Logging\DB.txt','a')
        f.write('*** Login Error ***')
        write_user()
        f.write('**********************')
        f.close()