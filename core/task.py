class Task(object):

    def __init__(self, action: str, params: dict):
        self.__action = action
        self.__params = params

    def get_action(self) -> str:
        return self.__action

    def get_params(self, key: str = None) -> dict:
        if key is None:
            return self.__params
        return self.__params[key] if key in self.__params else None

    def has_params(self, key: str) -> bool:
        params = self.get_params()
        if params is not None and key in params:
            return True
        return False

    def __str__(self):
        return "action: {}, params: {}".format(self.__action, self.__params)
