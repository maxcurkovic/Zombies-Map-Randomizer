import random

treyarch_maps = ["Nacht Der Untoten", "Verruckt", "Shi No Numa", "Der Riese", "Kino Der Toten", "Ascension", "Call of the Dead", "Five", "Shangri-La", "Moon", "Tranzit", "Town", "Bus Depot", "Farm", "Die Rise", "Mob of the Dead", "Buried", "Origins", "Shadows of Evil", "The Giant", "Der Eisendrache", "Zetsubou No Shima", "Gorod Krovi", "Revelations", "IX", "Blood of the Dead", "Classified", "Voyage of Despair", "Dead of the Night", "Ancient Evil", "Alpha Omega", "Tag Der Toten", "Die Maschine", "Firebase Z", "Mauer Der Toten", "Forsaken", "Outbreak", "Der Anfang"]
non_treyarch_maps = ["Outbreak", "Infection", "Carrier", "Descent", "Zombies in Spaceland", "Rave in the Redwoods", "Shaolin Shuffle", "Attack of the Radioactive Thing", "The Beast from Beyond", "Groesten Haus", "The Final Reich", "The Darkest Shore", "The Shadowed Throne", "The Tortured Path", "The Frozen Dawn"]
challenges = [["High Round Attempt", "Get to the highest round possible!"], ["Normal", "Play as you would a normal game."], ["No Perks", "No perks allowed!"], ["No Gobblegums", "No gobblegums allowed!"],["No Pack-A-Punch", "You cannot use the PaP machine!"], ["Starting Room Challenge", "You cannot leave the starting room at any point!"], ["Gun Game", "You must switch guns from the Mystery Box every round, starting on round 7!"], ["No Juggernog Challenge","This one is self explanatory."],["Two Box Challenge","You may only hit the Mystery Box twice in your game. You must keep those weapons, no wall weapons allowed. You may hit the box again should you get Mule Kick, but same rule applies!"],["Easter Egg Challenge","Complete the Easter Egg on the map. If there is no Easter Egg, pick a different challenge!"],["Rainbow Perk Challenge","Acquire all perks on the map in rainbow order! Order is as follows: Juggernog, Vulture Aid, Double Tap, Stamin-Up, Speed Cola, Mule Kick, Quick Revive, Who's Who, Electric Cherry, Deadshot Daquiri, Tombstone, PhD Flopper and Widows Wine!"]]
custom_maps = []
all_maps = treyarch_maps + non_treyarch_maps

infinite = 1

def main_menu():
    print("Zombies Map Randomizer, alpha version by Max Curkovic")
    print("Updated: March 7th, 2023. To exit, press Q.")
    print("1. Select a random Treyarch map")
    print("2. Select a random non-Treyarch map")
    print("3. Select a random challenge")
    print("4. Create your own list of maps to randomize")
    print("5. Randomize your custom map list")
    print("6. Select a random map from all maps in existence")
    print("7. Add a custom challenge")  
    user_interface()

def return_to_menu():
    yes_no = str(input())
    if yes_no == "N" or yes_no == "n":
        print()
        main_menu()
        
def user_interface():
    choice = str(input())
    print("Choice: " + str(choice))
    while(infinite):
        if choice == "1":
            print("The map you will play is: " + random.choice(treyarch_maps))
            print("Spin again? N to return to menu, any other key to continue")
            return_to_menu()
        elif choice == "2":
            print("The map you will play is: " + random.choice(non_treyarch_maps))
            print("Spin again? N to return to menu, any other key to continue")
            return_to_menu()
        elif choice == "3":
            random_challenge = random.choice(challenges)
            print("The challenge you will play is: " + random_challenge[0])
            print("Description: " + random_challenge[1])
            print("Spin again? N to return to menu, any other key to continue")
            return_to_menu()
        elif choice == "4":
            print("Your current list of maps is as follows: ")
            if custom_maps == []:
                print("Your list is currently empty!")
            else:
                for i in custom_maps:
                    print(i, end = " ")
            print()
            print("Please enter a new map: ")
            new_map = str(input())
            custom_maps.append(new_map)
            all_maps.append(new_map)
            print("Your map, " + new_map + ", has been inputted. Add another? N to return to menu, any other key to continue")
            return_to_menu()
        elif choice == "5":
            if custom_maps == []:
                print("You must add custom maps first before using this feature! Select another option.")
                main_menu()
            else:
                print("The map you will play is: " + random.choice(custom_maps))
                print("Spin again? N to return to menu, any other key to continue")
                yes_no2 = str(input())
                if yes_no2 == "N" or yes_no2 == "n":
                    print()
                    main_menu()
        elif choice == "6":
            print("The map you will play is: " + random.choice(all_maps))
            print("Spin again? N to return to menu, any other key to continue")
            return_to_menu()            
        elif choice == "7":
            challenge_name = str(input("Enter the name of your challenge."))
            challenge_desc = str(input("Enter the description of your challenge."))
            challenges.append([challenge_name, challenge_desc])
            print("Your challenge has been added. Add another? N to return to menu, any other key to continue")
            return_to_menu()
        elif choice == "Q" or choice ==  "q":
            print("Now exiting program. Thank you for using!")
            quit()
        else:
            print("Invalid command. Try again")
            user_interface()
main_menu()
