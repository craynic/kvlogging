import logging

ALL = ['Logger']


class SafeDict(dict):
    def __getitem__(self, key):
        try:
            return super(SafeDict, self).__getitem__(key)
        except KeyError:
            return ''


class Logger(logging.Logger):
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)
        self._context = dict()

    def bind(self, **kwargs):
        self._context.update(kwargs)

    def unbind(self, *args):
        for arg in args:
            self._context.pop(arg, None)

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False, **kwargs):
        load = SafeDict(self._context)
        load.update(kwargs)
        if args:
            load['_args'] = args
        # Empty dict will make Record do nothing to args, and cause a call
        # to function format with a tuple containing a empty dict.
        if not load:
            load = tuple()
        # Data in load will be used to generate log message with msg.
        super(Logger, self)._log(
            level, msg, load, exc_info=exc_info, extra=extra, stack_info=stack_info)
