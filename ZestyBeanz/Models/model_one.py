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
    model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Product")
    sale_id = fields.Many2one('sale.order', string="Sales")

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