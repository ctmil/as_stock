# -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError, UserError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

class stock_move(models.Model):
	_inherit = 'stock.move'

        @api.multi
        def change_location(self):
                return {'type': 'ir.actions.act_window',
                        'name': 'Completar requisicion',
                        'res_model': 'stock.change.location',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'target': 'new',
                        'nodestroy': True,
                        }

