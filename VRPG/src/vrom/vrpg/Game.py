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

import sys


class Game:
    def __init__(self, player):
        self.player = player
        self.commands = {
            'quit': self.quit,
            'help': self.display_help,
            'status': self.player.status,
            'rest': self.player.rest,
            'explore': self.player.explore,
            'flee': self.player.flee,
            'attack': self.player.attack
        }

    def display_help(self):
        return list(self.commands.keys())

    @staticmethod
    def quit():
        print("Exit current game")
        sys.exit()

    def run(self):
        while self.player.health > 0:
            if self.player.state == "fight":
                line = input("⚔⚔⚔>")
            else:
                line = input(" >> ")
            args = line.split()
            if len(args) > 0:
                command_found = False
                for input_command in self.commands.keys():
                    # print("Commands %s " % self.commands.keys())
                    if args[0] == input_command[:len(args[0])]:
                        print(self.commands[input_command]())
                        command_found = True
                        break
                if not command_found:
                    print("%s does not understand the request, try again" % self.player.name)
