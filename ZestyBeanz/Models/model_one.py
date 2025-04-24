from odoo import models, fields, api

class ModelOne(models.Model):
    _name = "model.one"
    _description = "Model One"

    seq=fields.Char(string="Sequence")
    name = fields.Char(string="Name", help='A normal name field', required=True, copy=False)
    age = fields.Integer(string="Age", default=18)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
    active = fields.Boolean("Active", default=True)
    description = fields.Text("Description", default="Test Description")
    email = fields.Char(string="Email", required=True, copy=False)
    joining_date = fields.Date(string="Joining Date", required=True)
    partner_ids = fields.Many2many('res.partner',string="Partner")
    sale_ids = fields.Many2many('sale.order','model_one_sale_rel','model_one_id','sale_id', string="Sale")
    product_ids = fields.Many2many('product.template', 'model_one_prduct_rel', 'model_one_id', 'product_id',  string="Products")
    model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Product")
    sale_id = fields.Many2one('sale.order', string="Sales")

    def write_values(self):
        #many2many fields
        products = self.env['product.template'].search([('list_price', '>', 200)], limit=1).id
        order = self.env['sale.order'].search([('id', '=', 26)], limit=1).id
        #self.write({'product_ids' : [[6, 0, products]]}) 
        #self.write({'product_ids' : [[5]]})
        #self.write({'product_ids' : [[4, products]]})
        #self.write({'product_ids' : [[3, products]]})
        #self.write({'sale_ids' : [[2, order]]})
        #self.write({'product_ids' : [[0, 0, {'name': 'Test Product', 'list_price':200}]]})

        #one2many fields
        #self.write({'model_one_line_ids' : [[0, 0, {'name': 'Test 1', 'product_id':products, 'price': 250}]]})
        #line = self.model_one_line_ids.filtered(lambda l : l.price == 300).id
        #existing_line = self.env['model.one.lines'].search([('price', '=', 300)], limit=1).id
        ex_line = self.env['model.one.lines'].search([('model_one_id', '=', False)], limit=1).id
        #self.write({'model_one_line_ids' : [[1, line, {'price': 350}]]})
        #self.write({'model_one_line_ids' : [[2, line]]})
        #self.write({'model_one_line_ids' : [[3, line]]})
        #self.write({'model_one_line_ids' : [[4, existing_line]]})
        #self.write({'model_one_line_ids' : [[4, ex_line]]})
        self.write({'model_one_line_ids' : [[6, 0, ex_line]]})

    def helloworld(self):
        print("Hello World")
    
    def show_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Sample Wizard',             
            'res_model': 'sample.wizard',       
            'view_mode': 'form',
            'view_id': self.env.ref('ZestyBeanz.view_form_sample_wizard').id,
            'target': 'new',
            'context': {'default_name': 'Thunder'}
    }


    @api.model
    def create(self,vals):
        print('----------', self.env['ir.sequence'])
        vals['seq'] = self.env['ir.sequence'].next_by_code('sequence.model.one')
        res = super(ModelOne,self).create(vals)
        return res

class ModelOnelines(models.Model):
    _name = "model.one.lines"
    _description = "Model One lines"

    name = fields.Char(string="Name", help='A normal name field')
    price = fields.Float(string="Standard Price")
    product_id = fields.Many2one('product.template', string="Product")
    model_one_id = fields.Many2one('model.one', string="Model One", domain="['|',('gender', '=', 'female'),('age','>',18)]")