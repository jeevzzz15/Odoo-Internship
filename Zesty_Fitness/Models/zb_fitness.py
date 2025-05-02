from odoo import models, fields, api
from datetime import timedelta

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
    total_amount = fields.Float(string="Total Amount", compute="_compute_total", store=True)

    @api.onchange('start_date', 'membership_plan_id')
    def _onchange_membership_dates(self):
        if self.start_date and self.membership_plan_id.duration_days:
            self.end_date = self.start_date + timedelta(days=self.membership_plan_id.duration_days)

    @api.depends('membership_plan_id.price', 'membership_plan_id.duration_days')
    def _compute_total(self):
        for rec in self:
            if rec.membership_plan_id:
                rec.total_amount = rec.membership_plan_id.price * rec.membership_plan_id.duration_days
            else:
                rec.total_amount = 0.0


class FitnessMembership(models.Model):
    _name = 'fitness.membership'
    _description = 'Membership Plan'

    name = fields.Char(string="Plan Name", required=True)
    duration_days = fields.Integer(string="Duration (Days)")
    price = fields.Float(string="Price")
