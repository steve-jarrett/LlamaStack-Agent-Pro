
# models/memory_banks.py

from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from llama_models.schema_utils import json_schema_type
from llama_stack.apis.memory import MemoryBank  # Assuming this is defined

class MemoryBankType(Enum):
    """
    Enum for different types of memory banks.

    Attributes:
        vector: Represents a vector-based memory bank.
        keyvalue: Represents a key-value-based memory bank.
        keyword: Represents a keyword-based memory bank.
        graph: Represents a graph-based memory bank.
    """
    vector = "vector"
    keyvalue = "keyvalue"
    keyword = "keyword"
    graph = "graph"

class _MemoryBankConfigCommon(BaseModel):
    """
    Common attributes for all memory bank configurations.

    Attributes:
        bank_id (str): The identifier for the memory bank.
    """
    # The unique identifier for the memory bank
    bank_id: str

class AgentVectorMemoryBankConfig(_MemoryBankConfigCommon):
    """
    Configuration for a vector-based memory bank.

    Attributes:
        type (Literal[MemoryBankType.vector.value]): The type of memory bank (vector).
    """
    # The type of memory bank, fixed to 'vector'
    type: Literal[MemoryBankType.vector.value] = MemoryBankType.vector.value

class AgentKeyValueMemoryBankConfig(_MemoryBankConfigCommon):
    """
    Configuration for a key-value-based memory bank.

    Attributes:
        type (Literal[MemoryBankType.keyvalue.value]): The type of memory bank (key-value).
        keys (List[str]): List of keys to focus on for storing memory.
    """
    # The type of memory bank, fixed to 'keyvalue'
    type: Literal[MemoryBankType.keyvalue.value] = MemoryBankType.keyvalue.value
    # List of keys that the memory bank will focus on for storing memory
    keys: List[str]

class AgentKeywordMemoryBankConfig(_MemoryBankConfigCommon):
    """
    Configuration for a keyword-based memory bank.

    Attributes:
        type (Literal[MemoryBankType.keyword.value]): The type of memory bank (keyword).
    """
    # The type of memory bank, fixed to 'keyword'
    type: Literal[MemoryBankType.keyword.value] = MemoryBankType.keyword.value

class AgentGraphMemoryBankConfig(_MemoryBankConfigCommon):
    """
    Configuration for a graph-based memory bank.

    Attributes:
        type (Literal[MemoryBankType.graph.value]): The type of memory bank (graph).
        entities (List[str]): List of entities to focus on in the memory bank.
    """
    # The type of memory bank, fixed to 'graph'
    type: Literal[MemoryBankType.graph.value] = MemoryBankType.graph.value
    # List of entities that the graph-based memory bank will focus on
    entities: List[str]

# Unified MemoryBankConfig with support for multiple memory bank types
MemoryBankConfig = Annotated[
    Union[
        AgentVectorMemoryBankConfig,          # Vector-based memory bank configuration
        AgentKeyValueMemoryBankConfig,        # Key-value-based memory bank configuration
        AgentKeywordMemoryBankConfig,         # Keyword-based memory bank configuration
        AgentGraphMemoryBankConfig,           # Graph-based memory bank configuration
    ],
    Field(discriminator="type"),  # Use the 'type' field to discriminate between different configurations
]
