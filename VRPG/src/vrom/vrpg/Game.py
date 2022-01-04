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

from src.vrom.vrpg.Display import Display
display = Display.display

class Game:
    def __init__(self, player):
        self.player = player
        self.commands = {
            'attack': self.player.attack,
            'explore': self._explore,
            'flee': self._flee,
            'help': self.display_help,
            'inventory': self.player.inventory.display,
            'quit': self.quit,
            'rest': self._rest,
            'status': self.player.status
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

    def _explore(self):
        display(self.player.explore())
        return ""

    def _flee(self):
        display(self.player.flee())
        return ""

    def _rest(self):
        display(self.player.rest())
        return ""


