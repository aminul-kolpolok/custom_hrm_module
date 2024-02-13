from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta

class HrGrade(models.Model):
    _name = 'hr.grade'
    _description = "HR Grade"

    _inherit = ['mail.thread']
    _order = "name"
    # _rec_name = 'complete_name'

    name = fields.Char('Grade No.')


    note = fields.Text('Note')
    # color = fields.Integer('Color Index')


