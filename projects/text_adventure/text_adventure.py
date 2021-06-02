import time

name = input('Hello, traveler! Tell us your name: ')
print(f'''\nKnight {name} if I got that right. You have a task of banishing a mighty dragon in our castle! 
Please use a \\help command to check the list of commands!\n
Proceed when you are ready.''')

rooms = {'Castle entrance': 1, 'Hallway': 2, 'Shop': 3, 'Room 1': 4, 'Room 2': 5, 'Library': 6, 'Secret room': 7, 'Sword room': 8, 'Drake room': 9}
rooms['Castle entrance'] = {'name': 'Castle entrance', 'doors': {'white': True}, 'monsters': {'count': 0}, 
                            'chest': False, 'sword': False, 'shop': False, 'description': 'Peaceful greenery with a look on a fiery castle.'}
rooms['Hallway'] = {'name': 'Hallway','doors': {'brown': True, 'cyan': True, 'blue': True, 'green': True, 'red': False, 'black': True}, 'monsters': {'count': 0}, 
                    'chest': False, 'sword': False, 'shop': False, 'description': 'A boring hallway.'}
rooms['Shop'] = {'name': 'Shop','doors': {'white': True}, 'monsters': {'count': 0}, 
                    'chest': False, 'sword': False, 'shop': True, 'description': 'Shady shop with a shady shopkeeper.'}
rooms['Room 1'] = {'name': 'Room 1','doors': {'white': True, 'purple': False, 'pink': False}, 'monsters': {'count': 2, 'slime': {'count': 2, 'hp': 10, 'dmg': 3, 'coin': 10}}, 
                    'chest': False, 'sword': False, 'shop': False, 'description': 'Crumbles of what seemed to be a bedroom.'}
rooms['Room 2'] = {'name': 'Room 2','doors': {'white': True, 'green': True}, 'monsters': {'count': 5, 'slime': {'count': 5, 'hp': 10, 'dmg': 3, 'coin': 10}}, 
                    'chest': False, 'sword': False, 'shop': False, 'description': 'Suprisingly well-kept room with a dangerous aura.'}
rooms['Library'] = {'name': 'Library','doors': {'white': True, 'cyan': True}, 'monsters': {'count': 3, 'goblin': {'count': 3, 'hp': 30, 'dmg': 10, 'coin': 30}}, 
                    'chest': False, 'sword': False, 'shop': False, 'description': 'Torn library with 3 strong monsters guarding it.'}
rooms['Secret room'] = {'name': 'Secret room','doors': {'blue': True}, 'monsters': {'count': 0}, 
                    'chest': True, 'sword': False, 'shop': False, 'description': "Shh, it's a secret."}
rooms['Sword room'] = {'name': 'Sword room','doors': {'blue': True}, 'monsters': {'count': 0}, 
                    'chest': False, 'sword': True, 'shop': False, 'description': 'Hidden room with a strange object inside of it.'}
rooms['Drake room'] = {'name': 'Drake room','doors': {'white': True}, 'monsters': {'count': 1, 'drake': {'count': 1, 'hp': 100, 'dmg': 90, 'coin': 1000}}, 
                    'chest': False, 'sword': False, 'shop': False, 'description': 'Final boss room.'}

knight = {'name': name, 'coins': 0, 'hp': 100, 'dmg': 10, 'sword': False, 'magic': False, 'current_room': rooms['Castle entrance']}

def drake_art():
    return '''             __.-/|
             \`o_O'
              =( )=  +-----+
                U|   | RIP |
      /\  /\   / |   +-----+
     ) /^\) ^\/ _)\     |
     )   /^\/   _) \    |
     )   _ /  / _)  \___|_
 /\  )/\/ ||  | )_)\___,|))
<  >      |(,,) )__)    |
 ||      /    \)___)\\
 | \____(      )___) )____
  \______(_______;;;)__;;;)'''

def interact():
    if knight['current_room']['shop']: 
        while True:
            agree = input('You meet the shady shopkeeper. Would you like to buy something? Yes or no\n')
            if agree.lower() == 'no': return
            elif agree.lower() == 'yes':
                buy = input('What do you want to buy: potion (restored 30 HP) for 10 coins, magic (almighty power, 100dmg) for 150 coins, or nothing?\n')
                if buy.lower() == 'nothing': 
                    print('You have choosen to buy nothing.')
                elif buy.lower() == 'magic':
                    if knight['coins'] >= 150:
                        knight['magic'] = True
                        knight['coins'] -= 150
                        print('You have bought the almighty magic! Who knows what could you do with it!')
                    elif knight['magic'] == True:
                        print('You already have the almighty magic!')
                    else: 
                        print('Not enought coins. Go slay some monsters!')
                elif buy.lower() == 'potion':
                    if knight['coins'] >= 10:
                        if knight['hp'] < 100:
                            knight['hp'] += 30
                            knight['coins'] -= 10
                            print(f"You have healed yourself for 10 hp! You have {knight['hp']} HP now!")
                        else: print('Your hp is too high!')
                    else: print('Not enought coins. Go slay some monsters!')
                else: print(f"{buy} is not on sale.")
    elif knight['current_room']['name'] == 'Secret room':
        while True:
            agree = input('You see a shining chest in the corner of the room. Would you like to open it? Yes or no\n')
            if agree.lower() == 'no': return
            elif agree.lower() == 'yes':
                if knight['current_room']['chest'] == False:
                    print('You have already opened this chest.')
                    return
                print('You begin to open the chest')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('You found 100 coins in the chest! You are rich!')
                knight['coins'] += 100
                knight['current_room']['chest'] = False
                return
    elif knight['current_room']['name'] == 'Sword room':
        if knight['current_room']['sword'] == False:
            print('You have already obtained the sword.')
            return
        while True:
            agree = input('You see a shining weapon in the middle of the room. Would you like to take it? Yes or no\n')
            if agree.lower() == 'no': return
            elif agree.lower() == 'yes':
                print('You begin to pull on it')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('.')
                time.sleep(1)
                print('You obtained the almighty sword! Your damage has increased.')
                knight['sword'] = True
                knight['dmg'] += 30
                knight['current_room']['sword'] = False
                return
    elif knight['current_room']['monsters'] == {} or knight['current_room']['monsters']['count'] == 0:
        print('Seems that this area is safe. You can proceed to the next room.')
    else:
        if knight['current_room']['monsters'].get('drake'):
            print('Uh oh. Seems like you encountered a legendary drake. Escape while you can!')
        count = 0
        monst_str = ''
        for k, v in knight['current_room']['monsters'].items():
            if k == 'count':
                count = v
                continue
            monst_str += f"{v['count']} {k}s, "
        while True:
            attack = input(f"This room has {count} monsters, of which there are {monst_str[:len(monst_str)-2]}. Attack? Yes or no\n")
            if attack.lower() == 'no': return
            elif attack.lower() == 'yes':
                damage = knight['dmg']
                if knight['magic'] == True:
                    while True:
                        magic_use = input("Do you want to consume your magic to deal damage in this room? Yes or no")
                        if magic_use.lower() == 'yes':
                            damage = 100
                            break
                        if magic_use.lower() == 'no': break
                for k, v in knight['current_room']['monsters'].items():
                    if k == 'count': 
                        continue
                    print('Attacking', k)
                    renew_hp = v['hp']
                    while knight['hp'] > 0 and v['count'] > 0 and v['hp'] > 0:
                        v['hp'] -= damage
                        print(f"You have dealt {damage} damage to a {k}.")
                        if v['hp'] <= 0:
                            print(f"You have slained a {k}! Earned {v['coin']} coins!")
                            knight['current_room']['monsters']['count'] -= 1
                            knight['coins'] += v['coin']
                            v['count'] -= 1
                            if v['count'] <= 0:
                                continue
                            else: v['hp'] = renew_hp
                        knight['hp'] -= v['dmg']*v['count']
                        print(f"You took {v['dmg']*v['count']} damage! Trying to attack again...\n")
                        time.sleep(3)
                    if v['count'] <= 0:
                        if knight['current_room']['monsters'].get('drake'):
                            print("CONGRATULATIONS. YOU HAVE BEATEN A LEGENDARY DRAKE AND FINISHED THE GAME!!!")
                            print(drake_art())
                        else: print('You have slain all the monsters!')
                        return
                    if knight['hp'] <= 0:
                        if knight['current_room']['monsters'].get('drake'):
                            print("You have been slain by a legendary drake. Can't really blame you...")
                        else: print('YOU HAVE DIED')
                        quit()
                return

def go():
    try:
        go_to_door = user_command.split(' ')[1]
    except:
        print('Wrong command.')
        return

    if go_to_door in knight['current_room']['doors'].keys():
        if go_to_door == 'brown': 
            knight['current_room'] = rooms['Castle entrance']
        if go_to_door == 'white':
            knight['current_room'] = rooms['Hallway']
        if go_to_door == 'blue':
            knight['current_room'] = rooms['Room 1']
        if go_to_door == 'cyan':
            knight['current_room'] = rooms['Room 2']
        if go_to_door == 'black':
            knight['current_room'] = rooms['Shop']
        if go_to_door == 'green':
            knight['current_room'] = rooms['Library']
        if go_to_door == 'purple':
            if knight['current_room']['monsters']['count'] > 0:
                print("You can't proceed. Monsters are guiding this room!")
                return
            knight['current_room'] = rooms['Sword room']
        if go_to_door == 'pink':
            if knight['current_room']['monsters']['count'] > 0:
                print("You can't proceed. Monsters are guiding this room!")
                return
            knight['current_room'] = rooms['Secret room']
        if go_to_door == 'red':
            knight['current_room'] = rooms['Drake room']
        print(f"You entered through the {go_to_door} door into the {knight['current_room']['name']}!")

    else: print("That door isn't connected to this room.")

while True:
    user_command = input('Command: ')
    if user_command == '\\help': print('''All commands:
    \\quit - quits the game
    \\room - gives informations about room you are in and lists all the doors available
    \\go 'door_color' - moves your character through the specified door
    \\interact - use to scout the room, interact with people or objects, or attack
    \\hp - shows your remaining health
    \\coins - shows you remaining coins
    \\dmg - shows how much damage you deal per attack''')
    elif user_command == '\\quit': quit()
    elif user_command == '\\room': print(f"{knight['current_room']['name']}. {knight['current_room']['description']} Doors in current room: {', '.join(list(knight['current_room']['doors'].keys()))}")
    elif user_command == '\\interact': interact()
    elif user_command.startswith('\\go'): go()
    elif user_command == '\\hp': print(f"You have {knight['hp']} HP.")
    elif user_command == '\\coins': print(f"You have {knight['coins']} coins.")
    elif user_command == '\\dmg': print(f"You have {knight['dmg']} damage.")