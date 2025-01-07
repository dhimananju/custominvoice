{
    'name': "Stakholders for Deal",
    'version': '18.0',
    'author': "Anju Dhiman",
    'category': 'Stakholders for Deal',
    'description': """Stakholders for Deal""",
    'sequence':-9999,
    'depends':["base","contacts","crm"],
     'data':[
         'security/ir.model.access.csv',
         'views/crm_lead.xml',
        ],
    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}
