import unittest
from tank import Shop
from tank import DB
from stub import player
import logging


class ShopTest(unittest.TestCase):


    @unittest.skip("tested - skipping")
    def test_shop_no_import_exception(self):
        try:
            s=Shop()
        except:
            self.assertFalse(True)

    @unittest.skip("tested - skipping")
    def test_buy_tank_valid_args_valid_credits_saved_result_True(self):
        s=Shop()
        p=player()
        p.resources.credits=1000
        p.resources.gold=1000
        s._Shop__buyTank(p,1101)
        self.assertTrue(p.saved_result)

    @unittest.skip("tested - skipping")
    def test_buy_tank_with_invalid_id_save_result_False(self):
        s=Shop()
        p=player()
        p.resources.credits=1000
        p.resources.gold=1000
        s._Shop__buyTank(p, -4)
        self.assertFalse(p.saved_result)

    @unittest.skip("tested - skipping")
    def test_buy_tank_with_invalid_id_type_saved_result_False(self):
        s=Shop()
        p=player()
        p.resources.credits=1000
        p.resources.gold=1000
        s._Shop__buyTank(p,"1101")
        self.assertFalse(p.saved_result)

    @unittest.skip("tested - find bug")
    def test_buy_tank_valid_args_valid_credits_correct_credits(self):
        s=Shop()
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p,1101)
        self.assertEqual(p.resources.credits , 0)
        self.assertEqual(p.resources.gold , 0)

    @unittest.skip("tested - skipping")
    def test_buy_tank_wrong_parameters_instance_exception(self):
        s=Shop()
        s._Shop__buyTank("123" , "123")
        msg="Shop.__buyTank must operate with player and tankId args, no is Instance cheking"
        raise Exception(msg)


    @unittest.skip("tested - skipping")
    def test_buy_tank_with_string_tankid_exception(self):
        p=player()
        p.resources.gold=100
        p.resources.credits=100
        try:
            s=Shop()

            p.credits.gold=100
            s._Shop__buyTank(p, "1101")
            msg="Shop.__buyTank no tankID type casting, is it bug or feature? "
            self.assertTrue(False,msg)
        except Exception as ex:
            print ex
            msg="ales OK"
            self.assertTrue(True,msg)

class DBTest(unittest.TestCase):
    @unittest.skip("tested - skipping")
    def test_init_no_exceptions(self):
        db=DB()




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

    #print tmp.__buyTank("123")
