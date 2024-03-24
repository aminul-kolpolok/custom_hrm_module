from odoo import fields, models, api
from datetime import datetime

class EmployeeAttendanceReport(models.TransientModel):
    _name = 'hr.attendance.report.wizard'
    _description = 'Print Employee Attendance Wizard Report'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    start_date = fields.Date(string="From")
    end_date = fields.Date(string="To")
    report_date = fields.Datetime(string="Report Date.", default=lambda _ : datetime.today(), readonly=True)



    def action_btn_attendance_report_info(self):
        data = {
            'employee_id': self.employee_id.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }
        return self.env.ref('custom_hrm_module.attendance_details_report_action').report_action(self, data=data)



