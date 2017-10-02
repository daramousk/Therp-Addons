# -*- coding: utf-8 -*-
# © 2013-2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "External users",
    "summary": "Allow external users on your system",
    "version": "10.0.1.0.0",
    "author": "Therp BV",
    "category": 'External users',
    'website': 'http://therp.nl',
    'depends': [
        'base',
    ],
    'data': [
        'data/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'view/res_users.xml',
    ],
    'license': 'AGPL-3',
}
