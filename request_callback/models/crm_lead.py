from odoo import models, api
import logging
_logger = logging.getLogger(__name__)

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def request_consultant(self):
        _logger.info(self.phone)
        _logger.info(self.lead_properties)
        return "anju here"
