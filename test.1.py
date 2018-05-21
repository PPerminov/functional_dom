import unittest
import __init__ as p1


class TestPairs(unittest.TestCase):
    def test_pairs(self):
        car1 = 5465123
        cdr1 = 5623
        car2 = 'yt676789'
        cdr2 = 'iu8y7t6r576t8y9u9ipko'
        pair1 = p1.cons(car1, cdr1)
        pair2 = p1.cons(car2, cdr2)
        self.assertNotEqual(pair1, pair2)
        self.assertEqual(p1.car(pair1), car1)
        self.assertEqual(p1.cdr(pair2), cdr2)

    def test_params(self):
        key = 898767890
        wrong_key = 'i78657890uoih'
        value = 9876890
        params_pair = p1.parameter(key, value)
        self.assertTrue(key == p1.get_key(params_pair))
        self.assertFalse(p1.get_value_by_key(params_pair, wrong_key))
        self.assertFalse(p1.parameter('', value))
        self.assertEqual(p1.get_value_by_key(params_pair, key), value)

    def test_list(self):
        pa1 = 'juhy7g6fgyhun'
        pa2 = '8976898yughijhko87uh'
        pa3 = '7987908'
        pa4 = '7987908'
        list1 = p1.special_list(pa1, pa2, pa3, pa4)
        self.assertEqual(p1.head(list1), pa1)
        self.assertEqual(p1.head(p1.tail(list1)),
                         p1.head(p1.special_list(pa2, pa3, pa4)))
        self.assertEqual(p1.head(p1.tail(list1)), pa2)

    def test_lists_equality(self):
        list1 = p1.special_list(1, 2, 3)
        list2 = p1.special_list(1, 2, 34)
        list3 = p1.special_list(1, 2, 3)
        tree_list1 = p1.special_list(1, 2, list1, 34)
        tree_list2 = p1.special_list(1, 2, list3, 34)
        self.assertTrue(p1.is_equal_lists(list1, list1))
        self.assertTrue(p1.is_equal_lists(tree_list1, tree_list2))
        self.assertFalse(p1.is_equal_lists(list1, list2))

    def test_quads(self):
        pa1 = 'juhy7g6fgyhun'
        pa2 = '8976898yughijhko87uh'
        pa3 = '7987908'
        pa4 = '7987908'
        pa5 = 'juhy7g6fgyhun'
        pa6 = '8976898yughijhko87uh'
        pa7 = '7987908'
        pa8 = '7987908'
        quad1 = p1.quad(pa1, pa2, pa3, pa4)
        self.assertEqual(p1.third(quad1), pa3)
        self.assertNotEqual(p1.first(quad1), pa4)

    # def test_unit()

    def test_create_parameters_list(self):
        key1 = 898767890
        key2 = 'i78657890uoih'
        value1 = 9876890
        value2 = '9876890'
        param1 = p1.parameter(key1, value1)
        param2 = p1.parameter(key2, value2)
        params_1 = p1.create_parameters_list(param1, param2, param1, param1)
        print(p1.head(p1.car(params_1)))
        self.assertEqual(
            p1.get_key(
                p1.head(
                    p1.tail(
                        params_1
                    )
                )
            ), key2)


if __name__ == '__main__':
    unittest.main()
