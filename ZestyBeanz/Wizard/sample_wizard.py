from odoo import _, api, fields, models
from datetime import date

class SampleWizard(models.TransientModel):
    _name = 'sample.wizard'
    _description = 'Sample wizard'

    name = fields.Char(string="Name")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age')

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                today = date.today()
                # Calculate age by comparing the year, month, and day
                age = today.year - record.dob.year
                if (today.month, today.day) < (record.dob.month, record.dob.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0