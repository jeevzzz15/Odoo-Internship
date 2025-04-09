from odoo import models, fields , api
from odoo.exceptions import ValidationError
from datetime import date
class Food(models.Model):
	_name = "food.food"
	_description = "Model For Food"
	_rec_name = "partner_id"


	# fields
	name = fields.Char(string="Name")
	partner_id = fields.Many2one('res.partner',string="Name")
	price = fields.Float(string="Standard Price")
	quantity = fields.Integer(string="Amount")
	review = fields.Text(string="Review Of The Food")
	is_satisfied = fields.Boolean(string="Satisfied/Not")
	check_in = fields.Date(string="Check In")
	served_time = fields.Datetime(string="Served Time")
	types = fields.Selection([('dine_in','Dine In'),('delivery','Delivery')])
	images = fields.Binary(string="Images")
	blog = fields.Html(string="Blog")
	sale_order_id = fields.Many2one('sale.order',string="Sale Order")
	invoice_id = fields.Many2one('account.move',string="Related Invoice")

	_sale_created = fields.Boolean(string="Sale Order Created")



	# @api.model
	# def default_get(self, fields_list):
	# 	res = super(Food, self).default_get(fields_list)
	# 	res['is_satisfied'] = True
	# 	return res
	
	def create_invoice(self):
		pass
	def create_contacts(self):
		pass
	def create_purchase_order(self):
		pass

	# ORM Methods
	# Create
	# Extend     = Extending base logic + Custom logic (base+custom)
	# Override   = Is Removing all the base Function and Setting Your logic
	# @api.model
	# def create(self,vals):

	# 	print("Before RES")
	# 	print("Self is ===",self)
	# 	print("Vals is ===",vals)

	# 	res = super(Food,self).create(vals)

	# 	print("After RES")
	# 	print("Self is ===",self)
	# 	print("Vals is ===",vals)
	# 	print("RES is ===",res)

	# 	if res.is_satisfied == False: # checking the is_satisfield is true or not
	# 		res.is_satisfied = True   # assingning it true

	# 	return res
	
	def write(self,vals):
		
		print("Before RES")
		print("Self is ===",self)
		print("Vals is ===",vals)
		print("Before  RES=== ",self.review)

		print("==========================")
		res = super(Food,self).write(vals)

		print("After RES")
		print("Self is ===",self)
		print("Vals is ===",vals)
		print("RES is ===",res)
		print("After Res  === ",self.review)
		return res
	

	def unlink(self):
		res = super(Food, self).unlink()

		return res

	# CRUD
	# C  = Create
	def create_sale_order(self):
		sale_order = self.env['sale.order'].create([{
			'partner_id':self.partner_id
			}])
		self._sale_created = True
		return sale_order
	

	# R  - Read
	# Search and Browse

	def purchase_records(self):
		foood = self.env['food.food'].search([('price','>',100),('is_satisfied','=',True)])
		print("The Result is === ",foood)

		food_browse = self.env['food.food'].browse(5)
		print("Browse Output is",food_browse)


	# U 
	# Update - Write

	def change_the_record(self):
		food_browse = self.env['food.food'].browse(self.id)
		food_browse.write({
			'review':"The value changed because of the write function",
			'quantity':1000

		})

	# D
	# Delete - Unlink

	def delet_the_rec(self):
		food_browse = self.env['food.food'].browse(self.id)
		food_browse.unlink()

	# oprators 
	# = , <  ,  >   ,  =>   ,  <=  , like  , ilike  , | (or)

	@api.model
	def default_get(self, fields_list):
		res = super(Food, self).default_get(fields_list)
		res['review'] = "The Value is setted before saving"
		res['is_satisfied'] = True
		return res
	

	
	date_of_birth = fields.Date(string="Date of Birth")
	age = fields.Integer(string="Age" , compute="_compute_age")

	@api.depends('date_of_birth')
	def _compute_age(self):
		for rec in self:
			if rec.date_of_birth: # To avoid the error
				today = date.today()
				born = rec.date_of_birth
				rec.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
			else:
				rec.age = 0
			