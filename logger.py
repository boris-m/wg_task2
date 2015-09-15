import logging

class fin_logger(object):
    def log_state(self,param):
        print "log state with {par} parameters".format(par = param)
        logging.debug("loga state log {msg}".format(msg = param))

