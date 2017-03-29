# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import tools
import datetime
import logging
import poplib
import time
import email

from openerp.osv import fields, osv
from openerp import tools, api, SUPERUSER_ID
from openerp.tools.translate import _
from openerp.exceptions import UserError

_logger = logging.getLogger(__name__)

class as_stock_quant(osv.osv):
	_name = "as.stock.quant"
	_description = "AS Stock Quant"
	_auto = False

	_columns = {
		'location_id': fields.many2one('stock.location','Location'),
		'company_id': fields.many2one('res.company','Company'),
		'product_id': fields.many2one('product.product','Company'),
		'qty': fields.integer('Qty'),
		}

	def init(self, cr):
        	tools.sql.drop_view_if_exists(cr, 'as_stock_quant')
	        cr.execute("""
			create view as_stock_quant as 
				select max(a.id) as id,a.location_id as location_id,a.company_id as company_id,
					a.product_id as product_id,sum(qty) as qty from stock_quant a group by 2,3,4
	        	""")
                                                 
