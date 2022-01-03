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
from Game import Game
from Player import Player

if __name__ == "__main__":
    # TODO Remove comment - actually for debugging
    # name = input("> What is your name? ")
    name = "(Player Name)"
    print("> 'help' to get a list of actions\n")
    player = Player(name)
    game = Game(player)
    print("> %s is starting is new adventure. (S)He took some food and started to get out of the town" % name)
    game.run()
