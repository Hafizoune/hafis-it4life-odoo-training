# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """School trainings""",

    'description': """
        Odoo school module for school trainings:
            - training courss
    """,

    'author': "Hafiz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [ 
         'views/course.xml',
         'views/session.xml',
         'views/contact.xml',
         'views/theme.xml',
    ],

}
