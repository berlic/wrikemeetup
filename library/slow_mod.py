#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: slow_mod
short_description: Slow module to demonstrate async logging
description:
   - Pauses for several seconds
   - Sends async log messages between wait intervals
options:
    seconds:
        description:
            - How many seconds to wait
        default: 5
        required: false
    count:
        description:
            - How many wait iterations to do
        default: 2
        required: false

author:
    - Konstantin Suvorov
'''

EXAMPLES = '''
- name: Wait for 6 seconds
  slow_mod:
    seconds: 3
    count: 2
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.async_send import send_msg
import time

module = AnsibleModule(
    argument_spec=dict(
        seconds=dict(type='int', required=False, default=5),
        count=dict(type='int', required=False, default=2)
    )
)

def rem_log(msg):
    if module._verbosity > 0:
        send_msg(msg)

rem_log('module started')
for c in range(module.params['count']):
    s = module.params['seconds']
    time.sleep(s)
    rem_log('slept for {} sec, count {}'.format(s,c))
rem_log('done')
module.exit_json(msg="Success!")
