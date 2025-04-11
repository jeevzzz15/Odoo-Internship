from odoo import models, fields

class FitnessMember(models.Model):
    _name = 'fitness.member'
    _description = 'Fitness Member'

    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    membership_plan_id = fields.Many2one('fitness.membership', string="Membership Plan")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    active = fields.Boolean(string="Active", default=True)


class FitnessMembership(models.Model):
    _name = 'fitness.membership'
    _description = 'Membership Plan'

    name = fields.Char(string="Plan Name", required=True)
    duration_days = fields.Integer(string="Duration (Days)")
    price = fields.Float(string="Price")
