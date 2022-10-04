# -*- encoding: utf-8 -*-
# #############################################################################
#
#    Web Easy Switch Company module for OpenERP
#    Copyright (C) 2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
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
#############################################################################
import odoo
import odoo.http as http
from odoo.http import request
import odoo.tools.config as config
from odoo import exceptions, _
from odoo.tests import common

class DBRollbackController(http.Controller):
    @http.route('/database_rollback/activate', type='json', auth='none')
    def activate(self):
        if config['workers'] > 0:
            raise exceptions.Warning(_('Number of workers in Odoo configuration file should be 0.'))
        registry = odoo.registry(common.get_db_name())
        if registry.test_cr is None:
            registry.enter_test_mode(registry.cursor())

    @http.route('/database_rollback/rollback', type='json', auth='none')
    def rollback(self):
        registry = odoo.registry(common.get_db_name())
        if registry.test_cr is not None:
            registry.leave_test_mode()
            db_name = common.get_db_name()
            odoo.registry(db_name)
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
