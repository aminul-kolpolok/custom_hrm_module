from datetime import timedelta

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _


class HrEmployeePrivate(models.Model):

    _inherit = "hr.employee"
    EMERGENCY_RELATION_OPTIONS = [
        ('spouse', 'Spouse'),
        ('parent', 'Parent'),
        ('sibling', 'Sibling'),
        ('father', 'Father'),
        ('friend', 'Friend'),
        ('brother', 'Brother'),
        ('elder_brother', 'Elder Brother'),
        ('wife', 'wife'),
        ('mother', 'Mother'),
        ('sister', 'Sister'),
        ('cousin', 'Cousin'),
        ('elder_sister', 'Elder Sister'),
        ('other', 'Other'),
    ]

    # employee_type_id = fields.Many2one('hr.employee.type', string="Employment Type", readonly=True)
    joining_date = fields.Date(string="Date of Joining:",
                               help='Date of first Employment fi it was before the start of the ',
                               groups="hr.group_hr_user", readonly=False) #, readonly=False
    probation_period = fields.Many2one('hr.probation.period', domain=[], string="Probation Period", groups='hr.group_hr_user')
    conf_due_date = fields.Date(string="Conf. Due Date:", groups='hr.group_hr_user')
    # joining_date = fields.Date(string="Joining date.", groups='hr.group_hr_user', store="True", readonly=False)
    date_of_confirmation = fields.Date(string="Date of Confirmation:", store=True)
    length_of_service = fields.Char(string="Length of service:", groups='hr.group_hr_user')
    forecasting_confirmation = fields.Date("Forecasting Confirmation", groups="hr.group_hr_user",
                                           help="Forecasting confirmation")
    employee_id = fields.Char(string="Employee Id", store="True")
    #---
    section = fields.Many2one('hr.section', string="Section", store="True")
    emp_grade = fields.Many2one('hr.grade', string="Grade", store="True")
    emp_contract_type = fields.Many2one('hr.contract.type', string="Employee Category", store="True")

    join_designation = fields.Char(string="Join Designation")
    mobile_personal = fields.Char(string="Mobile (personal)")
    tax_id = fields.Char(string="Tin No.")
    private_email = fields.Char(string="Personal Email", readonly=False, store=True)
    phone = fields.Char(string="Private Phone", readonly=False, store=True)
    present_address = fields.Char(string="Present Address.", readonly=False, store=True)
    #---
    emergency_address = fields.Char(string="Em. Contact")
    emergency_relation = fields.Selection(
        selection=EMERGENCY_RELATION_OPTIONS,
        string='Emergency Relation',
        help='Select the emergency relation',
    )
    team_name = fields.Many2one('hr.employee.teams', string='Team Name')



    @api.onchange('joining_date', 'probation_period') # This function is used for the calcualte probation period date!
    def _get_end_date(self):
        for et in self:
            if et.joining_date and et.probation_period:
                joining_date = et.joining_date
                if et.probation_period.unit == 'years':
                    conf_due_date = joining_date + relativedelta(years=et.probation_period.length)
                elif et.probation_period.unit == 'months':
                    conf_due_date = joining_date + relativedelta(months=et.probation_period.length)
                elif et.probation_period.unit == 'days':
                    conf_due_date = joining_date + relativedelta(days=et.probation_period.length)
                elif et.probation_period.unit == 'weeks':
                    conf_due_date = joining_date + relativedelta(weeks=et.probation_period.length)
                else:
                    conf_due_date = joining_date + relativedelta(days=et.probation_period.length)

                # Subtract one day from the calculated confirmation due date
                conf_due_date -= timedelta(days=1)

                et.conf_due_date = conf_due_date.strftime("%Y-%m-%d")
                et.forecasting_confirmation = conf_due_date.strftime("%Y-%m-%d")
            else:
                et.conf_due_date = None
                et.forecasting_confirmation = None