# R7. OrderedDict（1.7）

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
json.dumps(d)
