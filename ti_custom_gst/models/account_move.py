# -*- coding: utf-8 -*-

from odoo import fields, models,api

class Accountmove(models.Model):
    _inherit = "account.move"

    legal_entity_punjab = fields.Boolean(string="Legal Entity Punjab", default=False)  # Checkbox field

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
    }
