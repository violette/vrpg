#
# Created:     2021
# Copyright:   (c) 2021 VROM
#
# Copyright 2021-2022 Violette
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

from src.vrom.vrpg.Inventory import Inventory


class test_inventory(unittest.TestCase):
    inventory = Inventory(dict())
    console_output = None

    def setUp(self):
        self.inventory = Inventory(dict())
        self.console_output = io.StringIO()

    def tearDown(self):
        self.console_output.flush()
        self.console_output.close()

    def test_should_display_inventory(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.display()
            output = self.console_output.getvalue().strip()
        expected_output = """The inventory is empty"""
        self.assertMultiLineEqual(output, expected_output)

    def test_should_add_item_to_inventory(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.add_to_inventory('gold', 3)
            output = self.console_output.getvalue().strip()
        expected_output = """3 gold was added to the inventory"""
        self.assertMultiLineEqual(output, expected_output)

    def test_should_display_multiple_line_inventory(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.add_to_inventory({'gold': 3})
            self.inventory.add_to_inventory({'gold': 2})
            output = self.console_output.getvalue().strip()
        expected_output = """3 gold was added to the inventory
2 gold was added to the inventory"""
        self.assertMultiLineEqual(output, expected_output)

    def test_should_display_add_then_inventory(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.add_to_inventory('gold', 3)
            self.inventory.add_to_inventory('gold', 2)
            self.inventory.display()
            output = self.console_output.getvalue().strip()
        expected_output = """3 gold was added to the inventory
2 gold was added to the inventory
{'gold': 5}"""
        self.assertMultiLineEqual(output, expected_output)

    def test_should_display_remove_then_inventory(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.add_to_inventory('gold', 3)
            self.inventory.remove_from_inventory('gold', 2)
            self.inventory.display()
            output = self.console_output.getvalue().strip()
        expected_output = """3 gold was added to the inventory
2 gold was removed from the inventory
{'gold': 1}"""
        self.assertMultiLineEqual(output, expected_output)

    def test_should_display_remove_more_than_possessed_should_fail(self):
        with contextlib.redirect_stdout(self.console_output):
            self.inventory.add_to_inventory('gold', 3)
            self.inventory.remove_from_inventory('gold', 5)
            self.inventory.display()
            output = self.console_output.getvalue().strip()
        expected_output = """3 gold was added to the inventory
Only 3 gold available in the inventory
{'gold': 3}"""
        self.assertMultiLineEqual(output, expected_output)


if __name__ == '__main__':
    unittest_main()
