# coding: utf-8
#  -*- encoding: utf-8 -*-
# #############################################################################
#
#    Authors: Cojocaru Marcel (marcel.cojocaru@gmail.com)
#    Copyright (c) 2019 Cojocaru Aurelian Marcel PFA
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
        '/database_rollback/activate',
        type='json', auth='user')
    def activate(self):
        if config['workers'] > 0:
            raise exceptions.Warning(_('Number of workers in Odoo configuration file should be 0.'))

        registry = openerp.modules.registry.RegistryManager.get(
            request.session.db)
        if registry.test_cr is None:
            registry.enter_test_mode()
            registry.clear_caches()

    @http.route(
        '/database_rollback/rollback',
        type='json', auth='user')
    def rollback(self):
        registry = openerp.modules.registry.RegistryManager.get(
            request.session.db)
        if registry.test_cr is not None:
            registry.leave_test_mode()
            registry.clear_caches()
