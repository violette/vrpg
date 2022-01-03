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
from random import randint

from Monster import Monster


class Player:
    """The player class"""

    def __init__(self, pname):
        self.name = pname
        self.state = 'normal'
        self.health = 10
        self.health_max = 10
        self.kills = 0
        self.monster = None
        self.exp = 0
        self.level = 1

    def status(self):
        print("%s's status: %s" % (self.name, self.state))
        print("%s's health status: %d/%d" % (self.name, self.health, self.health_max))
        print("%s has slaughtered: %d monsters" % (self.name, self.kills))
        print("%s has %d points of experience" % (self.name, self.exp))
        return ''

    def tired(self):
        self.health = max(1, self.health - 1)
        return "%s feels tired." % self.name

    def rest(self):
        if self.state != 'normal':
            print("%s can't rest now!" % self.name)
            return self.enemy_attacks()
        else:
            self.health = self.health_max
            return "%s rests." % self.name

    def flee(self):
        if self.state != 'fight':
            print("%s performs some shadow boxing. It's exhausting." % self.name)
            return self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.monster.health):
                self.state = 'normal'
                previous_monster_name = self.monster.name
                self.monster = None
                return "%s flees from %s." % (self.name, previous_monster_name)
            else:
                print("%s couldn't escape from %s!" % (self.name, self.monster.name))
                return self.enemy_attacks()

    def explore(self):
        if self.state != 'normal':
            return "%s is too busy right now!" % self.name
        else:
            self.monster = Monster.get_random_from_level(self.level)
            print("%s is surprised by a %s." % (self.name, self.monster.name))
            if self.monster.status == 'aggressive':
                self.state = 'fight'
            return Monster.get_monster_behavior_from_status(self.monster.status, self.monster.name, self.name)

    def attack(self):
        if self.state != 'fight':
            print("%s performs some shadow boxing. It's exhausting." % self.name)
            return self.tired()
        else:
            self.state = 'normal'
            self.kills += 1
            self.exp += self.monster.exp
            return Player.get_player_attack(self.level, self.monster.name, self.name)
            # TODO Manage player life + combat
            # if randint(0, self.health) < 10:
            #     self.health = self.health + 1
            #     self.health_max = self.health_max + 1
            #     return "%s feels stronger!" % self.name

    def enemy_attacks(self):
        if self.state == 'fight':
            self.health = max(1, self.health - 1)
            return "%s stabs %s!" % (self.name, self.monster.name)
        else:
            self.monster = None
            return "The monster goes away"

    @staticmethod
    def get_player_attack(level: int, monster_name: str, player_name: str):
        file = open('resources/player_behavior.json')
        behavior_dict = json.load(file)
        entry_list = list(behavior_dict["level" + str(level)])
        random_entry = random.choice(entry_list)
        random_entry = random_entry.replace("<player_name>", player_name).replace("<monster_name>", monster_name)
        return random_entry
