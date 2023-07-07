


phonebook = {} # Dictionary to Store the Contact and Number in Key, Value Pair.
menu_choice = 0

def print_menu():
    print('1. New Contact')
    print('2. Existing Contact')
    print('3. Show Phonebook')


def newcontact( contact_name , contact_number, dictionary_to_store ):
    dictionary_to_store[contact_name] = contact_number
    print("Contact Saved.")
    return True

def searchexistingcontact( name , dictionary_name ):
    if name in dictionary_name:
        print("The number is", dictionary_name[name])
        return True
    else:
        print(name, "was not found")
        return False

def DisplayPhoneBoook( phonebook ):

    if ( len(phonebook) == 0 ):
        return False
    else:
        sorted_phonebook =dict(sorted(phonebook.items()))

        for name, phone_no in sorted_phonebook.items() :
            print("Name: ", name, "\tNumber:", phone_no)
        return True
    
def PhoneBookApplication():
    print_menu()
    while True:
        menu_choice = int(input("Type in a number (1-3): "))

        if menu_choice == 1:
            print("Add Name and Number")
            name = input("Name: ")
            phone_no = input("Number: ")
            newcontact( name, phone_no, phonebook )
            print_menu()
            
        elif menu_choice == 2:
            print("Existing contact")
            name = input("Name: ")
            searchexistingcontact ( name, phonebook )
            print_menu()
            
        elif menu_choice == 3:
            
            if ( DisplayPhoneBoook( phonebook ) == False ):
                print ("Phonebook is Empty.")
            print_menu()

