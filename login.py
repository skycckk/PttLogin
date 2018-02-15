import pexpect
import time

username = ''
password = ''

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
child.close()
print('done')

