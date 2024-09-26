from odoo import models, api,fields
import logging
_logger = logging.getLogger(__name__)

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    lead_properties_valid = fields.Boolean(
        string='Lead Properties Valid', compute='_compute_lead_properties_valid')

    @api.depends('lead_properties')
    def _compute_lead_properties_valid(self):
        for record in self:
            # Customize this condition based on how you want to evaluate lead_properties
            if record.lead_properties:
                _logger.info(record.lead_properties)
                for val in record.lead_properties:
                    _logger.info(val)
                    # Example condition: Check if the One2many field has at least one entry
                    record.lead_properties_valid = val.value
            else:
                record.lead_properties_valid = ""

    def request_consultant(self):
        _logger.info(self.phone)
        _logger.info(self.lead_properties)
        _logger.info(self.lead_properties_valid)
        return "anju here"
