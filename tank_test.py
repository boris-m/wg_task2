import unittest
from tank import Shop
from tank import DB
from stub import player
import logging

def db_test_fill(shop):
    shop.db.tanks[500] = {'credits': 500, 'gold': 0}
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

    #@unittest.skip("tested - skipping")
    def test_shop_no_import_exception(self):
        try:
            s=Shop()
        except Exception as e:
            self.assertFalse(True,msg="we get exception while creating instance of shop class:{ex} ".format(ex = e))

    def test_buy_tank_valid_args_valid_credits_check_adding_tank_to_player(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits  =  1000000
        p.resources.gold     =  1000000
        s._Shop__buyTank(p,5555)
        self.assertEqual(player.inventoryPlanes, [5555], msg="we hope to see buyed tank in player inventoryPlanes list")


    #@unittest.skip("tested - skipping")
    def test_buy_tank_valid_args_valid_credits_check_charge_value(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits  =  1000000
        p.resources.gold     =  1000000
        s._Shop__buyTank(p,5555)
        self.assertEqual(p.resources.credits, 1000000, msg="error charging credits while buying tank 5555")
        self.assertEqual(p.resources.gold,    1000000, msg="error charging gold while buying tank 5555")
        s._Shop__buyTank(p,0000)
        self.assertEqual(p.resources.credits, 1000000, msg="error charging credits while buying tank 0000")
        self.assertEqual(p.resources.gold,    1000000, msg="error charging gold while buying tank 0000")
        s._Shop__buyTank(p,6666)
        self.assertEqual(p.resources.credits, 1000000-6666, msg="error charging credits while buying tank 6666")
        self.assertEqual(p.resources.gold,    1000000-6666, msg="error charging gold while buying tank 6666")


    def test_buy_tank_valid_args_valid_credits_check_double_charge(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits  =  1000
        p.resources.gold     =  1000
        s._Shop__buyTank(p,500)
        self.assertEqual(p.resources.credits, 500, msg= " error charging credits while first buying tank")
        s._Shop__buyTank(p,500)
        self.assertEqual(p.resources.credits, 500, msg= " error charging credits while second buying tank")



    #@unittest.skip("tested - skipping")
    def test_buy_tank_with_invalid_id_save_result_False(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits=1000
        p.resources.gold=1000
        s._Shop__buyTank(p, -4)
        self.assertFalse(p.saved_result, msg = "wrong tankID  - we waiting NO player.saveResources run")

    #@unittest.skip("tested - skipping")
    def test_buy_tank_with_invalid_id_type_saved_result_False(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits=1000
        p.resources.gold=1000
        s._Shop__buyTank(p,"1101")
        self.assertFalse(p.saved_result, msg = "wrong tankID type - we waiting NO player.saveResources run")

    #@unittest.skip("tested - find bug")
    def test_buy_tank_valid_args_valid_credits_result_correct_credits(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p,9999)
        self.assertEqual(p.resources.credits , 0, msg="wrong credits charge, while player have no credits")
        self.assertEqual(p.resources.gold , 0, msg="wrong gold charge, while player have no gold")

    #@unittest.skip("tested - probably bug")
    def test_buy_tank_wrong_parameters_instance_result_exception(self):
        s=Shop()
        db_test_fill(s)
        try:
            s._Shop__buyTank("123" , "123")
            res=False
        except Exception,e:
            print e
            res=True
        self.assertTrue(res,msg="no args type validator")

    #@unittest.skip("tested - probably bug")
    def test_buy_tank_no_enought_resources__result_empty_inventoryPlanes(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p , 9999)
        self.assertEqual(p.inventoryPlanes, [], msg="if player have no enough resources he can not buy tank ")

    #@unittest.skip("tested - find bug")
    def test_buy_tank_double_buy_valid_args_valid_credits_result_one_buy(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.resources.credits=1000
        p.resources.gold=0
        s._Shop__buyTank(p,500)
        s._Shop__buyTank(p,500)
        self.assertEqual(p.inventoryPlanes , [500], msg="we waiting one tank")




    #@unittest.skip("tested - bug +bug = no bug")
    def test_buy_tank_negative_credits_result_no_actions(self):
        s=Shop()
        db_test_fill(s)
        s.db.tanks[999999999]= {'credits': -100, 'gold': 0}
        p=player()
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyTank(p,999999999)
        self.assertEqual(p.resources.credits , 0, msg="user buy tank and get prize?")


    #@unittest.skip("tested - bug")
    def test_buy_gun_no_enought_resources__result_empty_inventoryPlanes(self):
        s=Shop()
        db_test_fill(s)
        p=player()
        p.inventoryPlanes.append(9999)
        p.inventoryGuns[9999]=[]#TODO REMOVE it after bug fix
        p.resources.credits=0
        p.resources.gold=0
        s._Shop__buyGuns(p, 9999, 999 )
        print "credits - ",p.resources.credits
        self.assertEqual(p.inventoryGuns[9999],[],msg="we suupose user can not buy guns without resources")
    #@unittest.skip("stopped by bug")
    def test_buy_gun_result_correct_charge(self):
        tid=9999
        s=Shop()
        db_test_fill(s)
        p=player()
        p.inventoryPlanes.append(tid)
        p.inventoryGuns[tid]=[] #TODO REMOVE it after bug fix
        p.resources.credits=999
        p.resources.gold=0
        s._Shop__buyGuns(p, tid, 999 )
        self.assertEqual(p.resources.credits, 0,msg="error charging player")
    #@unittest.skip("stopped by bug")
    def test_buy_several_different_guns_result_several_guns_added(self):
        tid=9999
        s=Shop()
        db_test_fill(s)
        p=player()
        p.inventoryPlanes.append(tid)
        p.inventoryGuns[tid]=[] #TODO REMOVE it after bug fix
        p.resources.credits=999
        p.resources.gold=999
        s._Shop__buyGuns(p, tid, 999 )
        self.assertEqual(p.resources.credits, 0,msg="error charging player")
        s._Shop__buyGuns(p, tid, 998 )
        self.assertEqual(p.resources.gold, 1,msg="error charging player")
        self.assertEqual(p.inventoryGuns, {9999: [999, 998]},msg="error adding guns to player")
    #@unittest.skip("stopped by bug")
    def test_buy_several_same_guns_result_several_guns_added(self):
        tid=9999
        s=Shop()
        db_test_fill(s)
        p=player()
        p.inventoryPlanes.append(tid)
        p.inventoryGuns[tid]=[] #TODO REMOVE it after bug fix
        p.resources.credits=1998
        p.resources.gold=999
        s._Shop__buyGuns(p, tid, 999 )
        self.assertEqual(p.resources.credits, 999, msg="error charging player")
        s._Shop__buyGuns(p, tid, 999 )
        self.assertEqual(p.resources.credits, 0, msg="error charging player")
        self.assertEqual(p.resources.gold, 999 ,msg="error charging player")
        self.assertEqual(p.inventoryGuns, {9999: [999, 999]} ,msg="error adding guns to player.inventoryGuns")


if __name__ == "__main__":
    unittest.main()

