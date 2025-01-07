# -*- coding: utf-8 -*-

from odoo import fields, models, _

class respart(models.Model):
    _inherit = 'res.partner'

   name_with_company = fields.Char(
        string="Name with Company", compute="_compute_name_with_company"
    )

    relationship = fields.Selection([
        ('decision_maker', 'Decision Maker'),
        ('influencer', 'Influencer')
    ], string='Relationship', default='decision_maker')
    lead_id = fields.Many2one('crm.lead', string='CRM Lead', ondelete='set null')

    
