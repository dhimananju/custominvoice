{
    'name': "TI Lead/opp Software",
    'version': '1.0',
    'author': "Anju Dhiman",
    'category': 'Uncategorized',
    'description': """
    Add software to lead/opportunity and organisation module  """,
    'sequence':-100,
    'depends':['base','crm'],
    'data':[
        'views/menu.xml',
        'views/software.xml',
        'views/leads.xml',
        'views/category.xml',
        'views/company.xml',
        'views/contact.xml',
    ],
    'installable':True,
    'auto_install': False,
    'application':True,
    'license':'LGPL-3',
}
