# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#               <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Operating Unit",
    "version": "1.0",
    "author": "Eficent",
    "website": "http://www.eficent.com",
    "category": "Generic",
    "depends": ["base"],
    "description": """
Operating Unit
==============
An operating unit (OU) is an organizational entity part of a company, with
separate management ownership. Management by OU introduces the following
features:

- Partitions data from other OU's.
- Can define its own sequencing schemes.
- Administers user access to the data for processing and reporting.
- Is not product or customer specific.
- Provides OU specific P&L and Balance sheet

The current module defines the operating unit entity and the user's security
rules.

Other modules extend the standard Odoo apps with the operating unit.

    """,
    "init_xml": [],
    "update_xml": [
        "view/operating_unit.xml",
        "view/res_users.xml",
        "security/operating_unit_security.xml",
        "security/ir.model.access.csv",
    ],
    'demo_xml': [

    ],
    'test':[
    ],
    'installable': True,
    'active': False,
    'certificate': '',
}
