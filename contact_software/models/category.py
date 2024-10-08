from odoo import api,fields,models

class ContactSoftware(models.Model):
    _name = "software.category"
    _description = "Contacts Software"

    name = fields.Char(string="Category Name", required=True)
    active = fields.Boolean(string="Active", default=True)
