from odoo import  fields, models

class Bank_details(models.Model):
    _inherit = "res.partner.bank"

    branch = fields.Char(string="Branch Name")
    ifsc = fields.Char(string="IFSC Code") 
    pan_number = fields.Char(string="PAN Number")  