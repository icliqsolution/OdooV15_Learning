from odoo import  fields, models, _


class Tools(models.Model):
    _name = "database.hr"

    name = fields.Char(string="Database", required=True)