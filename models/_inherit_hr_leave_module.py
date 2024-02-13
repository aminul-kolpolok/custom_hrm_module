

from odoo import api, Command, fields, models, tools
from odoo.exceptions import UserError


class HolidaysRequest(models.Model):
    _inherit = "hr.leave"



    leave_apply_date = fields.Date(
        string="Leave Apply Date",
        readonly=True,
        default=fields.Date.today,
        help='This field is readonly and will be set to the current date automatically.'
    )

    responsible_id = fields.Many2one(
        'res.users', 'Responsible Time Off Officer',
        domain=lambda self: [('groups_id', 'in', self.env.ref('hr_holidays.group_hr_holidays_user').id)],
        help="Choose the Time Off Officer who will be notified to approve allocation or Time Off request")
    # manager_id = fields.Many2one('hr.employee', store=True, readonly=False)
    employee_id = fields.Many2one('hr.employee', string='Related Employee', ondelete='cascade',
                                  help="Employee-related data of the user", required=True)

    # @api.constrains('state', 'number_of_days', 'holiday_status_id')
    # def _check_holidays(self):
    #     for holiday in self:
    #         mapped_days = self.holiday_status_id.get_employees_days(
    #             (holiday.employee_id | holiday.sudo().employee_ids).ids, holiday.date_from.date())
    #         if holiday.holiday_type != 'employee' \
    #                 or not holiday.employee_id and not holiday.sudo().employee_ids \
    #                 or holiday.holiday_status_id.requires_allocation == 'no':
    #             continue
    #         if holiday.employee_id:
    #             leave_days = mapped_days[holiday.employee_id.id][holiday.holiday_status_id.id]
    #             if float_compare(leave_days['remaining_leaves'], 0, precision_digits=2) == -1 \
    #                     or float_compare(leave_days['virtual_remaining_leaves'], 0, precision_digits=2) == -1:
    #                 raise ValidationError(
    #                     _('The number of remaining time off is not sufficient for this time off type.\n'
    #                       'Please also check the time off waiting for validation.'))
    #         else:
    #             unallocated_employees = []
    #             for employee in holiday.sudo().employee_ids:
    #                 leave_days = mapped_days[employee.id][holiday.holiday_status_id.id]
    #                 if float_compare(leave_days['remaining_leaves'], self.number_of_days, precision_digits=2) == -1 \
    #                         or float_compare(leave_days['virtual_remaining_leaves'], self.number_of_days,
    #                                          precision_digits=2) == -1:
    #                     unallocated_employees.append(employee.name)
    #             if unallocated_employees:
    #                 raise ValidationError(
    #                     _('The number of remaining time off is not sufficient for this time off type.\n'
    #                       'Please also check the time off waiting for validation.')
    #                     + _('\nThe employees that lack allocation days are:\n%s',
    #                         (', '.join(unallocated_employees))))




    # def _check_approval_update(self, state):
    #     """ Check if target state is achievable. """
    #     if self.env.is_superuser():
    #         return
    #
    #     current_employee = self.env.user.employee_id
    #     is_officer = self.env.user.has_group('hr_holidays.group_hr_holidays_user')
    #     is_manager = self.env.user.has_group('hr_holidays.group_hr_holidays_manager')
    #
    #     for holiday in self:
    #         val_type = holiday.validation_type
    #
    #         if not is_manager and state != 'confirm':
    #
    #             # Additional check for validating
    #             if state == 'validate' and val_type == 'officer':
    #                 raise UserError(_('You must be the Responsible Time Off Officer to approve this leave'))
    #
    #             # Additional check for officer disallowance
    #             if state in ('validate1', 'validate', 'refuse') and val_type == 'officer' and is_officer:
    #                 raise UserError(
    #                     _('Officers are not allowed to approve/refuse leaves. Please contact your HR Manager.'))