#list of Fat Tony's admin
ft_admin = ['Sebastian','Seb','Jack','Greg','Jesse']

#define function to display current admin list
def current_list():
    print('\nThis is the current list of admins:')
    print(ft_admin)

#allow user to ADD name to list
list_update = input('\nWould you like to ADD a member to the list? (y/n)')
while list_update == 'y':
    name = input('Who would you like to add?\n')
    if name in ft_admin:
        print('\nThere\'s already a ' + name + ' in the club. You take me for an idiot?.')
    else:
        ft_admin.append(name)
        list_update = input('Anyone else you want to add?')

#print updated list
current_list()

#allow user to DELETE name from list
list_update = input('\nWould you like to REMOVE a member from the list? (y/n)')
while list_update == 'y':
    name = input('Who would you like to REMOVE?\n')
    if name not in ft_admin:
        print('\nI think you\'ve had too much to drink. There\'s no one by that name here. Now scram. Skedaddle!')
    else:
        ft_admin.remove(name)
        list_update = input('Anyone else you want to remove?')

#print updated list
current_list()