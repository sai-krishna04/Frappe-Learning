app_name = "library_mgmt"
app_title = "Library App"
app_publisher = "Krish"
app_description = "Library management System"
app_email = "krish@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []
override_doctype_dashboards = {
    "Students": "library_mgmt.library_app.doctype.students.student_dashboard.get_data"
}
# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_mgmt",
# 		"logo": "/assets/library_mgmt/logo.png",
# 		"title": "Library App",
# 		"route": "/library_mgmt",
# 		"has_permission": "library_mgmt.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_mgmt/css/library_mgmt.css"
# app_include_js = "/assets/library_mgmt/js/library_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_mgmt/css/library_mgmt.css"
# web_include_js = "/assets/library_mgmt/js/library_mgmt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_mgmt/public/scss/website"

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
# app_include_icons = "library_mgmt/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_mgmt.utils.jinja_methods",
# 	"filters": "library_mgmt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_mgmt.install.before_install"
# after_install = "library_mgmt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_mgmt.uninstall.before_uninstall"
# after_uninstall = "library_mgmt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_mgmt.utils.before_app_install"
# after_app_install = "library_mgmt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_mgmt.utils.before_app_uninstall"
# after_app_uninstall = "library_mgmt.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "library_mgmt.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_mgmt.notifications.get_notification_config"

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
# 		"library_mgmt.tasks.all"
# 	],
# 	"daily": [
# 		"library_mgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_mgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_mgmt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_mgmt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_mgmt.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "library_mgmt.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_mgmt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_mgmt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_mgmt.utils.before_request"]
# after_request = ["library_mgmt.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_mgmt.utils.before_job"]
# after_job = ["library_mgmt.utils.after_job"]

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
# 	"library_mgmt.auth.validate"
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

