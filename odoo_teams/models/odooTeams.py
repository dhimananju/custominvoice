from odoo import models, api,fields
import logging
from odoo.http import request
import werkzeug
import re
from bs4 import BeautifulSoup
import json
import requests

_logger = logging.getLogger(__name__)

class odooTeams(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        _logger.info(vals)
        _logger.info("create method called")
        lead = super(odooTeams, self).create(vals)
        name = lead.name
        companyid = lead.company_id
        #call custom function to send emssage to teams channel
        #add check for compamny id 5, 6, 10, 1 - Channel 19:c4c08d6944614b2e8930905c905e1c68
        allowed_companies = [1, 5, 6, 10]
        channelId = '19:c4c08d6944614b2e8930905c905e1c68'
        _logger.info(companyid)
        if companyid in allowed_companies:
            _logger.info(companyid)
            self.sendMessageTeams(name,channelId)
            
        allowed_companies_secod = [3]
        channelId_Secon = '19:49218707ae584db683da25b254de80d8'
        if companyid in allowed_companies_secod:
            self.sendMessageTeams(name,channelId_Secon)

        return lead
    
    @api.model
    def write(self, vals): 
        lead = super(odooTeams, self).write(vals)
        # Check if the message is related to a lead
        if vals.get('description'):
            # Custom logic here, e.g. log, notify, etc.
            name = self.name
            companyid = self.company_id
            # Parse the HTML and extract text
            soup = BeautifulSoup(vals.get('description'), "html.parser")
            plain_text = soup.get_text()
            _logger.info(plain_text)
            #call custom function to send emssage to teams channel
            #add check for compamny id 5, 6, 10, 1 - Channel 19:c4c08d6944614b2e8930905c905e1c68
            _logger.info(companyid)
            if companyid in allowed_companies:
                _logger.info(companyid)
                self.sendMessageTeams(name,channelId)
                
            allowed_companies_secod = [3]
            channelId_Secon = '19:49218707ae584db683da25b254de80d8'
            if companyid in allowed_companies_secod:
                self.sendMessageTeams(name,channelId_Secon)

        return lead
    
    def sendMessageTeams(self,name,channelId):
        _logger.info("sendMessageTeams")
        _logger.info(name)
        redmineurl = "https://mypmstudio.com/NotifyChannel.json"
        headers = {"Message": "text-message" ,"ChannelName":"19:c4c08d6944614b2e8930905c905e1c68","X-Redmine-API-Key":channelId}
        response = requests.post(redmineurl, headers=headers)
        _logger.info(response.content)

    
   
