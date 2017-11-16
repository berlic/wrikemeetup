#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.mylib import hello

module = AnsibleModule(argument_spec={})
module.exit_json(msg=hello())
