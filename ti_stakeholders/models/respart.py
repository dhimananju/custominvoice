# -*- coding: utf-8 -*-

from odoo import fields, models, _

class respart(models.Model):
    _inherit = 'res.partner'

    lead_id = fields.Many2one('crm.lead', string='CRM Lead', ondelete='set null')

    
