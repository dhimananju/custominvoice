from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class ContactSoftware(models.Model):
    _inherit = 'res.partner'
    
    swlist = fields.Many2many(
         'software',  # Reference to the custom model
         string="Software",
     )
     
    
