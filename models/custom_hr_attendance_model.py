
from odoo import api, Command, fields, models, tools
from odoo.exceptions import UserError


from odoo.osv.expression import AND, OR
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import AccessError


class HrAttendance(models.Model):
    _inherit = "hr.attendance"
    # _description = "Attendance"
    # _order = "check_in desc"

    late_time = fields.Float(string="Late")
    early_time = fields.Float(string="Early Leave")

    @api.depends('check_out')
    def _compute_early_time(self):
        for attendance in self:
            if attendance.check_out:
                end_time = fields.Datetime.from_string(attendance.check_out).replace(hour=18, minute=30, second=0,
                                                                                     microsecond=0)  # End time is 6:30 PM
                if fields.Datetime.from_string(attendance.check_out) < end_time:
                    early_delta = end_time - fields.Datetime.from_string(attendance.check_out)
                    hours = int(early_delta.total_seconds() // 3600)
                    minutes = int((early_delta.total_seconds() % 3600) // 60)
                    attendance.early_time = hours + minutes / 60.0  # Convert minutes to hours
                else:
                    attendance.early_time = 0.0
            else:
                attendance.early_time = 0.0