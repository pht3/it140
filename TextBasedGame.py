
# function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("COVID Text Adventure Game")
    print("you gotta start somewhere, so we are putting you in the Lobby")
    print("Gotta catch 'em...uhmm Collect all 6 items to protect yourself from Covid or dun-dun-dunnnnnnn...Covid")
    print("Move commands: south, north, east, west")
    print("Add to Inventory command, where item is available: 'get'")

'''************************END show_instructions**********************************'''

#displays current room and the valid directions
def displayCurrentRoomInfo(rm, currm, items):

    for room, direct in rm.items():
        if currm == room:
            print('Current Room: ', room)
            for val in direct:
                if(val == 'item'):
                    print('Item to pick up:',val,'-->',direct[val])
                elif(val == 'Message'):
                    print('***********************************')
                else:
                    print('Valid direction from', room,':',val, '-->', direct[val])
            print()

    if len(items) > 0:
        print('Inventory: ', items)
        print()

'''************************END displayCurrentRoomInfo*********************************************'''

#traversing the rooms
#the room layout is also in this function
def roomTraverse():

    # dictionary of rooms, items, and villain
    rooms = {
    # Starting point lobby(north, east, south, west) - no items
        'Lobby': {'South': 'Gift Shop', 'North': 'Delivery Room', 'East': 'Emergency Room', 'West': 'Waiting Room'},
    # east only- item: Globes
        'Waiting Room': {'East': 'Lobby', 'item': 'Gloves','Message':'Rubba dub dub here are the gloves!'},
    # noth and east, item: Lysol Spray
        'Gift Shop': {'North': 'Lobby', 'East': 'Cafeteria', 'item': 'Lysol Spray','Message':'germs...germs everywhere! Take this Lysol Spray!'},
    # west and north, item: Vaccine
        'Emergency Room': {'West': 'Lobby', 'North': 'Intensive Care Unit', 'item': 'Vaccine','Message':'No one likes needles, but it beats the alternative!'},
    # west only - item: face shield
        'Cafeteria': {'West': 'Gift Shop', 'item': 'Face Shield', 'Message':'Be like the Mandalorian and never take it off'},
    # north and east, item: Clorox Wipes
        'Delivery Room': {'East': 'Operation Room', 'South': 'Lobby', 'item': 'Clorox Wipes','Message':'wipe on, wipe off'},
    # west only, item: Surgical Mask
        'Operation Room': {'West': 'Delivery Room', 'item': 'Surgical Mask','Message':'Keep the surgical mask on, this is the way'},
    # South only, VILLAIN!!!
        'Intensive Care Unit': {'South': 'Emergency Room', 'item': 'COVID-19'}  # villain
    }

    # default room that player starts in
    currentRoom = 'Lobby'

    #items collected
    items = []

    # player enter in direction
    user_input = input('There is nothing to pick up in the Lobby, so enter a direction, yes, it is case sensitive: ')

    while user_input.lower() != 'quit':

        #check item count
        if len(items) == 6:
            print('Woo hoo!!!! You collected all 6 items, you are safe from Covid! Thanks for playing!!!')
            exit()

        # checks if Direct input is valid for the currentRoom
        if user_input in rooms[currentRoom]:

            # assigns currentRoom to the new room
            currentRoom = rooms[currentRoom][user_input]
            print('Hey you moved to the', currentRoom)

            #checks currentRoom and item count
            if currentRoom == 'Intensive Care Unit' and len(items) < 6:
                print('You enter a room with Covid and you did not collect all items to protect yourself!')
                print('Game ended, get plenty of rest')

                #i should be writing the logic through instead of exit(), i know
                exit()
            else:
                #displays the new currentRoom and the valid directions
                displayCurrentRoomInfo(rooms, currentRoom, items)

        else:
            print('Invalid command, enter "exit" to quit')

            # displays the new currentRoom and the valid directions
            displayCurrentRoomInfo(rooms, currentRoom, items)

        #picking up an item
        user_input = input('Enter command: ')

        while user_input == 'get' and currentRoom not in ('Lobby','Intensive Care Unit'):

            if rooms[currentRoom]['item'] != 'None':

                #appending item to items list
                item_obtain = rooms[currentRoom]['item']
                items.append(item_obtain)

                # sets item to 'None' to show users no items are available
                rooms[currentRoom]['item'] = 'None'

                print(rooms[currentRoom]['Message'])
                print('you picked up', item_obtain)

                #check item count
                if len(items) == 6:
                    print('Woo hoo!!!! You collected all 6 items, you are safe from Covid! Thanks for playing!!!')
                    exit()
                else:
                    user_input = input('Enter a direction to get out of this room: ')
            else:
                print('You already picked up the item here')
                user_input = input('Enter a direction to get out of this room: ')

    print('Thanks for playing!')

print('Thanks for playing!')

'''****************************END roomTraverse********************************************'''

#main function
def main():
    print()
    show_instructions()
    print()
    roomTraverse()

if __name__ == '__main__':
    main()
