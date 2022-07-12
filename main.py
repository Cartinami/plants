import functions
import classes
import bank


print("\nWelcome to Plant Plants. Happy Planting!\n")


def main():
    inventory = classes.Inventory( )
    name = functions.ask_str('What is your name?')
    cash = bank.Bank(name)
    print(cash)
    
    response = None
    while response != 0:
        response = functions.ask_int('\nWhat would you like to do? 1 = New Plant, 2 = View, 3 = Water, 4 = Move, 5 = sell plant, 6 = deposit, 7 = withdrawal 0 = Quit')

        # new plant
        if response == 1:
            name = functions.ask_str('What would you like to name it?')
            inventory.add(classes.Plant(name))
            print('New plant: "' + name + '" was created.\n')

        # view plants
        elif response == 2:
            print('Name: ' + cash.name)
            print('\nBalance:')
            print(cash.view_balance())

            print('\nTransactions:\n')
            tran = cash.view_transactions()
            for key in tran:
                print(str(key) + ': ' + str(tran[key]))

            if len(cash.transactions) == 0:
                print('<Empty>')
            print('\nInventory:')
            for plant in inventory.plants:
                print(plant)
            if len(inventory.plants) == 0:
                print('<Empty>')

        # water plants
        elif response == 3:
            which = functions.ask_int('Which plant would you like to water?')
            i = which - 1
            if i < len(inventory.plants):
                print(inventory.plants[i].water())
            else:
                print('No plant found.')

        # move to sun or back to inventory
        elif response == 4:
            try:
                move = functions.ask_int('Which plant would you like to move?') - 1
                plant = inventory.plants[move]
                if plant.isInSun == True:
                    where = 'out of'
                elif plant.isInSun == False:
                    where = 'to'
                inventory.move(plant)

                print('Successfully moved plant {} sunlight.'.format(where))
            except:
                print('Plant not found.')

        # Sell a plant
        elif response == 5:
            try:
                i = functions.ask_int('Which plant would you like to sell?') - 1
                plant = inventory.plants[i]
                price = plant.value
                plant.stop_timer()
                inventory.plants.remove(plant)

                cash.deposit(price)
                print('Successfully sold plant for:' + str(plant.value))
                print('New Balance:\n', str(cash.view_balance()))
            except:
                print('No plant found.')

        # deposit
        elif response == 6:
            amount = functions.ask_int('How much would you like to deposit?')
            cash.deposit(amount)
            print(
            'Success! Deposited: {}\n'.format(amount)
            + 'New Balance: '
            + str(cash.view_balance())
            )

        # withdrawal
        elif response == 7:
            amount = functions.ask_int('How much would you like to withdrawal?')
            if amount <= cash.view_balance():
                cash.withdrawal(amount)
                print(
                'Success! Withdrew: {}\n'.format(amount)
                + 'New Balance: '
                + str(cash.view_balance())
                )
            else:
                print('Insufficent Funds.')

        # quit
        elif response == 0:
            # stop timers to close app
            for plant in inventory.plants:
                plant.stop_timer()

        else:
            print('Please try again.')


if __name__ == '__main__':
    main()
