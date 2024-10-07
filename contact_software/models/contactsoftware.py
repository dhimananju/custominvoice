from odoo import api,fields,models

class ContactSoftware(models.Model):
    _name = "contact.software"
    _description = "Contacts Software"

    name = fields.Char(string="Software Name", required=True)
    category = fields.Many2one(
        'software.category',  # Reference to the custom model
        string="Category",
        required=True,
        ondelete='set null'  # Specifies what happens on deletion of related records
    )
    website = fields.Char(string="Website")
    description = fields.Html(string='Description')  # HTML editor field
