{
    'name': "TI Lead/opp Software",
    'version': '1.0',
    'author': "Anju Dhiman",
    'category': 'Uncategorized',
    'description': """
    Add software option to contact and add software/category menu to contact module we well
    """,
    'sequence':-100,
    'depends':['base','crm'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/software.xml',
        'views/leads.xml',
        'views/category.xml',
    ],
    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}
