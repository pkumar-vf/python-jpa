# app/meta.py
from typing import Any, Dict
from pydantic import BaseModel as PydanticModel, ConfigDict
from bson import ObjectId

# defaults you want applied to every document model
DEFAULT_DOCUMENT_CONFIG: Dict[str, Any] = {
    "populate_by_name": True,
    "arbitrary_types_allowed": True,
    "json_encoders": {ObjectId: str},
}

# Pydantic's metaclass
PydanticMeta = type(PydanticModel)

class DocumentMeta(PydanticMeta):
    def __new__(mcls, name, bases, namespace, **kwargs):
        existing = dict(namespace.get("model_config", {}) or {})
        merged = {**DEFAULT_DOCUMENT_CONFIG, **existing}
        namespace["model_config"] = ConfigDict(**merged)
        return super().__new__(mcls, name, bases, namespace, **kwargs)
