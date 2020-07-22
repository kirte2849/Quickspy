import json
import time

from quickspy.util import get_uuid


class JsonMsgManager:
    def __init__(self, fromname):
        self.fromname =  fromname

    def jsmsg(self, toname, msg):
        ajsmsg = {
            'header': {
                'uuid': get_uuid(),
                'time': time.time(),
                'fromname': self.fromname,
                'toname': toname,
                # from ip,from session
            },

            'body': {
                'msg': msg
            },

        }
        return json.dumps(ajsmsg)

def jsmsg(fromname, toname, msg):
    ajsmsg = {
        'header': {
            'uuid': get_uuid(),
            'time': time.time(),
            'fromname': fromname,
            'toname': toname,
            # from ip,from session
        },

        'body': {
            'msg': msg
        },

    }
    return json.dumps(ajsmsg)