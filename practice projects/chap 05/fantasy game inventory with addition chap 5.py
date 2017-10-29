#!/usr/bin/env python3
'''
Imagine that a vanquished dragon’s loot is represented as a list of
strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where
the inventory parameter is a dictionary representing the player’s
inventory (like in the previous project) and the addedItems parameter
is a list like dragonLoot. The addToInventory() function should return
a dictionary that represents the updated inventory. Note that the
addedItems list can contain multiples of the same item.
'''


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(inventory.get(k, 0), k)
        item_total = item_total + inventory.get(k, 0)
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

