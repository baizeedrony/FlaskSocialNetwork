'''
Class Example of Python
class user:
    name=''
    email=''
    password=''
    login = False

    def login(self):
        email=input('enter email: ')
        password=input('enter password: ')
        if email == self.email and password == self.password:
            login = True
            print('login successful')
        else:
            print('failed')



    def logout(self):
        login = False
        print('Logged out')

    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.isLoggedIn():
            print('profile name:', self.name,"\n",'&Email:' ,self.email)
        else:
            print('user is not logged in')


user1 = user()

user1.name='rony'
user1.email='baizeedrony@gmail.com'
user1.password="12345"

user1.login()
user1.profile()'''


'''thistupple=("rony","jamil","kamran","faisal")
if "rony" in thistupple:
        print("yes rony is here")
        print(len(thistupple))'''

'''i=1
while i<11:
    print(i)
    if (i==6):
        break
    i+=1'''


'''x=lambda a,b,c:(a*b)+c
print(x(9,3,7))'''


'''def myfunc(n):
    return lambda a:a*n


mydoubler=myfunc(2)
print(mydoubler(3))'''


'''i = 0
while i < 40:
    i += 1
    if i == 10:
        continue
    print(i)'''



'''for i in range (25):
    print(i)'''

x = lambda a, b: a+b
print(x(2, 6))



