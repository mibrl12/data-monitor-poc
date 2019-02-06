import datetime
import dateutil.parser
import logging
from abc import abstractmethod, ABCMeta
from pymongo.database import Database

from models.monitored_actuals import MonitoredActuals

log = logging.getLogger(__file__)


class DataMonitor(metaclass=ABCMeta):

    def __init__(self, db: Database):
        self._db = db

    @abstractmethod
    def start(self):
        pass


class PriceDataMonitor(DataMonitor):
    collection_name = MonitoredActuals.PRICE.name.lower()

    def __init__(self, db: Database):
        super().__init__(db=db)
        self._collection = db[self.collection_name]
        self._offset = 0
        self._allowed_lateness = datetime.timedelta(seconds=60)
        self._threshold = 100

    def start(self):
        prices = self._collection.find().skip(self._offset)
        for price in prices:
            self.detect_outlier(price)
            self.detect_late_arrival(price)
        self._offset = self._collection.count()

    def detect_outlier(self, price):
        if price['value'] > self._threshold:
            print(f'Outlier: {price}')
            # expose metric (e.g. counter outliers)

    def detect_late_arrival(self, price):
        event_time = dateutil.parser.parse(price['timestamp'])
        processed_time = dateutil.parser.parse(price['processed_timestamp'])

        if (processed_time - event_time) > self._allowed_lateness:
            print(f'Too late: {price}')
            # expose metric (e.g. counter late arrivals)

