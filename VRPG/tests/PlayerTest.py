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
import contextlib
import io
import unittest.mock
from unittest import main as unittest_main

from src.vrom.vrpg.Player import Player


class PlayerTestCase(unittest.TestCase):
    player = None
    console_output = None

    @classmethod
    def setUpClass(cls):
        cls.player = Player("Sam Carter")
        cls.console_output = io.StringIO()

    def test_should_display_player_status(self):
        with contextlib.redirect_stdout(self.console_output):
            self.player.status()
            output = self.console_output.getvalue().strip()
        expected_output = """Sam Carter\'s status: normal
Sam Carter\'s health status: 10/10
Sam Carter has slaughtered: 0 monsters
Sam Carter has 0 points of experience"""
        self.assertMultiLineEqual(output, expected_output)
        self.console_output.close()

    def test_should_display_player_tired(self):
        with contextlib.redirect_stdout(self.console_output):
            self.player.tired()
            output = self.console_output.getvalue().strip()
        expected_output = """Boo"""
        self.assertMultiLineEqual(output, expected_output)
        self.console_output.close()


if __name__ == '__main__':
    unittest_main()
