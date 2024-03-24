from odoo import fields, models, api


class AllAttendanceReport(models.AbstractModel):
    _name = 'report.custom_hrm_module.employee_details_report_template'
    _description = 'Employee Attendance Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        employee_id = data.get('employee_id')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Construct the SQL query
        query = """
            SELECT *
            FROM hr_attendance
            WHERE employee_id = %s
        """
        params = [employee_id]

        if start_date and end_date:
            # Add conditions for start and end date
            query += " AND (check_in >= %s OR check_out <= %s)"
            params.extend([start_date, end_date])

        # Execute the SQL query
        self.env.cr.execute(query, params)
        result = self.env.cr.dictfetchall()

        return {
            'docs': result,
            'start_date': start_date,
            'end_date': end_date,
        }
