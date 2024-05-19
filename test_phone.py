import unittest
import phone_checker

list_phone_uncor = [
    "",
    "+79313698787",
    "89313546654",
    "+7-898-985-98-98"
]

list_phone_cor = [
        "8-931-325-43-45"
    ]


class Test_test_phone(unittest.TestCase):
    def test_F_phone(self):
        for phone in list_phone_uncor:
            self.assertFalse(phone_checker.phone_checker(phone))
    def test_T_phone(self):
        for phone in list_phone_cor:
            self.assertTrue(phone_checker.phone_checker(phone))

if __name__ == '__main__':
    unittest.main()
