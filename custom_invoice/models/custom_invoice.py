from odoo import models, api
import logging
import json
import requests

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _invoice_paid_hook(self):
        for move in self:
             _logger.info("override _invoice_paid_hook")
             if move.payment_state == "paid":
                 if move.ref!="":
                        checkIfexist =  self.checkTicketExist(move.ref)
                        if checkIfexist:
                                text = "This Invoice is paid so closing the ticket"
                                self.redmine_api(move.ref,5,text)
    
    def action_post(self):
        # Call the original function to ensure normal behavior
        res = super(AccountMove, self).action_post()
        # Call the custom function after posting the invoice
        #for invoice in self:
            # if invoice.payment_state != "paid":
            #     if invoice.ref!="":
            #         checkIfexist =  self.checkTicketExist(invoice.ref)
            #         _logger.info(checkIfexist)
            #         if checkIfexist:
            #                 text = "Invoice has been raised"
            #                 self.redmine_api(invoice.ref,2,text)

    def checkTicketExist(self,ref):
        redmineurl = "https://mypmstudio.com/issues/"+ref+".json"
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache","X-Redmine-API-Key":"eaffd4f722364a677d97e3e775eacfafc8adca82"}
        response = requests.get(redmineurl, headers=headers)
        try:
             data = response.json()  
             return data
        except:
             return False
        
                
    """custom function to hit redmine API"""         
    def redmine_api(self,ref,status,text):
            _logger.info("redmine update")
            redmineurl = "https://mypmstudio.com/issues/"+ref+".json"
            dataparams = { "issue": {"notes": text, "status_id": status } }
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache","X-Redmine-API-Key":"eaffd4f722364a677d97e3e775eacfafc8adca82"}
            response = requests.put(redmineurl, data=json.dumps(dataparams), headers=headers)
