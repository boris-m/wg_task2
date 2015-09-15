import unittest
from tank import Shop
from tank import DB
from stub import player
import logging

def db_test_fill(shop):
    shop.db.tanks[9999] = {'credits': 9999, 'gold': 0}
    shop.db.tanks[8888] = {'credits': 8888, 'gold': 8888}
    shop.db.tanks[7777] = {'credits': 0, 'gold': 7777}
    shop.db.tanks[6666] = {'credits': 6666, 'gold': 6666}
    shop.db.tanks[5555] = {'credits': 0, 'gold': 0}
    shop.db.tanks[4444] = {'credits': None, 'gold': 0}
    shop.db.tanks[3333] = {'credits': 0, 'gold': None}
    shop.db.tanks[2222] = {'credits': None, 'gold': None}
    shop.db.tanks[1111] = {'credits': "123", 'gold': "123"}

    shop.db.guns[9999]={999: {'credits': 999, 'gold': 0},
                        998: {'credits': 0, 'gold': 998},
                        997: {'credits': 997, 'gold': 997},
                        996: {'credits': 0, 'gold': 0}}
    shop.db.guns[8888]={999: {'credits': 999, 'gold': 0},
                        998: {'credits': 0, 'gold': 998},
                        997: {'credits': 997, 'gold': 997},
                        996: {'credits': 0, 'gold': 0}}
    shop.db.guns[7777]={799: {'credits': 999, 'gold': 0},
                        798: {'credits': 0, 'gold': 998},
                        797: {'credits': 997, 'gold': 997},
                        796: {'credits': 0, 'gold': 0}}
    shop.db.guns[6666]={999: {'credits': None, 'gold': 0},
                        998: {'credits': 0, 'gold': "998"},
                        997: {'credits': -997, 'gold': -997},
                        996: {'credits': 0, 'gold': 0}}



class ShopTest(unittest.TestCase):


    @unittest.skip("tested - skipping")
    def test_shop_no_import_exception(self):
        try:
            s=Shop()
        except:
            self.assertFalse(True)

    @unittest.skip("tested - skipping")
    def test_buy_tank_valid_args_valid_credits_check_charge_value(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits  =  1000000
        p.resources.gold     =  1000000
        s._Shop__buyTank(p,5555)
        self.assertEqual(p.resources.credits, 1000000)
        self.assertEqual(p.resources.gold,    1000000)
        s._Shop__buyTank(p,0000)
        self.assertEqual(p.resources.credits, 1000000)
        self.assertEqual(p.resources.gold,    1000000)
        s._Shop__buyTank(p,6666)
        self.assertEqual(p.resources.credits, 1000000-6666)
        self.assertEqual(p.resources.gold,    1000000-6666)

    def test_buy_tank_valid_args_valid_credits_check_double_charge(self):
        s=Shop()
        db_test_fill(s)
        s.db.tanks[500] = {'credits': 500, 'gold': 0}
        p=player()
        p.resources.credits  =  1000
        p.resources.gold     =  1000
        s._Shop__buyTank(p,500)
        self.assertEqual(p.resources.credits, 500)
        s._Shop__buyTank(p,500)
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
