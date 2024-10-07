{
    'name': "TI Odoo Teams Integration",
    'version': '1.0',
    'author': "Anju Dhiman",
    'category': 'Uncategorized',
    'description': """
    Using Redmine API whenever a new lead is created or a new opportunity is created or a new note is logged on a lead or opportunity, notify the Teams channel for that Lead/Opportunity
    """,
    'sequence':-100,
    'depends':['base','crm'],
    'data':[
    ],
    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}