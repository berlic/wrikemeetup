#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

IS_FAILED=True

module = AnsibleModule(argument_spec={})

if module._debug:
    import epdb; epdb.serve()

if IS_FAILED:
    module.fail_json(msg="Ouch!")
else:
    module.exit_json(msg="Success!")
