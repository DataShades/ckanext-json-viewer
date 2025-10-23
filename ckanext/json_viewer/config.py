import ckan.plugins.toolkit as tk

CONF_DEFAULT_THEME = "ckanext.json_viewer.default_theme"
CONF_DEFAULT_VIEW_NAME = "ckanext.json_viewer.default_view_name"
CONF_DEFAULT_DESCRIPTION = "ckanext.json_viewer.default_description"


def get_default_theme() -> str:
    return tk.config[CONF_DEFAULT_THEME]


def get_default_view_name() -> str:
    return tk.config[CONF_DEFAULT_VIEW_NAME]


def get_default_description() -> str:
    return tk.config[CONF_DEFAULT_DESCRIPTION]
