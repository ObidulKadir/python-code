
#Optional Argumant

def get_name(firstname,lastname,middlename=''):
    complete_name=firstname
    if middlename:

        complete_name+= "" + middlename
    complete_name+="" + lastname
    return complete_name

print(get_name("sheikh","kadir"))
print(get_name("sheik"," kadir "," obidul "))