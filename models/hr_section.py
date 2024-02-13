from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta

class HrSection(models.Model):
    _name = 'hr.section'
    _description = "HR Section"

    _inherit = ['mail.thread']
    _order = "name"
    # _rec_name = 'complete_name'

    name = fields.Char('Section Name')


    note = fields.Text('Note')
    # color = fields.Integer('Color Index')


