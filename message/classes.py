from rest_framework.response import Response


class Context(object):
    def __init__(self, chat_id, original, checked=''):
        self.chat_id = chat_id
        self.original = original
        self.checked = checked


class ResponseThen(Response):
    def __init__(self, data, then_callback, **kwargs):
        super().__init__(data, **kwargs)
        self.then_callback = then_callback

    def close(self):
        super().close()
        self.then_callback()
