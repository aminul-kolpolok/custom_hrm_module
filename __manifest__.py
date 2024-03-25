# -*- coding: utf-8 -*-
{
    'name': "Kolpolok HRMS - Employee Directory",
    'version': '16.0.1.0.1',
    'summary': """Kolpolok HRMS - HR Employee Directory""",
    'description': """Kolpolok HRMS - HR Directory""",
    'category': 'Generic Modules/Human Resources',
    'live_test_url': 'https://youtu.be/XwGGvZbv6sc',
    'author': 'Kolpolok Technologies, HRMS',
    'company': 'Kolpolok Techno Solutions',
    'maintainer': 'Kolpolok Techno Solutions',
    # 'website': "https://www.openhrms.com",
    'depends': ['base', 'hr', 'hr_holidays', 'stock', 'hr_attendance'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [
        'security/ir.model.access.csv',
        # 'report/broadfactor.xml',
        'views/hrms_employee_directory.xml',
        'views/probation_period_views.xml',
        'views/inherit_employees_base_field.xml',
        # 'views/inherit_user_access.xml',
        'views/inherit_user_profile_data.xml',
        'views/inherit_hr_leave_form_update.xml',
        'views/_inherit_leave_allocation.xml',
        'views/hr_emp_teams_views.xml',
        'views/hr_section.xml',
        'views/hr_emp_grade.xml',
        'views/leave_balance_report.xml',
        'chart_views/show_employee_chart.xml',
        'views/hr_attendence_inherited_view.xml',
        'views/rename_manu_view.xml',
        'report/attendance_report_wizard.xml',
        'report/report_view.xml',
        'report/employee_attendance_report_format.xml',
        # KPI xml file added here....,
        # 'kpi_views/kpi_form_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_hrm_module/static/src/js/organizational_view.js',
            'custom_hrm_module/static/src/scss/chart_view.scss',
            'custom_hrm_module/static/src/xml/chart_view.xml',

        ],
    },

    'images': ["static/description/banner.png"],
    'license': "AGPL-3",
    'installable': True,
    'application': True,

}
