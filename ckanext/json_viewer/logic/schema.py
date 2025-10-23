from __future__ import annotations

import ckan.plugins.toolkit as tk
from ckan import types
from ckan.logic.schema import validator_args

from ckanext.json_viewer import config


@validator_args
def get_preview_schema(
    unicode_safe: types.Validator,
    default: types.ValidatorFactory,
    one_of: types.ValidatorFactory,
) -> types.Schema:
    return {
        "theme": [
            default(config.get_default_theme()),
            unicode_safe,
            one_of(get_available_themes()),
        ]
    }


def get_available_themes() -> list[str]:
    return [theme["text"] for theme in tk.h.json_viewer_get_theme_options()]
