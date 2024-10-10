{
    'name': 'TI-PMS ticket number',
    'version': '1.0',
    'category': 'Invoicing',
    'summary': 'Add custom field in lead for PMS ticket number',
    'description': """
        Add custom field in lead for PMS ticket number
    """,
    'author': 'Anju Dhiman',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license':'LGPL-3',
}
