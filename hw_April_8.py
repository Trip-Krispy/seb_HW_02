#list of Fat Tony's admin
ft_admin = ['Sebastian','Seb','Jack','Greg','Jesse']

#define function to display current admin list
def current_list():
    print('\nThis is the current list of admins:')
    print(ft_admin)

#define function allowing user to ADD name to list
def add_list():
    list_update = input('\nWould you like to ADD a member to the list? (y/n)')
    while list_update == 'y':
        name = input('WHO would you like to add?\n')
        if name in ft_admin:
            print('\nThere\'s already a ' + name + ' in the club. You take me for an idiot?')
        else:
            ft_admin.append(name)
            list_update = input('Would you like to add anyone else? (y/n)')

#define function allowing user to DELETE name from list
def delete_list():
    list_update = input('\nWould you like to REMOVE a member from the list? (y/n)')
    while list_update == 'y':
        name = input('WHO would you like to REMOVE?\n')
        if name not in ft_admin:
            print('\nI think you\'ve had too much to drink. There\'s no one by that name here.')
        else:
            ft_admin.remove(name)
            list_update = input('Would you like to remove anyone else? (y/n)')

#print current list
current_list()

#allow user to add admins
add_list()

#print current list
current_list()

#allow user to remove admins
delete_list()

#print current list
current_list()