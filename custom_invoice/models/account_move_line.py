from odoo import models, api
import logging
import json
import requests

_logger = logging.getLogger(__name__)

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def reconcile(self):
        """
        Override the reconcile method to include custom logic.
        """
        # Call the original reconcile method
        result = super(AccountMoveLine, self).reconcile()
        _logger.info("reconcile")
        # Fetch the related invoices and apply custom logic
        for line in self:
            invoice = line.move_id
            if invoice and invoice.is_invoice():
                if invoice.payment_state == 'paid':
                    if invoice.ref!="":
                        checkIfexist =  self.checkTicketExist(invoice.ref)
                        if checkIfexist:
                                text = "This Invoice is paid so closing the ticket"
                                self.redmine_api(invoice.ref,5,text)

        return result
  
    def checkTicketExist(self,ref):
        redmineurl = "https://mypmstudio.com/issues/"+ref+".json"
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache","X-Redmine-API-Key":"c114e0da57abd372e21771c5e0c334674bcb871f"}
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
