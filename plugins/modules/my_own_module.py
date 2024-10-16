#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

version_added: "1.0.0"

description: Creates a file with text content at the specified path.

options:
    path:
        description: Path to new file.
        required: true
        type: str
    content:
        description: File content.
        required: true
        type: str

author:
    - Boris
'''

EXAMPLES = r'''
# Create file with content 
- name: Creates a file with text content at the specified path
    my_namespace.my_collection.my_own_module:
      path: "/tmp/text.txt"
      content: "This is a test"
'''

RETURN = r'''
# These are examples of possible return values.
path:
    description: File path.
    type: str
    returned: always
    sample: '/tmp/text.txt'
content:
    description: File content.
    type: str
    returned: always
    sample: 'This is a test'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )
    
    result = dict(
        changed=False,
        failed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result['path'] = module.params['path']
    result['content'] = module.params['content']

    file = open(module.params['path'], 'w')
    file.write(module.params['content'])
    file.close()
    
    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
