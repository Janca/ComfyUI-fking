import os

from .fk_nodes import FkBasicNode
from .fk_typing import FK_SUPPORTED_ENCODINGS


class FkFileNode(FkBasicNode):

    CATEGORY = "fking/files"


class FkReadFileContents(FkFileNode):

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = "file_as_string"

    def execute(self, file_path, encoding, errors, clean_whitespace):
        file_contents: str
        with open(file_path, "r", encoding=encoding, errors=errors) as f:
            file_contents = f.read()

        if clean_whitespace:
            file_contents = file_contents.strip()

        return (file_contents,)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
                "encoding": (FK_SUPPORTED_ENCODINGS, {"default": "utf-8"}),
                "errors": (
                    ["strict", "ignore", "replace"],
                    {"default": "strict"},
                ),
                "clean_whitespace": ("BOOLEAN", {"default": True}),
            }
        }


class FkReadFileGetLineIndex(FkFileNode):

    CATEGORY = "fking/files"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("line_as_string",)

    def execute(
        self, line_index, file_path, encoding, errors, clean_whitespace, default_value
    ):
        file_contents: str

        if default_value:
            default_value = default_value.strip()

        if not os.path.exists(file_path) and errors == "ignore":
            return (default_value,)

        try:
            with open(file_path, "r", encoding=encoding, errors=errors) as f:
                file_contents = f.read()

        except Exception as e:
            if errors != "ignore":
                raise e

            return (default_value,)

        if clean_whitespace:
            file_contents = file_contents.strip()

        file_lines = file_contents.splitlines()
        if line_index >= len(file_lines):
            return (default_value,)

        return (file_lines[line_index],)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "line_index": ("INT", {"default": 0}),
                "default_value": ("STRING", {"default": ""}),
                "file_path": ("STRING", {"default": ""}),
                "encoding": (FK_SUPPORTED_ENCODINGS, {"default": "utf-8"}),
                "errors": (
                    ["strict", "ignore", "replace"],
                    {"default": "strict"},
                ),
                "clean_whitespace": ("BOOLEAN", {"default": True}),
            }
        }
