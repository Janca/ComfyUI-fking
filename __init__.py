from .py.fk_files import *
from .py.fk_text import *
from .py.fk_types import *
from .py.fk_json import *

NODE_CLASS_MAPPINGS = {
    # FILE
    "FkReadFileContentsAsString": FkReadFileContents,
    "FkReadFileGetLineIndexAsString": FkReadFileGetLineIndex,
    # JSON - OBJECT
    "FkJsonParseObject": FkJsonParseObject,
    "FkJsonParseObjectGetStringValue": FkJsonParseObjectGetStringValue,
    "FkJsonParseObjectGetIntValue": FkJsonParseObjectGetIntValue,
    "FkJsonParseObjectGetFloatValue": FkJsonParseObjectGetFloatValue,
    # JSON - ARRAY
    "FkJsonStrToArray": FkJsonStrToArray,
    # JSON - ARRAY - AT INDEX
    "FkJsonStrToArrayGetValueAtIndex": FkJsonStrToArrayGetValueAtIndex,
    "FkJsonStrToArrayGetStringAtIndex": FkJsonStrToArrayGetStringAtIndex,
    "FkJsonStrToArrayGetIntAtIndex": FkJsonStrToArrayGetIntAtIndex,
    "FkJsonStrToArrayGetFloatAtIndex": FkJsonStrToArrayGetFloatAtIndex,
    "FkJsonStrToArrayGetBooleanAtIndex": FkJsonStrToArrayGetBooleanAtIndex,
    # JSON - ARRAY - RANDOM
    "FkJsonStrToArrayGetValueRandom": FkJsonStrToArrayGetValueRandom,
    "FkJsonStrToArrayGetStringRandom": FkJsonStrToArrayGetStringRandom,
    "FkJsonStrToArrayGetIntRandom": FkJsonStrToArrayGetIntRandom,
    "FkJsonStrToArrayGetFloatRandom": FkJsonStrToArrayGetFloatRandom,
    "FkJsonStrToArrayGetBooleanRandom": FkJsonStrToArrayGetBooleanRandom,
    # TEXT
    "FkTextConvertEncoding": FkTextEncode,
    # TYPINGS
    "FkTypeCoerceAnyToString": FkTypeCoerceAnyToString,
    "FkTypeCoerceToAny": FkTypeCoerceToAny,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # FILES
    "FkReadFileContentsAsString": "File: Read Contents",
    "FkReadFileGetLineIndexAsString": "File: Read Line",
    # JSON - Object
    "FkJsonParseObject": "JSON Object",
    "FkJsonParseObjectGetStringValue": "JSON Object: Get Value As String",
    "FkJsonParseObjectGetIntValue": "JSON Object: Get Value As Int",
    "FkJsonParseObjectGetFloatValue": "JSON Object: Get Value As Float",
    # JSON - ARRAY
    "FkJsonStrToArray": "JSON Array",
    # JSON - ARRAY - AT INDEX
    "FkJsonStrToArrayGetValueAtIndex": "JSON Array: Get Value At Index",
    "FkJsonStrToArrayGetStringAtIndex": "JSON Array: Get String At Index",
    "FkJsonStrToArrayGetIntAtIndex": "JSON Array: Get Int At Index",
    "FkJsonStrToArrayGetFloatAtIndex": "JSON Array: Get Float At Index",
    "FkJsonStrToArrayGetBooleanAtIndex": "JSON Array: Get Boolean At Index",
    # JSON - ARRAY - RANDOM
    "FkJsonStrToArrayGetValueRandom": "JSON Array: Random Value",
    "FkJsonStrToArrayGetStringRandom": "JSON Array: Random Value As String",
    "FkJsonStrToArrayGetIntRandom": "JSON Array: Random Value As Int",
    "FkJsonStrToArrayGetFloatRandom": "JSON Array: Random Value As Float",
    "FkJsonStrToArrayGetBooleanRandom": "JSON Array: Random Value As Boolean",
    # TEXT
    "FkTextConvertEncoding": "Text: Convert Encoding",
    # TYPINGS
    "FkTypeCoerceAnyToString": "Coerce Value to String",
    "FkTypeCoerceToAny": "Coerce Value to Any",
}
