from odoo import  fields, models, _


class DevelopmentOpsTool(models.Model):
    _name = "development.ops.tool.hr"

    name = fields.Char(string="Development Tool", required=True)