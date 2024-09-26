from odoo import models, api
import logging
import json
import requests

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_creat_payments(self):
        # Call the super method to ensure the base functionality is executed
        res = super(AccountPayment, self).action_creat_payments()
        _logger.info("anju testing custom invoice")
        # Get invoices linked to this payment
        for payment in self:
            if payment.invoice_ids:
                for invoice in payment.invoice_ids:
                    #invoice.custom_action_after_payment()

        return res

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        # Call the original function to ensure normal behavior
        res = super(AccountMove, self).action_post()
        # Call the custom function after posting the invoice
        for invoice in self:
            text = "Invoice has been raised"
            self.redmine_api(invoice.ref,2,text)
        return res
    
    @api.model
    def button_mark_as_paid(self):
        # Call the super method to ensure the base functionality is executed
        res = super(AccountMove, self).button_mark_as_paid()
        for move in self:
             _logger.info("testing custom invoice")
             _logger.info(move.payment_state)
             _logger.info(move.ref)
             if move.ref:
                _logger.info("Change status to in progress")
                if move.payment_state != "paid":
                    text = "Invoice has been raised"
                    self.redmine_api(move.ref,2,text)

        return res
        
    def action_invoice_paid(self):
        """get payment state and ticket ref  and call redmine API function"""
        res = super(AccountMove, self).action_invoice_paid()
        for move in self:
             _logger.info("testing custom invoice")
             _logger.info(move.payment_state)
             _logger.info(move.ref)
             if move.ref:
                _logger.info("testing custom invoice12333")
                if move.payment_state == "paid":
                    text = "This Invoice is paid so closing the ticket"
                    self.redmine_api(move.ref,5,text)
                 
                 
    """custom function to hit redmine API"""         
    def redmine_api(self,ref,status,text):
        _logger.info("testing custom invoice2")
        redmineurl = "https://mypmstudio.com/issues/"+ref+".json"
        dataparams = { "issue": {"notes": text, "status_id": status } }
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache","X-Redmine-API-Key":"eaffd4f722364a677d97e3e775eacfafc8adca82"}
        response = requests.put(redmineurl, data=json.dumps(dataparams), headers=headers)
        
