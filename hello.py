print('''
      *
      * *
      * * *
      * * * *
      * * * * *
      ''')

print('''
            _
           / _)
          / / 
   ._ ^^^_/  
   _/     /
<_.|_|-|_|
      ''')

print('''
      ^--^
      (oo)\_____   
      (---)\     )\//
      ||---w  |
      ||     ||
      ''')
 
print('my name is {1} {3} and i am {2} years old and i love {0} {program} '\
      .format('python','sunil',30,'kc',program='programming'))

name='ram'
result=name.upper()
print(result)

name='ram'
result=name.lower()
print(result)

name='python programming'
result=name.title()
print(result)

name='python'
result=name.center(10,'*')
print(result)

print('*'*30)

name='7'
result=name.zfill(10)
print(result)

name='7'
result=name.ljust(10,'0')
print(result)

invoice_no=7
print('='*33)
print('INVOICE'.center(31))
print(f'Invoice no:INV{str(invoice_no).zfill (5)}'.center(31))
print('Customer:John Doe'.center(31))
print('Amount:$199.99'.center(31))
print('='*33)

receipt_no=45
print('='*33)
print('CASH RECEIPT'.center(31))
print(f'Receipt no:RCP{str(receipt_no).zfill (5)}'.center(31))
print('Date:10-Nov-2025'.center(31))
print('Cashier: Alice Smith')
print('='*33)

ticket_no=12007
print('='*33)
print('MOVIE TICKET'.center(31))
print(f'Ticket:TKT{str(ticket_no) .zfill (5)}'.center(31))
print('Seat:F-12'.center(31))
print('Time:07:30 PM'.center(31))
print('='*33)

name='ram'
print(name[0])

name='ram'
print(name[:])

name='expression'
print(name[-1:7])

programming_language='python programming'
print(programming_language[::7])

value=5
print(f"{value*value}")

name='ram'
password_len=name.count('r')
print(password_len)

name='ram'
result=name.replace('r','R')
print(f"Modified value: (result)")    #transformationi.e.replace method
print(result)

name='ram'
result=name.replace('r','RR')
print(f"Modified value: (result)")
print(result)

name='ram'
result=name.replace('r','R').replace('m','R')
print(f"Modified value: (result)")
print(result)

name='ram'
result=name.maketrans('rm','RR')   #maketrans
print(result)

#print(f"Modified value: {name.translate (result)}")
#print(ord('Z'))# A Z 65 98
#print(ord('a'))# a z  97 122    #aSKIVALUE

username='    ram@gmail.com    '
result= username.rstrip()       #stripmethod
print(result)

username='python program '
result= username.split()        #split method  
print(result)

sername='python program '
result= username.split()
print(''.join(result))      #join method
print('@'.join(result))      #yesma kei add garne

phone_number='+9779828758323'
result=phone_number.startswith('+977')    #startswith
print(result)
#startswithh endswith rfind index rindex

phone_number='image.jpg'
result=phone_number.endswith('.jpg')    #endswith
print(result)

phone_number='image.jpg'
result=phone_number.find('M')    #find index
print(result)               #find index index ko ma value chaina bahnne in aaucha M ra m ma garda 

phone_number='image.jpg'
result=phone_number.index('m')   
print(result)                 #index ma program crash

phone_number='image.jpg'
result=phone_number.rfind('m')   
print(result)

hone_number='image.jpg'
result=phone_number.rfind('m')-len(phone_number)     #yesko calculations imp cha 
print(result)     

domain_name='ram123@gmail.com'
result=domain_name[domain_name.find('@'):]
print(result)

domain_name='ram123@gmail.com'
result=domain_name[6:]
print(result)

full_name=input('Enter your ful name: ').lower() 
result=full_name.split()
print('_'.join(result))

password=input('Enter your password: ').lower()
result=password.split()
result=password.replace('a','@')
result=password.replace('e','3')
result=password.replace('i','!')
result=password.replace('o','0')
result=password.replace('s','$')

password=input('Enter your password: ').lower()
result=password.maketrans('asoei','@$031')
print(f'your secret agent code:{password.translate(result)}0##9')

domain_namename='laxman.kc123@gmail.com'
result=username.find('laxman.kc')    #photos ma garera hera
print(result)


