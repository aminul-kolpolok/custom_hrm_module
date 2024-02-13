from datetime import timedelta

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _


class HrEmployeePrivate(models.Model):
    _inherit = "res.users"

    leave_manager_id = fields.Many2one(string="Time off")