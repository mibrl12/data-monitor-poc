import logging
from abc import abstractmethod, ABCMeta

from pymongo.database import Database

log = logging.getLogger(__file__)


class DataMonitor(metaclass=ABCMeta):

    def __init__(self, db: Database):
        self._db = db

    @abstractmethod
    def start(self):
        pass


class PriceDataMonitor(DataMonitor):

    collection_name = 'prices'

    def __init__(self, db: Database):
        super().__init__(db=db)
        self._collection = db[self.collection_name]
        self.offset = 0

    def start(self):
        prices = self._collection.find().skip(self.offset)
        for price in prices:
            self.detect_outlier(price)
        self.offset = self._collection.count()

    def detect_outlier(self, price):
        # check if out of normal values
        # expose metric (e.g. counter outliers)
        print(price)

    def detect_late_arrival(self, price):
        # check older than allowed
        # expose metric (e.g. counter late arrivals)
        print(price)
