from odoo import models, fields
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

class leadcustomField(models.Model):
    _inherit = 'crm.lead'

    pms_ticket = fields.Char(string="PMS Ticket Number")
  
    
class CrmLead(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    def action_apply(self):
        result = super(CrmLead, self).action_apply()
        
        # Get the opportunities that were created or converted
        leads = self.env['crm.lead'].browse(self._context.get('active_ids', []))

        # Update the custom field of the opportunity
        for lead in leads:
            if lead.type == 'opportunity':  # Ensure it's an opportunity
                lead.write({
                    'pms_ticket': 'https://mypmstudio.com/issues/'+lead.pms_ticket,
                })