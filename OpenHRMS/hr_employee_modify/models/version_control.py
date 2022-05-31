import string
from odoo import fields, models, _

class VersionControl(models.Model):
    _name = "version.control.hr"

    name = fields.Char(string="Version Control", required=True)