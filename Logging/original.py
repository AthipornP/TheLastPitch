import time
def write_user():
    f.write('Username : ' + username + '\n')
    f.write('password : ' + password + '\n')
    f.write('Login date : {}/{}/{} \n'.format(time.strftime('%d'),time.strftime('%m'),int(time.strftime('%Y'))+543))
    f.write('Login time : {}/{}/{} \n'.format(time.strftime("%H"),time.strftime("%M"),time.strftime("%S")))
print('Welcome to Test LOGFile')
while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == 'Test' and password == '1234':
        print('Login successfully')
        f = open('DB.txt','a')
        f.write(chr(92)*4 +'Login Success ////\n')
        write_user()
        f.write('#######################\n')
        f.close()
        break
    else:
        print('Your username or passsword is incorrect, try again')
        f = open('DB.txt','a')
        f.write('*** Login Error ***\n')
        write_user()
        f.write('**********************\n')
        f.close()
