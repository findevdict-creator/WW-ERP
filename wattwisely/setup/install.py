import frappe

APP_NAME = "Wattwisely ERP"

# System roles from the URD (section 3.2). Permissions are assigned per DocType.
ROLES = (
	"Director",
	"Pre-Bidding Lead",
	"Pre-Bidding Engineer",
	"Post-Bidding Lead",
	"Project Engineer",
	"Project Costing",
	"Quality Lead",
	"QC Inspector",
	"Finance Lead",
	"Accountant",
	"Auditor",
)


def after_install():
	create_roles()
	apply_branding()


def after_migrate():
	# Branding is only applied on install so changes made later in the UI are kept
	create_roles()


def create_roles():
	for role_name in ROLES:
		if not frappe.db.exists("Role", role_name):
			frappe.get_doc({"doctype": "Role", "role_name": role_name, "desk_access": 1}).insert(
				ignore_permissions=True
			)


def apply_branding():
	logo = "/assets/wattwisely/images/logo.svg"
	frappe.db.set_single_value("Website Settings", "app_name", APP_NAME)
	frappe.db.set_single_value("Website Settings", "app_logo", logo)
	frappe.db.set_single_value("Website Settings", "favicon", logo)
	frappe.db.set_single_value("System Settings", "app_name", APP_NAME)
	frappe.db.set_single_value("Navbar Settings", "app_logo", logo)
