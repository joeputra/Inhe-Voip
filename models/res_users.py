# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, _, api


class Users(models.Model):
	_inherit = 'res.users'

	voip_status = fields.Selection([
		('dnd', 'Do Not Disturb'),
		], string="Status Agent")
	sip_ignore_incoming = fields.Boolean("Reject All Incoming Calls", default=False,
                                         groups="base.group_user")
	
	# @api.model
	# def set_voip_status(self, status):
	# 	self.voip_status = status
	# 	return {
    #         'type': 'ir.actions.client',
    #         'tag': 'reload',
    #     }
	@api.onchange('voip_status')
	def onchange_voip_status(self):
		return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

# from odoo import models, fields, api


# class inhe_voip(models.Model):
#     _name = 'inhe_voip.inhe_voip'
#     _description = 'inhe_voip.inhe_voip'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
