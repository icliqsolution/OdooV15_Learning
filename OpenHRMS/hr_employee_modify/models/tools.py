from odoo import  fields, models, _


class Tools(models.Model):
    _name = "tools.hr"

    name = fields.Char(string="Tools", required=True)