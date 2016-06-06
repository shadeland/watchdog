import logging

import motor
from apscheduler.schedulers.tornado import TornadoScheduler

class Job:
    def __init__(self, **kargs):
        self.id = kargs['id']
        self.usrId = kargs['usrID']
        self.url = kargs['url']
        self.createDate = kargs['createDate']
        self.repeat = kargs['repeat']

    def get_asp(self):
        pass



class JobCreator:
    """A singlethon that creates jobs and add them to data stores"""
    # xTODO aps and db_client should get init in the constructor so that we can have one global JobCreator object in application
    def __init__(self,aps: TornadoScheduler = None, db_client: motor.MotorClient =None):
        self.aps = aps
        self.db_client = db_client


    def create_job(self, url=None, usr_id=None):
        """
        create job
        :param url: url of thre page to be watched
        :param usr_id: userid of job owner, if None raise an error
        :param aps: points to global aps
        :param db_client: points to global db_client
        :return: if succeeds returns
        """
        self._add_job_uw(self.db_client, url = url, usr_id=usr_id)
        # self._add_job_aps(aps,wu_id)

    def _add_job_aps(self,uw_job_id):
        """
        :param aps:
        :param uw_job_id:
        :return:
        """
        logging.debug("add job aps started with %s", uw_job_id)
        newjob = self.aps.add_job(func=print, args=["executing job {0}".format(uw_job_id)], trigger='interval', seconds=3)
        self.update_job_uw(uw_job_id, aps_job_id = newjob.id)
        logging.debug("add job aps ending")

    def _add_job_uw(self, db_client, **kargs):
        logging.debug("add job uw starting")

        def my_callback (result, e):
            if e:
                raise e
            self._add_job_aps(result)
        db_client.jobs_database.jobs.insert({'url': kargs['url'],
                                            'usr_id': kargs['usr_id']}, callback= my_callback)
        logging.debug("add job uw ended")

    def update_job_uw(self, uw_job_id, **kwargs):
        logging.debug("updating {0} with {1}".format(uw_job_id, kwargs))
        self.db_client.jobs_database.jobs.update({'_id': uw_job_id}, {'aps_job_id': kwargs['aps_job_id']})



