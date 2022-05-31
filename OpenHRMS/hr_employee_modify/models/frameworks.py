import string
from odoo import  fields, models, _

class Frameworks(models.Model):
    _name = "frameworks.hr"

    name = fields.Char(string="Framework", required=True)