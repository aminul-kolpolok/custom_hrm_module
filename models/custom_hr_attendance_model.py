
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
