# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2022-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Aswani PC (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': "Open HRMS - HR Employee Directory",
    'version': '16.0.1.0.1',
    'summary': """Open HRMS - HR Employee Directory""",
    'description': """Open HRMS - HR Directory""",
    'category': 'Generic Modules/Human Resources',
    'live_test_url': 'https://youtu.be/XwGGvZbv6sc',
    'author': 'Cybrosys Techno solutions,Open HRMS',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['base','hr','hr_holidays','stock'],
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
        # 'views/org_chart_views.xml',
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
