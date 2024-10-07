from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class CRMLeadRedmine(models.Model):
    _inherit = 'res.partner'
    swww = fields.Char(String="Tetsting")
   
