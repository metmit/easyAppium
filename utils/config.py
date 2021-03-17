from cfg.session import desired_capabilities
from cfg.processor import processors
from cfg.producer import producers
from core.producer import Producer
from core.processor import Processor


class Config(object):

    def __init__(self):
        pass

    @staticmethod
    def get_session(key=None):
        configs = desired_capabilities
        if key is None or key not in configs:
            return configs

        return configs[key]

    @staticmethod
    def get_processor(app_name) -> Processor.__class__:
        if app_name not in processors:
            raise Exception("获取{} Processor失败...".format(app_name))
        return processors[app_name]

    @staticmethod
    def get_producer(app_name) -> Producer.__class__:
        if app_name not in producers:
            raise Exception("获取{} Producer失败...".format(app_name))
        return producers[app_name]