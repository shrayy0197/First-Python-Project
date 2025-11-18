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
result=domain#

password=input('enter a password: ')
result=password.strip()
has=len(password)
has=has -2
print("="*33)
step2=password[0]+'*'*has+password[-1]
print(step2.center(50))
print("="*33)
print(result)

#operators
num1=int(input('enter a first number: '))
num2=int(input('enter a second nmber: '))
print(num1+num2)

#operators
num1=int(input('enter a first number: '))
num2=int(input('enter a second nmber: '))
print(num1//num2)

num1=[1,2,3,4]
num1+=num2
print(num1)

num1=[1,2,3,4]
num2=num1       #effect parcha original lai modify nagarera naya return garcha tara effect gardaina cuz a lai no effect
num1=num1+num2
print(num1)
print(num2)

num1=[1,2,3,4]
num2=num1
num1+=num2     #original lai nai modifiy
print(num1)
print(num2)

a=12
b=13
if a!=b and a%2==0:
    print('success')
else:
    print('failed')

student_name=['ram','shyam','abishek','harisharam']    #not in
user_name=(input('eneter a student name: '))
if user_name not in student_name:
    print('true')
else:
    print('false')
student_name='ram'
print('r' not in student_name)

ame='ram'
print(id(name))  #memory location nikalera dine id le

name='ram'
name1='shyam'
print(id(name))
print(id(name1))
print(name is name1)

name=[12]
name1=[12]
print(id(name))
print(id(name1))
print(name is name1)

#string tuple bollen value int float same variable ma multipple value assin garda pani same location aaucha
#  cux they are immutable data type
#list set dictionary they are mutable data type

a=2+3
print(a.real)
print(a.imag) 
#complex and real number
# list[]
tuples=(1,2,3)
print(type(tuples))

#set=(1,2,3)
#dictionary {key-=value}{'ram':'A+'}

a={*()}
print(type(a))    #set

a=12
b=13
print(a&b)
print(bin(a))
print(bin(b))    #check table csampus ma

a=12
b=13
print(~a)   #bitwise not 
