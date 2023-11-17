import ipinfo
import sys
try:
    ip_address=sys.argv[1]
except IndexError:
    ip_address=input('Enter the IP address (press Enter to enter your own): ')

if not ip_address:
    ip_address=None
access_token='<Insert IPinfo key here>'
##using a client object for calls
handler=ipinfo.getHandler(access_token)
details=handler.getDetails(ip_address)
##printing the details
for key,value in details.all.items():
    try:
        ##try encoding with UTF 8 and ignore errors
        print(f'{key} : {value}'.encode('utf-8', 'ignore').decode('utf-8'))
    except UnicodeEncodeError:
        ##print a placeholder if encding problem
        print(f'{key} : {"<encoding error>"}')
