import io

from .fk_nodes import FkBasicNode
from .fk_typing import FK_SUPPORTED_ENCODINGS


class FkTextEncode(FkBasicNode):

    CATEGORY = "fking/text"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("encoded_string",)

    def execute(self, string: str, encoding, errors):
        encoded_string = string.encode(encoding=encoding, errors=errors)\
            .decode(encoding=encoding)
            
        return (encoded_string,)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"default": ""}),
                "encoding": (FK_SUPPORTED_ENCODINGS, {"default": "utf-8"}),
                "errors": (
                    ["strict", "ignore", "replace"],
                    {"default": "strict"},
                ),
            },
        }
