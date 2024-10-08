from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class CompanySoftware(models.Model):
    _inherit = 'res.company'
    
    swlist = fields.Many2many(
         'contact.software',  # Reference to the custom model
         string="Software",
     )
