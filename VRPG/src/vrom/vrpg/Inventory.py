#
# Created:     2022
# Copyright:   (c) 2022 VROM
#
# Copyright 2022 VROM - Violette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
# -------------------------------------------------------------------------------


class Inventory:
    """The monster class"""

    def __init__(self, inventory: dict):
        self.inventory = inventory

    def remove_from_inventory(self, object_to_remove: str, number_of_items: int):
        initial = self.inventory.get(object_to_remove)
        if object_to_remove in self.inventory:
            total = initial - number_of_items
            if total < 0:
                print("Only %s %s available in the inventory" % (initial, object_to_remove))
            else:
                self.inventory.update({object_to_remove: total})
                print("%s %s was removed from the inventory" % (number_of_items, object_to_remove))
        return self.inventory

    def display(self):
        if not self.inventory:
            print("The inventory is empty")
        else:
            print(self.inventory)
        return ''

    def add_to_inventory(self, drop_items):
        if not drop_items:
            return self.inventory
        for key, value in drop_items.items():
            total = value
            if key in self.inventory:
                total += self.inventory.get(key)
            self.inventory.update({key: total})
            print("%s %s was added to the inventory" % (key, value))
        return self.inventory
