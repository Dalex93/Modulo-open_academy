# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Modulo de Cursos""",

    'description': """
        Open Academy module for managing trainings:
            - training course
            - training session
            - attendees registration
    """,

    'author': 'Cristian Alexander Martinez',
    'company': 'ZeroCorp',
    'website': 'https://github.com/AlxZeroX',
    'live_test_url': 'https://github.com/AlxZeroX',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Courses',
    'version': '14.0.14.10.21',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website_slides'],

    # always loaded
    'data': [
        'data/slide_channel_data.xml',
        'data/slide_channel_data_v13.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
