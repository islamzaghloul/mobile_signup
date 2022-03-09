# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'mobile login',
    'version': '1.0',
    'summary': 'login with mobile',
    'sequence': 10,
    'description': """hospital software management""",
    'category': 'productivity',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['auth_signup', 'web', 'base'],
    # here is adding dependances of other modules
    'data': [
        # 'views/patient.xml',
        # 'views/template.xml',
         'views/logintemplate.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
