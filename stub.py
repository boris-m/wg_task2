class Resources(object):
    def __init__(self):
        self.credits = None
        self.gold    = None


class player(object):
    def __init__(self):
        self.resources       = Resources()
        self.inventoryPlanes = []
        self.inventoryGuns   = {}
        self.saved_result    = False

    def saveResources(self):
        print "resources saved"
        self.saved_result=True






