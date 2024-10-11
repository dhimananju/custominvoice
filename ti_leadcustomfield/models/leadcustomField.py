from odoo import models, fields
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

class leadcustomField(models.Model):
    _inherit = 'crm.lead'

    pms_ticket = fields.Char(string="PMS Ticket Number")
    
    #update pms_ticket when pipleline edited with PM ticket url
    def write(self, vals): 
        # Check if the message is related to a lead
        for field_name in self:
            pms_ticket = field_name.pms_ticket
            record_type = field_name.type
            if record_type == "opportunity":
                if vals.get('pms_ticket'):
                    vals['pms_ticket'] = 'https://mypmstudio.com/issues/'+vals['pms_ticket']
                
        lead = super(leadcustomField, self).write(vals)
        return lead
    
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