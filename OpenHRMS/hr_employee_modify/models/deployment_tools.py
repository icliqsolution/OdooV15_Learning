import string
from odoo import fields, models, _

class DeploymentTools(models.Model):
    _name = "deployment.tools.hr"

    name = fields.Char(string="Deploymen Tools", required=True)