class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json'
        }
