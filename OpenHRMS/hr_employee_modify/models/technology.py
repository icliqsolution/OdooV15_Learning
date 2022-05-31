from odoo import  fields, models, _


class technology_hr(models.Model):
    _name= "emp.technology_hr"
    

    name = fields.Char(string="Technology", required=True)