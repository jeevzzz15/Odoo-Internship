{
'name': 'Sample Module',
'version': '18.0.0.0',
'summary': 'This Module is for training purposes.',
'description': """This Module is for training purposes.
""",
'category':'',
'author': ' Jeevan V',
'website': 'www.zbeanztech.com',
"license": "LGPL-3",
'depends': ['sale','sale_management','account','contacts','product','report_xlsx','base'],
'data': [
    
    'security/security.xml', # Always keep security fiels @ top
    'security/ir.model.access.csv', # Always keep security fiels @ top
    'data/sequence.xml',
    'data/cron.xml',
    'data/my_mail_template.xml',
	'report/model_one_qweb_report.xml',
	'report/sale_order_report.xml',
	'report/report.xml',
    'wizard/sample_wizard_view.xml',
    'views/model_one_view.xml',
    'views/model_one_lines.xml', 
    'views/sale_order_view.xml',
	'views/my_employee_view.xml',
    'views/food.xml',
    'views/menu.xml',
    'views/car_rental.xml',
],
'test': [],
'demo': [],
'installable': True,
'auto_install': False,
'application': False,
}