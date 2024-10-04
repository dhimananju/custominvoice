from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class CRMLeadRedmine(models.Model):
    _inherit = 'res.partner'

    x_sw = fields.Many2one(
        'contact.software',  # Reference to the custom model
        string="Software",
        ondelete='set null',
    )
    #software = fields.Char("sss")
