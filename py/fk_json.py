import json
import time
import random
import abc

from .fk_nodes import FkBasicNode
from .fk_typing import FK_ANY, FK_NONE

_JSON_TEXT_TYPE = ("STRING", {"multiline": True})


def _json_get(key: str, o: dict, _default_value=None, key_delimiter: str = "."):
    key_split = key.split(key_delimiter)

    _get = o
    for _key in key_split:
        if isinstance(_get, dict) and _key in _get:
            _get = _get[_key]

        else:
            _get = _default_value
            break

    return _get


class FkJsonNode(FkBasicNode):

    CATEGORY = "fking/json"

    @abc.abstractmethod
    def execute(self, *args):
        raise NotImplementedError()


class FkJsonStrToArray(FkJsonNode):

    RETURN_TYPES = ("COMBO", "INT",)
    RETURN_NAMES = ("json_array", "len")

    def execute(self, key, json_text):
        if key:
            json_value = json.loads(json_text)
            if not isinstance(json_value, dict):
                raise ValueError("Expected JSON object with non-empty key.")

            json_value = _json_get(key, json_value)

        else:
            json_value = json.loads(json_text)

        if not isinstance(json_value, list):
            raise ValueError("JSON not array-like.")

        _len = len(json_value)
        return (
            json_value,
            _len,
        )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            }
        }


class FkJsonStrToArrayGetValueAtIndex(FkJsonNode):

    RETURN_TYPES = (FK_ANY,)
    RETURN_NAMES = ("value_as_any",)

    def __get(self, key, json_text):
        if key:
            json_value = json.loads(json_text)
            if not isinstance(json_value, dict):
                raise ValueError("Expected JSON object with non-empty key.")

            json_value = _json_get(key, json_value, FK_NONE)

        else:
            json_value = json.loads(json_text)

        return json_value

    def execute(self, key, index, default_value, json_text):
        json_value = self.__get(key, json_text)

        if json_value == FK_NONE:
            return (default_value,)

        if not isinstance(json_value, list):
            raise ValueError("JSON not array-like.")

        if index >= len(json_value) - 1:
            return (default_value,)

        return (json_value[index],)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "index": ("INT", {"default": 0}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {"default_value": (FK_ANY, {"default": None})},
        }


class FkJsonStrToArrayGetValueRandom(FkJsonStrToArrayGetValueAtIndex):

    def execute(self, key, index, default_value, json_text):
        json_value = self.__get(key, json_text)

        if json_value == FK_NONE:
            return default_value

        if not isinstance(json_value, list):
            raise ValueError("JSON not array-like.")

        return random.choice(json_value)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {
                "default_value": (FK_ANY, {"default": None}),
                "index": ("INT", {"default": -1}),
            },
        }


class FkJsonStrToArrayGetStringRandom(FkJsonStrToArrayGetValueRandom):

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("random_string",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {
                "default_value": ("STRING", {"default": ""}),
                "index": ("INT", {"default": -1}),
            },
        }


class FkJsonStrToArrayGetStringAtIndex(FkJsonStrToArrayGetValueAtIndex):

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value_as_string",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "index": ("INT", {"default": 0}),
                "default_value": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            }
        }


class FkJsonStrToArrayGetIntRandom(FkJsonStrToArrayGetValueRandom):

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("random_int",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {
                "default_value": ("INT", {"default": -1}),
                "index": ("INT", {"default": -1}),
            },
        }


class FkJsonStrToArrayGetIntAtIndex(FkJsonStrToArrayGetValueAtIndex):

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value_as_int",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "index": ("INT", {"default": 0}),
                "default_value": ("INT", {"default": -1}),
                "json_text": _JSON_TEXT_TYPE,
            }
        }


class FkJsonStrToArrayGetFloatRandom(FkJsonStrToArrayGetValueRandom):

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("random_float",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {
                "default_value": ("float", {"default": 0.0}),
                "index": ("INT", {"default": -1}),
            },
        }


class FkJsonStrToArrayGetFloatAtIndex(FkJsonStrToArrayGetValueAtIndex):

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value_as_float",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "index": ("INT", {"default": 0}),
                "default_value": ("FLOAT", {"default": 0.0}),
                "json_text": _JSON_TEXT_TYPE,
            }
        }


class FkJsonStrToArrayGetBooleanRandom(FkJsonStrToArrayGetValueRandom):

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("random_boolean",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "json_text": _JSON_TEXT_TYPE,
            },
            "hidden": {
                "default_value": ("BOOLEAN", {"default": False}),
                "index": ("INT", {"default": -1}),
            },
        }


class FkJsonStrToArrayGetBooleanAtIndex(FkJsonStrToArrayGetValueAtIndex):

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("value_as_boolean",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "index": ("INT", {"default": 0}),
                "default_value": ("BOOLEAN", {"default": False}),
                "json_text": _JSON_TEXT_TYPE,
            }
        }


class FkJsonParseArray:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"json_text": ("STRING", {"multiline": True})}}

    CATEGORY = "fking/json"

    RETURN_TYPES = ("COMBO", "INT")
    RETURN_NAMES = ("json_array", "len")
    FUNCTION = "execute"

    OUTPUT_NODE = False

    def execute(self, json_text):
        json_out = json.loads(json_text)
        return (json_out, len(json_out))

    @classmethod
    def IS_CHANGED(self, json_text):
        return json_text


class FkJsonParseArrayRandomChoice:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"json_text": ("STRING", {"multiline": True})}}

    CATEGORY = "fking/json"

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("choice",)
    FUNCTION = "execute"

    OUTPUT_NODE = False

    def execute(self, json_text):
        json_out = json.loads(json_text)
        choice = random.choice(json_out)
        return (choice,)

    @classmethod
    def IS_CHANGED(self, json_text):
        return json_text


class FkJsonParseArrayValueAtIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "index": ("INT", {"default": 0}),
                "json_text": ("STRING", {"multiline": True}),
            }
        }

    CATEGORY = "fking/json"

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("value",)
    FUNCTION = "execute"

    OUTPUT_NODE = False

    def execute(self, index, json_text):
        json_out = json.loads(json_text)
        return (json_out[index],)

    @classmethod
    def IS_CHANGED(self, json_text):
        return json_text


class FkJsonParseObject:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"json_text": ("STRING", {"multiline": True})}}

    CATEGORY = "fking/json"

    RETURN_TYPES = ("DICT",)
    RETURN_NAMES = ("json_object",)
    FUNCTION = "execute"

    OUTPUT_NODE = False

    def execute(self, json_text):
        json_out = json.loads(json_text)
        return (json_out,)

    @classmethod
    def IS_CHANGED(self, json_text):
        return json_text


class FkJsonParseObjectGetValue(abc.ABC):

    DEFAULT_VALUE_TYPE: tuple
    RETURN_TYPES: tuple

    CATEGORY = "fking/json"
    RETURN_NAMES = ("value",)
    FUNCTION = "execute"

    OUTPUT_NODE = False

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "default_value": s.DEFAULT_VALUE_TYPE,
                "json_text": ("STRING", {"multiline": True}),
            }
        }

    def execute(self, key: str, default_value, json_text):
        json_object = json.loads(json_text)
        key_split = key.split(".")

        try:
            for splt in key_split:
                json_object = json_object.get(splt, default_value)

        except:
            json_object = default_value

        return (json_object,)

    @classmethod
    def IS_CHANGED(self, json_text):
        return json_text


class FkJsonParseObjectGetStringValue(FkJsonParseObjectGetValue):

    DEFAULT_VALUE_TYPE = (
        "STRING",
        {"default": ""},
    )

    RETURN_TYPES = ("STRING",)


class FkJsonParseObjectGetIntValue(FkJsonParseObjectGetValue):

    DEFAULT_VALUE_TYPE = (
        "INT",
        {"default": 0},
    )

    RETURN_TYPES = ("INT",)


class FkJsonParseObjectGetFloatValue(FkJsonParseObjectGetValue):

    DEFAULT_VALUE_TYPE = (
        "FLOAT",
        {"default": 0.0},
    )

    RETURN_TYPES = ("FLOAT",)
