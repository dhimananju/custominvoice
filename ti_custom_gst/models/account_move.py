# -*- coding: utf-8 -*-

from odoo import fields, models

class Accountmove(models.Model):
    _inherit = "account.move"

    legal_entity_punjab = fields.Boolean(string="Legal Entity Punjab", default=False)  # Checkbox field
