from odoo import models, fields

class Car_rental(models.Model):
    _name = "car.rental"
    _description = "Model For Car rentals"

    car_name = fields.Char(string="Name")
    car_model = fields.Char(string='Model')
    body_color = fields.Char(string='Color')
    wheel_type = fields. Selection([('alloy wheels', 'Alloy Wheels '), ('chrome wheels', 'Chrome Wheels '), ])
    amount = fields.Float(string="Standard Price")
    available = fields.Boolean("Active", default=True)
    seat_count = fields.Integer(string="Seat count")