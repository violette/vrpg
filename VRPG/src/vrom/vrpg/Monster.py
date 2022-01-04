#
# Created:     2021
# Copyright:   (c) 2021 VROM
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
import random


class Monster:
    """The monster class"""

    def __init__(self, name: str, attack: int, drop_items: dict, exp: int, level: int, life_points: int, status: str):
        self.name = name
        self.attack = attack
        self.drop_items = drop_items
        self.exp = exp
        self.level = level
        self.life_points = life_points
        self.status = status

    @staticmethod
    def get_random_from_level(level=1):
        file = open('resources/monsters.json')
        monsters_dict = json.load(file)
        entry_list = list(monsters_dict["level" + str(level)])
        random_entry = random.choice(entry_list)
        # TODO enable logging - debug
        print(random_entry)
        return Monster(random_entry["name"],
                       int(random_entry["attack"]),
                       random_entry["drop_items"],
                       int(random_entry["exp"]),
                       level,
                       int(random_entry["lp"]),
                       random_entry["status"])

    @staticmethod
    def get_monster_behavior_from_status(status: str, monster_name: str, player_name: str):
        file = open('resources/monsters_behavior.json')
        behavior_dict = json.load(file)
        entry_list = list(behavior_dict[status])
        random_entry = random.choice(entry_list)
        random_entry = random_entry.replace("<player_name>", player_name).replace("<monster_name>", monster_name)
        return random_entry
