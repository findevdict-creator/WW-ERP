# Wattwisely ERP

Custom Frappe app for Wattwisely, installed on top of ERPNext (Frappe v15).

Current contents: app skeleton, branding (app name, logo, favicon) and the URD system roles.
Replace `wattwisely/public/images/logo.svg` with the real logo (keep the file name).

## Install

```bash
bench get-app https://github.com/findevdict-creator/WW-ERP --branch main
bench --site <site> install-app wattwisely
```

On Frappe Cloud: add this repo as an app to a private bench group, deploy, then install it on the site.

## License

MIT
