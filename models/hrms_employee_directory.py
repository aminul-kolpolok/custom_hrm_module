# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta
import pandas as pd
from pytz import utc
from odoo import models, fields, api, _
from odoo.http import request
from odoo.tools import float_utils

ROUNDING_FACTOR = 16





class HrEmployeePublic(models.Model):
    # _name = 'hr.employee.directory'
    # _name = 'hr.employee.public.inherited'
    _inherit = 'hr.employee.public'



    birthday = fields.Date('Date of Birth', groups="base.group_user",
                           help="Birthday")
    name=fields.Char(string="Employee Manager Name:")
    #------
    joining_date = fields.Date(string="Date of Joining:",
                               help='Date of first Employment fi it was before the start of the ',
                               groups="hr.group_hr_user")  # , readonly=False
    probation_period = fields.Many2one('hr.probation.period', domain=[], string="Probation Period",
                                       groups='hr.group_hr_user')
    conf_due_date = fields.Date(string="Conf. Due Date:", groups='hr.group_hr_user')
    date_of_confirmation = fields.Date(string="Date of Confirmation:", store=True)
    length_of_service = fields.Char(string="Length of service:", groups='hr.group_hr_user')
    section = fields.Many2one('hr.section', string="Section", store="True")
    emp_grade = fields.Many2one('hr.grade', string="Grade", store="True")
    team_name = fields.Many2one('hr.employee.teams', string='Team Name')
    emp_contract_type = fields.Many2one(string="Employee Category", store="True",
                                        related='employee_id.emp_contract_type')
    # leave_manager_id = fields.Many2one(string='Time Off', invisible=True)







