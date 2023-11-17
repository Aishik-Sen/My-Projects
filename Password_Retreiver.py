import subprocess
import os
print('\n\n\nWelcome to your personal password retriever')
p1=subprocess.run('netsh wlan show profiles', shell=True, capture_output=True)
a = p1.stdout.decode()
x = a.find('All')
l=a[x:].split('All User Profile     :')
print('Available Wlan Profiles: ')
q=1
for i in l[1:]:
    print(q,'-',i)
    q+=1
z=int(input('Enter your choice: '))

p2=subprocess.run(f'netsh wlan show profile name="{l[z].strip()}" key=clear',shell=True,capture_output=True )
a2 = p2.stdout.decode()
x2 = a2.find('Key Content')
x3 = a2.find('Cost')
print(a2[x2:x3])

print(os.getcwd())