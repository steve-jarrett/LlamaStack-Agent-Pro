# models/steps.py

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from llama_models.schema_utils import json_schema_type

from llama_models.llama3.api.datatypes import CompletionMessage, ToolCall, ToolResponse, SafetyViolation  # Assuming
