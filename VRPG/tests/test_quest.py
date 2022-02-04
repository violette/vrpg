#
# Created:     2022
# Copyright:   (c) 2022 VROM
#
# Copyright 2022 Violette
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

from src.vrom.vrpg.Quest import Quest


class test_quest(unittest.TestCase):
    quest = None
    console_output = None

    def setUp(self):
        self.quest = Quest("quest_name", 1, 2, "This is a description", {"gold": 2, "wood": 1},
                           {"stem": 4, "silver": 4})
        self.console_output = io.StringIO()

    def tearDown(self):
        self.console_output.close()

    def test_should_display_description(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.description
        expected_output = "This is a description"
        self.assertEquals(output, expected_output)

    def test_should_display_name(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.name
        expected_output = "quest_name"
        self.assertEquals(output, expected_output)

    def test_should_display_level(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.level
        expected_output = 2
        self.assertEquals(output, expected_output)

    def test_should_display_numero(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.numero
        expected_output = 1
        self.assertEquals(output, expected_output)

    def test_should_display_required_items(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.required_quest_items
        expected_output = {'gold': 2, 'wood': 1}
        self.assertEquals(output, expected_output)

    def test_should_display_reward_items(self):
        with contextlib.redirect_stdout(self.console_output):
            output = self.quest.reward_items
        expected_output = {'stem': 4, 'silver': 4}
        self.assertEquals(output, expected_output)


if __name__ == '__main__':
    unittest_main()
