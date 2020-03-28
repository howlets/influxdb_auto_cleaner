from logger.logging import service_logger
from influxdb import InfluxDBClient
from urllib.parse import urlparse
import traceback
import auto_cleaner.settings as settings
import time
import json

log = service_logger()


def _influx_client():
    influx_host = urlparse(settings.INFLUXDB_URL).hostname
    influx_port = urlparse(settings.INFLUXDB_URL).port

    client = InfluxDBClient(influx_host, influx_port, settings.INFLUXDB_USER, settings.INFLUXDB_PASS)

    return client


def clean_fields():
    print(settings.RP_CONFIG)
