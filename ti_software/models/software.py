from odoo import api,fields,models

class Software(models.Model):
    _name = "software"
    _description = "Software"

    name = fields.Char(string="Software Name", required=True)
    category = fields.Many2one(
        'software.category',  # Reference to the custom model
        string="Category",
        required=True,
        ondelete='restrict'  # Specifies what happens on deletion of related records
    )
    website = fields.Char(string="Website")
    description = fields.Html(string='Description')  # HTML editor field
