app_name = "arm_accounting"
app_title = "Accounting_ARM "
app_publisher = "Sync"
app_description = "full accounting and finance system with reports and insights "
app_email = "nafaelhadi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "arm_accounting",
# 		"logo": "/assets/arm_accounting/logo.png",
# 		"title": "Accounting_ARM ",
# 		"route": "/arm_accounting",
# 		"has_permission": "arm_accounting.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/arm_accounting/css/arm_accounting.css"
# app_include_js = "/assets/arm_accounting/js/arm_accounting.js"

# include js, css files in header of web template
# web_include_css = "/assets/arm_accounting/css/arm_accounting.css"
# web_include_js = "/assets/arm_accounting/js/arm_accounting.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "arm_accounting/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "arm_accounting/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "arm_accounting.utils.jinja_methods",
# 	"filters": "arm_accounting.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "arm_accounting.install.before_install"
# after_install = "arm_accounting.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "arm_accounting.uninstall.before_uninstall"
# after_uninstall = "arm_accounting.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "arm_accounting.utils.before_app_install"
# after_app_install = "arm_accounting.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "arm_accounting.utils.before_app_uninstall"
# after_app_uninstall = "arm_accounting.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "arm_accounting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"arm_accounting.tasks.all"
# 	],
# 	"daily": [
# 		"arm_accounting.tasks.daily"
# 	],
# 	"hourly": [
# 		"arm_accounting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"arm_accounting.tasks.weekly"
# 	],
# 	"monthly": [
# 		"arm_accounting.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "arm_accounting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "arm_accounting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "arm_accounting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["arm_accounting.utils.before_request"]
# after_request = ["arm_accounting.utils.after_request"]

# Job Events
# ----------
# before_job = ["arm_accounting.utils.before_job"]
# after_job = ["arm_accounting.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"arm_accounting.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["module", "in", ["Accounting_ARM"]]
        ]
    },
    {
        "dt": "Property Setter",
        "filters": [
            ["doc_type", "in", ["Account", "POS Invoice", "Purchase Invoice", "Sales Invoice"]]
        ]
    },
    {
        "dt": "Workspace",
        "filters": [
            ["name", "in", ["المحاسبة", "ايرادات", "مصروفات"]]
        ]
    },
    {
        "dt": "Client Script",
        "filters": [
            ["module", "in", ["Accounting_ARM"]]
        ]
    },
    {
        "dt": "Server Script",
        "filters": [
            ["module", "in", ["Accounting_ARM"]]
        ]
    },
    {
        "dt": "Custom HTML Block",
        "filters": [
            ["name", "in", ["ARM-Welcome card"]]
        ]
    },
    {
        "dt": "Print Format",
        "filters": [
            ["name", "in", ["ARM Standard Invoice", "ARM_Print_format"]]
        ]
    },
    {
        "dt": "Number Card",
        "filters": [
            ["name", "in", ["صافي دخل المشاريع", "اجمالي مبيعات ", "الذمم المدينة", "الذمم الدائنة", "عهد الموظفين", "إجمالي المصاريف التشغيلية الشهرية"]]
        ]
    },
    {
        "dt": "Dashboard Chart",
        "filters": [
            ["name", "in", ["تكلفة المشاريع", "مقارنة المبيعات الشهرية", "المصاريف حسب النوع", "الارباح و الخسائر"]]
        ]
    },
    {
        "dt": "Report",
        "filters": [
            ["name", "in", ["Purchase Register", "Sales Register", "تقرير ارباح المشاريع", "Cash Flow", "Accounts Payable", "General Ledger", "Trial Balance (Simple)", "Customer Ledger Summary", "Project Profitability", "Bank Reconciliation Statement", "Accounts Receivable Summary", "Balance Sheet", "Profit and Loss Statement", "Trial Balance"]]
        ]
    }
]


