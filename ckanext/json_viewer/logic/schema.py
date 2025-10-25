from __future__ import annotations

import ckan.plugins.toolkit as tk
from ckan import types
from ckan.logic.schema import validator_args

from ckanext.json_viewer.config import ExtConfig


@validator_args
def get_preview_schema(  # noqa: PLR0913
    unicode_safe: types.Validator,
    default: types.ValidatorFactory,
    one_of: types.ValidatorFactory,
    int_validator: types.Validator,
    is_positive_integer: types.Validator,
    boolean_validator: types.Validator,
) -> types.Schema:
    return {
        "theme": [
            default(ExtConfig.get_default_theme()),
            unicode_safe,
            one_of(get_available_themes()),
        ],
        "max_height": [
            default(ExtConfig.get_default_max_height()),
            int_validator,
            is_positive_integer,
        ],
        "expand": [default(ExtConfig.get_default_expand()), boolean_validator],
        "indentation": [
            default(ExtConfig.get_default_indentation()),
            int_validator,
            is_positive_integer,
        ],
        "show_data_types": [
            default(ExtConfig.get_default_show_data_types()),
            boolean_validator,
        ],
        "show_toolbar": [
            default(ExtConfig.get_default_show_toolbar()),
            boolean_validator,
        ],
        "show_copy_button": [
            default(ExtConfig.get_default_show_copy_button()),
            boolean_validator,
        ],
        "show_sizes": [default(ExtConfig.get_default_show_sizes()), boolean_validator],
    }


def get_available_themes() -> list[str]:
    return [theme["text"] for theme in tk.h.json_viewer_get_theme_options()]
