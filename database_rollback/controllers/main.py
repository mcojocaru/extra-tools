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
import openerp
import openerp.http as http
from openerp.http import request
import openerp.tools.config as config
from openerp import exceptions, _


class DBRollbackController(http.Controller):
    @http.route(
        '/web_database_rollback/activate',
        type='json', auth='none')
    def activate(self):
        if config['workers'] > 0:
            raise exceptions.Warning(_('Number of workers in Odoo configuration file should be 0.'))
        registry = openerp.modules.registry.RegistryManager.get(
            request.session.db)
        if registry.test_cr == None:
            registry.enter_test_mode()

    @http.route(
        '/web_database_rollback/rollback',
        type='json', auth='none')
    def rollback(self):
        registry = openerp.modules.registry.RegistryManager.get(
            request.session.db)
        if registry.test_cr != None:
            registry.leave_test_mode()

