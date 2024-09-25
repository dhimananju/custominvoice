from odoo import models, api

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def request_consultant(self):
        return "anju here"