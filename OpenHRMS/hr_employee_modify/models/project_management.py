from odoo import  fields, models, _


class ProjectManagement(models.Model):
    _name = "project.management.hr"

    name = fields.Char(string="Project Management", required=True)


class OtherTechnology(models.Model):
    _name = "other.tools.technologies.hr"

    name = fields.Char(string="Other Tools & Technologies", required=True)