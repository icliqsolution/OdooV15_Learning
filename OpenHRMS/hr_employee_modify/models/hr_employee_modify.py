
from odoo import api, fields, models, _


class EmployeeModify(models.Model):
    _inherit = 'hr.employee'

    technology_id = fields.Many2many("emp.technology_hr",string="Technology")
    frameworks_id = fields.Many2many("frameworks.hr",string="Frameworks")
    tools_id = fields.Many2many("tools.hr",string="Tools")
    database_id = fields.Many2many("database.hr",string="Database")
    deployment_id = fields.Many2many("deployment.tools.hr",string="Deployment Tools")
    version_id = fields.Many2many("version.control.hr",string="Version Control")
    server_id = fields.Many2many("server.hr",string="Server")
    dev_ops_id = fields.Many2many("development.ops.tool.hr",string="Development Ops Tool")
    os_id = fields.Many2many("opeting.system.hr",string="opeting system")
    monitoring_id = fields.Many2many("monitoring.tool.hr",string="Monitoring Tool")
    project_id = fields.Many2many("project.management.hr",string="Project Management")
    other_id = fields.Many2many("other.tools.technologies.hr",string="Other Tools Technologies")
