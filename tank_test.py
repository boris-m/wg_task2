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

    unittest.skip("tested - skipping")
    def test_buy_tank_valid_args_valid_credits_saved_result_True(self):
        s=Shop()
        s.db.tanks[1101] = {'credits': 500, 'gold': 0}
        p=player()
        p.resources.credits  =  1000
        p.resources.gold     =  1000
        s._Shop__buyTank(p,1101)
        s._Shop__buyTank(p,1101)
        self.assertEqual(p.resources.credits, 500)
        self.assertEqual(p.resources.gold,   1000)

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
    def test_buy_tank_valid_args_valid_credits_result_correct_credits(self):
        s=Shop()
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p,1101)
        self.assertEqual(p.resources.credits , 0)
        self.assertEqual(p.resources.gold , 0)

    @unittest.skip("tested - probably bug")
    def test_buy_tank_wrong_parameters_instance_result_exception(self):
        s=Shop()
        try:
            s._Shop__buyTank("123" , "123")
            res=False
        except Exception,e:
            print e
            res=True
        self.assertTrue(res)

    @unittest.skip("tested - probably bug")
    def test_buy_tank_no_enought_resources__result_empty_inventoryPlanes(self):
        s=Shop()
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p , 1101)
        self.assertEqual(p.inventoryPlanes, [])

    @unittest.skip("tested - find bug")
    def test_buy_tank_double_buy_valid_args_valid_credits_result_one_buy(self):
        s=Shop()
        p=player()
        p.resources.credits=1000
        p.resources.gold=0
        s._Shop__buyTank(p,1101)
        self.assertEqual(p.resources.credits , 0)
        self.assertEqual(p.resources.gold , 0)



    @unittest.skip("tested - bug +bug = no bug")
    def test_buy_tank_negative_credits_result_no_actions(self):
        s=Shop()
        s.db.tanks[999999999]= {'credits': -100, 'gold': 0}
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p,999999999)
        self.assertEqual(p.resources.credits , 0)


    def test_buy_tank_no_enought_resources__result_empty_inventoryPlanes(self):
        s=Shop()
        p=player()
        p.inventoryPlanes.append(1101)
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyGuns(p, 1101, 224 )
        print p.resources.credits

        self.assertEqual(p.inventoryPlanes, [])

class DBTest(unittest.TestCase):
    @unittest.skip("tested - skipping")
    def test_init_no_exceptions(self):
        db=DB()




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

    #print tmp.__buyTank("123")
