import unittest

from main import get_test_data, get_one_to_many, get_many_to_many, task_g1, task_g2, task_g3

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.streets, self.houses, self.hou_str = get_test_data()
        self.one_to_many = get_one_to_many(self.houses, self.streets)
        self.many_to_many = get_many_to_many(self.houses, self.streets, self.hou_str)
    def test_task_g1(self):
        result=task_g1(self.houses,self.streets)
        expected = {
            'Английский бульвар': [(111, 9000)],
            'Амурская улица': [(123, 4500), (125, 3300)],
            'Абрикосовая улица': [(635, 1200)],
        }
        self.assertEqual(result, expected)

    def test_task_g2(self):
        result = task_g2(self.one_to_many)
        expected = [('Английский бульвар', 9000),
                    ('Железнодорожная улица', 6300),
                    ('Амурская улица', 4500),
                    ('Абрикосовая улица', 1200)]
        self.assertEqual(result, expected)

    def test_task_g3(self):
        result = task_g3(self.many_to_many)
        expected= [(635, 1200, 'Абрикосовая улица'),
                   (123, 4500, 'Амурская улица'),
                   (125, 3300, 'Амурская улица'),
                   (111, 9000, 'Английский бульвар'),
                   (325, 6300, 'Железнодорожная улица'),
                   (265, 4400, 'Железнодорожная улица'),
                   (123, 4500, 'Острякова'),
                   (111, 9000, 'Приморская улица')]
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()