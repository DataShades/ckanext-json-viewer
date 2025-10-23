from typing import Any

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan import types
from ckan.common import CKANConfig

import ckanext.resourceproxy.plugin as proxy
from ckanext.json_viewer import config
from ckanext.json_viewer.logic.schema import get_preview_schema


@tk.blanket.helpers
@tk.blanket.config_declarations
class JsonViewerPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IResourceView, inherit=True)

    # IConfigurer

    def update_config(self, config_: CKANConfig):
        tk.add_template_directory(config_, "templates")
        tk.add_resource("assets", "json_viewer")

    # IResourceView

    def info(self) -> dict[str, Any]:
        return {
            "name": "json_viewer",
            "title": "JSON Viewer",
            "icon": "fa fa-code",
            "iframed": False,
            "default_description": "Preview JSON data as a tree structure.",
            "schema": get_preview_schema(),
            "always_available": True,
            "default_title": config.get_default_view_name(),
        }

    def can_view(self, data_dict: dict[str, Any]) -> bool:
        return data_dict["resource"].get("format", "").lower() == "json"

    def setup_template_variables(self, context: types.Context, data_dict: dict[str, Any]):
        return {"resource_url": proxy.get_proxified_resource_url(data_dict)}

    def view_template(self, context: types.Context, data_dict: dict[str, Any]):
        return "json_view.html"

    def form_template(self, context: types.Context, data_dict: dict[str, Any]):
        return "json_form.html"
