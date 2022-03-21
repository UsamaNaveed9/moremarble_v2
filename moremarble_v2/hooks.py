# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "moremarble_v2"
app_title = "Moremarble V2"
app_publisher = "Usama Naveed"
app_description = "Moremarble V2"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "usamanaveed9263@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/moremarble_v2/css/moremarble_v2.css"
# app_include_js = "/assets/moremarble_v2/js/moremarble_v2.js"

# include js, css files in header of web template
# web_include_css = "/assets/moremarble_v2/css/moremarble_v2.css"
# web_include_js = "/assets/moremarble_v2/js/moremarble_v2.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "moremarble_v2/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "moremarble_v2.install.before_install"
# after_install = "moremarble_v2.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "moremarble_v2.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"moremarble_v2.tasks.all"
# 	],
# 	"daily": [
# 		"moremarble_v2.tasks.daily"
# 	],
# 	"hourly": [
# 		"moremarble_v2.tasks.hourly"
# 	],
# 	"weekly": [
# 		"moremarble_v2.tasks.weekly"
# 	]
# 	"monthly": [
# 		"moremarble_v2.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "moremarble_v2.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "moremarble_v2.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "moremarble_v2.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

