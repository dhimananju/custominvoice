from odoo import models, api,fields
import logging
from odoo.http import request
import werkzeug
import re

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
                # Example: checking if at least one 'lead_properties' record has a certain value
                for data in record.lead_properties:
                    record.lead_properties_valid = data.get("value")
            else:
                record.lead_properties_valid = False

    def request_consultant(self):
        # Gather the fields you want to send to the third-party site
        description = self.description or ''
        oppno = self.name or ''
        customername = self.partner_id.name or ''    
        #https://mypmstudio.com/projects/ti-sales/issues/new?issue[description]=prefilled%20description
        # Construct the URL with the fields as query parameters
        base_url = "https://mypmstudio.com/projects/ti-sales/issues/new"
        query_params = {
            'issue[description]': "{{lead(" + str(oppno) + ")}} \n" + re.sub(r'<[^>]+>', '', description),
            'issue[subject]': customername  + " - <What do you want the Consultant to Do?>",
        }

        # Construct the full URL with query parameters
        encoded_params = werkzeug.urls.url_encode(query_params)
        full_url = f"{base_url}?{encoded_params}"

        # Redirect to the third-party URL
        return {
            'type': 'ir.actions.act_url',
            'url': full_url,
            'target': 'new'  # 'new' opens in a new tab; 'self' opens in the same window
        }
        
