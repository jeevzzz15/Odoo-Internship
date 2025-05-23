from odoo import models, fields, api

class MyEmployee(models.Model):
	
	_name = "my.employee"
	_description = "Employee"
	
	employee_name = fields.Char(string="Employee Name", required=True)
	designation = fields.Char(string="Designation")
	phone_number = fields.Integer(string="Phone")
	address = fields.Text("Description")
	status = fields.Selection([('active', 'Active'), ('on_leave', 'On Leave'), ('resigned', 'Resined'), ('terminated', 'Terminated')], string="Status")