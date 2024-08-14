from .fk_typing import FK_ANY, FK_NONE

class FkTypeCoerceAnyToString:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"value": (FK_ANY,)}}

    CATEGORY = "fking/types"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value_as_string",)
    FUNCTION = "execute"

    OUTPUT_NODE = False

    def execute(self, value):
        return (str(value),)

    @classmethod
    def IS_CHANGED(self, value):
        return str(value)

class FkTypeCoerceToAny:
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required":{"value":(FK_ANY,)}}
    
    CATEGORY = "fking/types"
    
    RETURN_TYPES = (FK_ANY,)
    RETURN_NAMES = ("value_as_any",)
    FUNCTION = "execute"
    
    OUTPUT_NODE = False
    
    def execute(self, value):
        return (value,)
    
    @classmethod
    def IS_CHANGED(self, value):
        return str(value)
