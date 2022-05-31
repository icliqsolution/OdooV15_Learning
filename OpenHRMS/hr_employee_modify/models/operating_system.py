from odoo import  fields, models, _


class DevelopmentOpsTool(models.Model):
    _name = "opeting.system.hr"

    name = fields.Char(string="Opeting System", required=True)