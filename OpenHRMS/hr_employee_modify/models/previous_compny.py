from odoo import api, fields, models, _


class PreviousCompany(models.Model):
    _name = 'previous.company'

    employee_id = fields.Many2one('hr.employee', string="Employee", help="Employee")
    per_company_name = fields.Char(string="Company Name")
    per_company_location = fields.Char(string="Company Location")
    per_start_date = fields.Date(string="Start Date")
    per_end_date = fields.Date(string="End Date")


class InheritCompanyPrevious(models.Model):
    _inherit = 'hr.employee'

    previouscompany_id = fields.One2many('previous.company', 'employee_id', string="Previous Company", help="Previous Company")