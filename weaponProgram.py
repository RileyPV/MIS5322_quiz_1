import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
weapons = open("weapons.csv", 'r')



# create a csv object from the file object
weapons_file = csv.reader(weapons, delimiter=",")




#skip the header row
next(weapons_file)


#create an empty dictionary named 'weapons_dict'

weapons_dict = {}

#use a for loop to iterate through every row of the csv file
for record in weapons_file:
    print(record)

    
    #use variables for name,speed and range (optional)
    weap_name = (record[0])
    weap_speed = (record[1])
    weap_range = (record[2])
    

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    my_weapon = w.Weapon(weap_name, weap_speed, weap_range)
    # append the name and bullet count to 'weapons_dict'
    weapons_dict["Weapon Name"] = weap_name
    weapons_dict["Bullet Count"]= my_weapon.get_bullets()
    print(weapons_dict)


    # print out the name of the weapon using the appropriate method of the object 
    print(my_weapon.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    print(my_weapon.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    print(my_weapon.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print(my_weapon.get_bullets())

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    
    # use an appropriate loop to keep firing the weapon until all bullets run out
    for count in range(my_weapon.get_bullets()):
        # call the appropriate method to fire a bullet
        my_weapon.fire_bullet(my_weapon.get_bullets())
        # print out the bullet count every time the weapon is fired
        print(my_weapon.get_bullets())

    


#using a loop print out the name and number of bullets from the dictionary
for record in weapons_dict:
    print(weapons_dict["Weapon Name"])
    print(weapons_dict["Bullet Count"])


print(weapons_dict)
    


    




