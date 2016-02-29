# -*- coding:utf-8 -*-

from django.test import TestCase

from lottery.utils import reverse_integer, _calculate_wining_number


class TestUtils(TestCase):

    def test_reverse_integer(self):
        self.assertEqual(1234, reverse_integer(4321))
        self.assertEqual(1234, reverse_integer(432100))
        self.assertEqual(
            1234567890123456789012345678901234567890123456789,
            reverse_integer(9876543210987654321098765432109876543210987654321))

    def test_calculate_wining_number(self):
        sh_index = 2894.47
        sz_index = 9975.42
        number_count = 150000
        self.assertEqual(
            87883,
            _calculate_wining_number(sh_index=sh_index,
                                     sz_index=sz_index,
                                     number_count=number_count))
