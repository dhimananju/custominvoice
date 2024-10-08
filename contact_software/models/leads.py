from odoo import models, api,fields
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

class CRMLeadSoftware(models.Model):
    _inherit = 'crm.lead'
    
    swlist = fields.Many2many(
         'contact.software',  # Reference to the custom model
         string="Software",
     )
    
    @api.model
    def create(self, vals):
        _logger.info("create leads method called")
        lead = super(CRMLeadSoftware, self).create(vals)
        partner_id = lead.partner_id
        swlist = lead.swlist
        _logger.info(swlist)
        #check if partner id exist or not , if exist update software list there
        partner_record = request.env['res.partner'].sudo().browse(partner_id.id)
        if partner_record.exists():
            partner_record.write({
                'swlist': swlist,
            })
                

        return lead
    
    def write(self, vals): 
        _logger.info("write function leads")
        lead = super(CRMLeadSoftware, self).write(vals)
        partner_id = self.partner_id
        swlist = self.swlist
        _logger.info(swlist)
        #check if partner id exist or not , if exist update software list there
        partner_record = request.env['res.partner'].sudo().browse(partner_id.id)
        if partner_record.exists():
            partner_record.write({
                'swlist': swlist,
            })
        return lead