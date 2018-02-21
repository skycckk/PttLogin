import pexpect
import time

username = ''
password = ''
email = ''

child = pexpect.spawn('ssh bbsu@ptt.cc')
child.expect('new'.encode('big5'))
time.sleep(5)
print('sending username...')
child.sendline(str(username + '\r\n').encode('big5'))
child.expect(':')

time.sleep(5)
print('sending password...')
child.sendline(str(password + '\r\n').encode('big5'))

time.sleep(5)
print('checking password...')
log = child.read(128).decode('utf-8', errors='ignore')
if '密碼不對' in log:
    os.system("echo 'PTT login failed!' | mail -s 'Ptt login warning!' " + email)
    print('Login failed!!')
else:
    print('Login succeed!!')

child.close()
print('done')

