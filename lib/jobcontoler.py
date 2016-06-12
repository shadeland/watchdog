""" Works as a middleware or for the lack of any better explanation as a controller
    Controls the interaction between UrlWatch and APS
    Handles will use this class to get the most of the work done
    it is the only module that is connected to UW Job db
    """

class JobControler:
    """Work as a middleware between UI,UrlWatch, APS, DB ,User and everything t
    keep refrence to DB ,APS,
    it's better idea to store instance in application wide setrings so it would be
    accessible trough "setting" objects in handlres

    """
    def __init__(self,aps,db):
        # Todo soon : user management
        if aps:
            self.aps= aps
        else:
            raise
        pass
    pass

    #UrlWatch interface
    def uw_create_job(self):
        pass
    def uw_edit_job(self):
        pass
    def uw_delete_job(self):
        pass
    def uw_get_job(self):
        pass

    #APS interface
    def aps_create_job(self):
        pass
    def aps_update_job(self):
        pass
    def aps_delete_job(self):
        pass
    def aps_get_job(self):
        pass

    #User ,
    def usr_get_user(self):
        pass
    def usr_update_user(self):
        pass
    #API
    def api_response(self):
        pass
    def api_request(self):
        pass