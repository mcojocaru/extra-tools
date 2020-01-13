# -*- encoding: utf-8 -*-
{
    'name': 'Database Rollback',
    'version': '9.0.1.0.0',
    'category': 'web',
    'author': "Cojocaru Marcel <marcel.cojocaru@gmail.com>",
    'company': "Cojocaru Marcel Software PFA",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'web',
    ],
    'data': [
        'view/db_rollback.xml',
    ],
    'qweb': [
        'static/src/xml/db_rollback.xml',
    ],
    'installable': True,
    'auto_install': False,
}
