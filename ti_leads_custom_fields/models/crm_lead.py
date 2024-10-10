from odoo import models, api,fields
import logging
from odoo.http import request
import werkzeug
import re

_logger = logging.getLogger(__name__)

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    pms_ticket_number = fields.Char(string='PMS Ticket Number')

   
