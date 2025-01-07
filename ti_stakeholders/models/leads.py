from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class crmLeads(models.Model):
    _inherit = "crm.lead"
    #contactline_ids = fields.One2many("res.partner",'lead_id','Contacts')
    contactline_ids = fields.One2many("stake.holder",'lead_id','Contacts Detail')

class stakeHolder(models.Model):
    _name = "stake.holder"
     
    lead_id = fields.Many2one("crm.lead","CRM lead")
    partner_id = fields.Many2one("res.partner",'Contact Name',domain=[('is_company', '!=', True),('parent_id', '!=', False)])
    
    relationship = fields.Selection([
        ('decision_maker', 'Decision Maker'),
        ('influencer', 'Influencer')
    ], string='Relationship', default='decision_maker')
            
           
