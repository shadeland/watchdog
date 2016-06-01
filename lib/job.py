class Job:
    def __init__(self, **kargs):
        self.id = kargs['id']
        self.usrId = kargs['usrID']
        self.url = kargs['url']
        self.createDate = kargs['createDate']
        self.repeat = kargs['repeat']

    def get_asp(self):
        pass




