from odoo import models, api,fields
import logging

_logger = logging.getLogger(__name__)

class ContactSoftware(models.Model):
    _inherit = 'res.partner'
    
    swlist = fields.Many2many(
         'contact.software',  # Reference to the custom model
         string="Software",
     )
     
    @api.model
    def create(self, vals):
        _logger.info("create leads method called")
        lead = super(odooTeams, self).create(vals)
        partner_id = lead.partner_id
        swlist = lead.swlist
        _logger.info(swlist)
        #check if partner id exist or not , if exist update software list there
        #partner_record = request.env['res.partner'].sudo().browse(partner_id.id)
            #if partner_record.exists():
                

        return lead
