from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class CRMLeadRedmine(models.Model):
    _inherit = 'res.partner'

    x_softwares = fields.Many2one(
        'contact.software',  # Reference to the custom model
        string="Softwaresss",
        ondelete='set null',
    )
    #software = fields.Char("sss")
