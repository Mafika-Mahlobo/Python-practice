#function takes a list as an argument and return a string listing elements


def print_list(item_list):

    #appending all list items into empty string while formatting string
    items_str = ''
    for index in range(len(item_list)):
        if index == 0:
            items_str += str(item_list[index])
        elif index < len(item_list) - 1:
            items_str += ', '+str(item_list[index])
        else:
            items_str += ' and '+str(item_list[index])

    return items_str
    
"""
to run, press F5 then call the function in python shell/terminal passing it a list
e.g print_list([1,3,4,'monday','tuesday'])

"""
