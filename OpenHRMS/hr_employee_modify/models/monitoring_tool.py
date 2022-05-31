from odoo import  fields, models, _


class MonitoringTool(models.Model):
    _name = "monitoring.tool.hr"

    name = fields.Char(string="Monitoring Tool", required=True)