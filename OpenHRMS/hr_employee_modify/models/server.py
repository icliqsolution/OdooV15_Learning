from odoo import  fields, models, _


class Server(models.Model):
    _name = "server.hr"

    name = fields.Char(string="Server", required=True)