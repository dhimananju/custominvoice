# -*- coding: utf-8 -*-

from odoo import fields, models, _

class respart(models.Model):
    _inherit = 'res.partner'

    
    relationship = fields.Selection([
        ('decision_maker', 'Decision Maker'),
        ('influencer', 'Influencer')
    ], string='Relationship', default='decision_maker')
    lead_id = fields.Many2one('crm.lead', string='CRM Lead', ondelete='set null')

    
