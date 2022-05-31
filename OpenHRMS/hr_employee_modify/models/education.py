from odoo import api, fields, models, _


class Education(models.Model):
    _name = 'education.employee'

    certificates = fields.Selection([
        ('graduate', 'Graduate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctor'),
        ('school', 'School'),
        ('other', 'Other'),
    ], 'Certificate Level', default='other')
    study_fields = fields.Char("Field of Study")
    study_schools = fields.Char("School")
    grades = fields.Integer(string="Grade")
    passing_years = fields.Integer(string="Passing Year")
    employee_id = fields.Many2one('hr.employee', string="Employee", help="Employee")

class Educations_details(models.Model):
    _inherit = 'hr.employee'

    education_details_id = fields.One2many('education.employee', 'employee_id', string="Education Details", help="Employee Educations Details")
