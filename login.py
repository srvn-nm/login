# author : Sarvin Nami
# storedPassword = '12345'
# enteredPassword = input('Please enter your password here.')
# if storedPassword == enteredPassword :
#     print('You logged in successfully!')
# else :
#     print('you entered your password wrong. Please try again.')
# while storedPassword != enteredPassword :
#     enteredPassword = input('you entered your password wrong. Please try again.')
# print('You logged in successfully!')
users = { 'Sarvin' : '12345' , 'Abtin' : '13579' , 'Nazanin' : '02468'}
enteredUsername = input('Please enter your username here : ')
enteredPassword = input('Please enter your password here : ')
# if enteredUsername in users and users[enteredUsername] == enteredPassword :
#     print('You logged in successfully.') 
# else :
#     print('Sorry.Your username or password is incorrect.')
while enteredUsername not in users or users[enteredUsername] != enteredPassword :
    print('Sorry.Your username or password is incorrect.Please try again.')
    enteredUsername = input('Please enter your username here : ')
    enteredPassword = input('Please enter your password here : ')
print('You logged in successfully.') 