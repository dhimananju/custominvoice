from odoo import models, api,fields
import logging
from odoo.http import request
import werkzeug
import re
#from bs4 import BeautifulSoup
import json
import requests

_logger = logging.getLogger(__name__)

class odooTeams(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        _logger.info("create method called")
        lead = super(odooTeams, self).create(vals)
        name = lead.name
        companyid = lead.company_id
        #call custom function to send emssage to teams channel
        #add check for compamny id 5, 6, 10, 1 - Channel 19:c4c08d6944614b2e8930905c905e1c68
        msg = "A new lead/opp "+name+" is added"
        _logger.info(msg)
        allowed_companies = [1, 5, 6, 10]
        channelId = '19:c4c08d6944614b2e8930905c905e1c68'
        if companyid.id in allowed_companies:
            self.sendMessageTeams(name,channelId,msg)
            
        allowed_companies_secod = 3
        channelId_Secon = '19:49218707ae584db683da25b254de80d8'
        if companyid.id == allowed_companies_secod:
            self.sendMessageTeams(name,channelId_Secon,msg)

        return lead
    
   
    def write(self, vals): 
        _logger.info("write function")
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
            msg = "A new lead/opp "+name+" is edited with description: plain_text"
            allowed_companies = [1, 5, 6, 10]
            channelId = '19:c4c08d6944614b2e8930905c905e1c68'
            if companyid.id in allowed_companies:
                self.sendMessageTeams(name,channelId,msg)
                
            allowed_companies_secod = 3
            channelId_Secon = '19:49218707ae584db683da25b254de80d8'
            if companyid.id == allowed_companies_secod:
                self.sendMessageTeams(name,channelId_Secon,msg)

        return lead
    
    def sendMessageTeams(self,name,channelId,msg):
        _logger.info("sendMessageTeams")
        redmineurl = "https://mypmstudio.com/NotifyChannel.json"
        headers = {"Message": msg ,"ChannelName":channelId,"X-Redmine-API-Key":"eaffd4f722364a677d97e3e775eacfafc8adca82"}
        response = requests.post(redmineurl, headers=headers)
        _logger.info(response.content)

    
   
