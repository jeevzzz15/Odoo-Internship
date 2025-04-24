from odoo import _, api, fields, models

class SampleWizard(models.TransientModel):
    _name = 'sample.wizard'
    _description = "Sample wizard"
    
    name = fields.Char(string="Name")