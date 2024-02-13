
from odoo import models, fields, api
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = "res.users"
    # _inherits = 'hr.employee.teams'
    EMERGENCY_RELATION_OPTIONS = [
        ('spouse', 'Spouse'),
        ('parent', 'Parent'),
        ('sibling', 'Sibling'),
        ('friend', 'Friend'),
        ('other', 'Other'),
    ]

    employee_id = fields.Many2one('hr.employee', string='Related Employee', ondelete='cascade', help="Employee-related data of the user", required=True)
    leave_manager_id = fields.Many2one(related='employee_id.leave_manager_id')
    joining_date = fields.Date(related='employee_id.joining_date', string="Date of Joining", readonly=False)
    probation_period = fields.Many2one(related='employee_id.probation_period', string="Probation Period")
    date_of_confirmation = fields.Date(string="Date of Confirmation:", related='employee_id.date_of_confirmation')
    conf_due_date = fields.Date(related='employee_id.conf_due_date', string="Conf. Due Date")
    emergency_address = fields.Char(string="Em. Contact", related='employee_id.emergency_address')
    emergency_relation = fields.Selection(
        selection=EMERGENCY_RELATION_OPTIONS,
        string='Emergency Relation',
        help='Select the emergency relation',
        related='employee_id.emergency_relation'
    )

    team_name = fields.Many2one(string='Team Name', related="employee_id.team_name")


    department_id = fields.Many2one(string="Department", related="employee_id.department_id")
    emp_grade = fields.Many2one(string="Grade", related="employee_id.emp_grade")
    section = fields.Many2one(string="Section", related="employee_id.emp_grade")
    tax_id = fields.Char(string="Tin No.", related='employee_id.tax_id')
    # expense_manager_id = fields.Many2one('res.users', invisible=True)

