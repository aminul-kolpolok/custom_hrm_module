
from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo import fields, models



class HrEmployeeKpi(models.Model):
    _name = 'employee.kpi'
    _inherit = "hr.attendance"



    def _default_employee(self):
        return self.env.user.employee_id

    employee_id = fields.Many2one('hr.employee', string="Employee", default=_default_employee, required=True,
                                  ondelete='cascade', index=True)
    department_id = fields.Many2one('hr.department', string="Department", related="employee_id.department_id",
                                    readonly=True)
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string="Check Out")
    worked_hours = fields.Float(string='Worked Hours', store=True, readonly=True)




    # @api.depends('check_in', 'check_out')
    # def _compute_worked_hours(self):
    #     for attendance in self:
    #         if attendance.check_out and attendance.check_in:
    #             delta = attendance.check_out - attendance.check_in
    #             attendance.worked_hours = delta.total_seconds() / 3600.0
    #         else:
    #             attendance.worked_hours = False