# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import except_orm
from openerp.osv import osv
import urllib2, httplib, urlparse, gzip, requests, json
from StringIO import StringIO
import openerp.addons.decimal_precision as dp
from datetime import date
import logging
import ast
from openerp import exceptions
from openerp.exceptions import ValidationError

#Get the logger
_logger = logging.getLogger(__name__)

class stock_change_location(models.TransientModel):
        _name = 'stock.change.location'

	picking_type_id = fields.Many2one('stock.picking.type',domain=[('code','=','incoming')],string='Depósito',required=True)

        @api.multi
        def confirm_line(self):
		if self.picking_type_id and \
			'active_id' in self.env.context.keys() and self.env.context['active_model'] == 'stock.move':
			move = self.env['stock.move'].browse(self.env.context['active_id'])
			vals = {
				'picking_type_id': self.picking_type_id.id,
				'location_dest_id': self.picking_type_id.default_location_dest_id.id
				}
			move.write(vals)
			picking = move.picking_id
			vals_picking = {
				'picking_type_id': self.picking_type_id.id
				}
			picking.write(vals_picking)
			vals_pack_operation = {
				'location_dest_id': self.picking_type_id.default_location_dest_id.id
				}
			if picking.pack_operation_product_ids:
				for pack_operation in picking.pack_operation_product_ids:
					pack_operation.write(vals_pack_operation)
		return None
