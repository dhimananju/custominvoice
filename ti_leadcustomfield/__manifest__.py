{
    'name': "TI PMS tciket number",
    'version': '1.0',
    'author': "Anju Dhiman",
    'category': 'Hospital Management',
    'summary':'Custom field in lead PMS tciket number',
    'description': """
    PMS tciket number
    """,
    'sequence':-100,
    'depends':['base','crm'],
    'data':[
        'views/leadCustomField.xml',
    ],
    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}