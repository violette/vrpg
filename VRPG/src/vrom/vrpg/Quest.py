#
# Created:     2022
# Copyright:   (c) 2022 VROM
#
# Copyright 2021 Violette
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
import json


# The quest class. There is only one level per class.
# The quest can be achieved anywhere.
class Quest:
    """The monster class"""

    def __init__(self, name: str, numero: int, level: int, description: str, required_quest_items: dict,
                 reward_items: dict):
        self.name = name
        self.numero = numero
        self.level = level
        self.description = description
        self.required_quest_items = required_quest_items
        self.reward_items = reward_items

    # For now there is only one quest per level
    @staticmethod
    def get_quest_from_level(level=1):
        file = open('resources/quests.json')
        monsters_dict = json.load(file)
        quests_list_per_level = list(monsters_dict["level" + str(level)])
        # TODO enable logging - debug
        print(quests_list_per_level)
        entry = quests_list_per_level[0]
        return Quest(entry["name"],
                     int(entry["numero"]),
                     int(entry["level"]),
                     entry["description"],
                     entry["required_items"],
                     entry["reward_items"])

    def display(self):
        print("HERE")
        return ''
