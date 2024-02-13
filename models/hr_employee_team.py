from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta

class HRTeams(models.Model):
    _name = 'hr.employee.teams'
    _description = "HR Employee Teams"

    _inherit = ['mail.thread']
    _order = "name"
    # _rec_name = 'complete_name'

    name = fields.Char('Team Name', required=True)
    # complete_name = fields.Char('Complete Name', compute='_compute_complete_name', store=True)
    active = fields.Boolean('Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
    # parent_id = fields.Many2one('hr.department', string='Parent Department', index=True,
    #                             domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    # child_ids = fields.One2many('hr.department', 'parent_id', string='Child Departments')
    manager_id = fields.Many2one('hr.employee', string='Manager', tracking=True,
                                 domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    # member_ids = fields.One2many('hr.employee', 'department_id', string='Members', readonly=True)
    # jobs_ids = fields.One2many('hr.job', 'department_id', string='Jobs')
    note = fields.Text('Note')
    color = fields.Integer('Color Index')


