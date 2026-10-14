app_name = "wattwisely"
app_title = "Wattwisely ERP"
app_publisher = "Wattwisely"
app_description = "Wattwisely ERP: project-supply workflows on Frappe and ERPNext"
app_email = "admin@wattwisely.example"
app_license = "mit"

required_apps = ["erpnext"]

# Branding
# ------------------
# Replace the files in wattwisely/public/images with the real logo (same names)

app_logo_url = "/assets/wattwisely/images/logo.svg"

add_to_apps_screen = [
	{
		"name": "wattwisely",
		"logo": "/assets/wattwisely/images/logo.svg",
		"title": "Wattwisely ERP",
		"route": "/app",
	}
]

website_context = {
	"favicon": "/assets/wattwisely/images/logo.svg",
	"splash_image": "/assets/wattwisely/images/logo.svg",
}

app_include_css = "/assets/wattwisely/css/wattwisely.css"

# Installation
# ------------

after_install = "wattwisely.setup.install.after_install"
after_migrate = "wattwisely.setup.install.after_migrate"
