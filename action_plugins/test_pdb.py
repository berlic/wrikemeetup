#!/usr/bin/env python

from ansible.plugins.action import ActionBase
import os

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        ret = "qqq"
        if os.environ.get('MYDEBUG') == '1':
            import sys; sys.stdin = open('/dev/tty')
            import pdb; pdb.set_trace()
        return { 'changed': False, 'ansible_facts': { 'ret': ret } }
