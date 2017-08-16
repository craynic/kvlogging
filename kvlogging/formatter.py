import logging
import json


class JsonFormatter(logging.Formatter):
    extra_fields = ['created', 'levelname']

    def format(self, record):
        message = super(JsonFormatter, self).format(record)
        data = dict(record.args)
        data['message'] = message
        for field in self.extra_fields:
            data[field] = getattr(record, field)
        formatted = json.dumps(data)
        return formatted


class StreamFormatter(logging.Formatter):
    key_width = 10

    def kv_format(self, kv):
        k, v = kv
        return '\n> {k:{kw}}: {v}'.format(k=k, v=v, kw=self.key_width)

    def make_kv_str(self, data):
        return ''.join(map(
            self.kv_format,
            data.items()
        ))

    def format(self, record):
        data = dict(record.args)
        record.kvdata = self.make_kv_str(data)
        message = super(StreamFormatter, self).format(record)
        return message
