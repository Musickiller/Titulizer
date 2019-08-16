# import for clear()
from os import system, name 

scr_size_x = 50
# scr_size_y = 15

# define clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def titelize1(s, symb = "="):
    s = " " + s + " "
    return s.center(scr_size_x, symb)
        
#
def main_menu():
    #this code will reppeat, can make a function
    s = ""
    while s not in ["x", "q"]:
        clear()
        print ("+" * scr_size_x)
        print ("")
        print (titelize1("Main Menu"))
        print ("")
        print ("+" * scr_size_x)
        print ("")
        print ("1 or i ".ljust(20), "interactive mode")
        print ("x, q ".ljust(20), "exit this program")
        print ("")
        print ("anything else ".ljust(20), "titelize once and close")
        print ("")
        
        s = input("Enter value or 'x' to exit: ")
        
        if s in ["1", "i"]:
            interactive_mode()
            
        else:
            print("")
            print (titelize1(s))
            break
        
#

def interactive_mode():
    #this code will reppeat, can make a function
    s = ""
    while s not in ["x", "q", "b"]:
        clear()
        print ("+" * scr_size_x)
        print ("")
        print (titelize1("Interactive Mode"))
        print ("")
        print ("+" * scr_size_x)
        print ("")
        print ("1".ljust(20), "select a character to fill")
        print ("2".ljust(20), f"adjust field length ({scr_size_x})")
        print ("x, q, b ".ljust(20), "back to main menu")
        print ("")
        print ("anything else ".ljust(20), "make it look nice")
        print ("")
        if s != "":
            print (titelize1(s))
            print("")
        s = input("Enter value or 'x' to return: ")

main_menu()