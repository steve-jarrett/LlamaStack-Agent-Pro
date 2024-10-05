# models/tools.py

from enum import Enum
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field

from llama_models.schema_utils import json_schema_type

from llama_stack.apis.common.deployment_types import RestAPIExecutionConfig  # Assuming this is defined
from llama_models.llama3.api.datatypes import ToolParamDefinition  # Assuming this is defined

class AgentTool(Enum):
    """
    Enum for the different tools that an agent can utilize.

    Attributes:
        brave_search: Represents the Brave search tool.
        wolfram_alpha: Represents the Wolfram Alpha tool.
        photogen: Represents the Photogen tool.
        code_interpreter: Represents a code interpreter tool.
        function_call: Represents a function calling tool.
        memory: Represents a memory tool.
        openai_gpt: Represents the OpenAI GPT tool.
        llama: Represents the Llama tool.
    """
    # Represents the Brave search tool
    brave_search = "brave_search"
    # Represents the Wolfram Alpha tool
    wolfram_alpha = "wolfram_alpha"
    # Represents the Photogen tool
    photogen = "photogen"
    # Represents a code interpreter tool
    code_interpreter = "code_interpreter"
    # Represents a function calling tool
    function_call = "function_call"
    # Represents a memory tool
    memory = "memory"
    # Represents the OpenAI GPT tool
    openai_gpt = "openai_gpt"
    # Represents the Llama tool
    llama = "llama"

class ToolDefinitionCommon(BaseModel):
    """
    Common attributes for all tool definitions.

    Attributes:
        input_shields (Optional[List[str]]): A list of input shields used for filtering input data.
        output_shields (Optional[List[str]]): A list of output shields used for filtering output data.
    """
    # Optional list of input shields with a default empty list
    input_shields: Optional[List[str]] = Field(default_factory=list)
    # Optional list of output shields with a default empty list
    output_shields: Optional[List[str]] = Field(default_factory=list)

class SearchEngineType(Enum):
    """
    Enum for the different search engines available for use in the search tool.

    Attributes:
        bing: Represents the Bing search engine.
        brave: Represents the Brave search engine.
    """
    # Represents the Bing search engine
    bing = "bing"
    # Represents the Brave search engine
    brave = "brave"

@json_schema_type  # Decorator to define JSON schema type for SearchToolDefinition
class SearchToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Search tool used by the agent.

    Attributes:
        type (Literal[AgentTool.brave_search.value]): Type of tool (always brave_search).
        api_key (str): The API key for the search engine.
        engine (SearchEngineType): The search engine to use (default is Brave).
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'brave_search'
    type: Literal[AgentTool.brave_search.value] = AgentTool.brave_search.value
    # The API key required for accessing the search engine
    api_key: str
    # The search engine to use, defaulting to Brave
    engine: SearchEngineType = SearchEngineType.brave
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for WolframAlphaToolDefinition
class WolframAlphaToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Wolfram Alpha tool used by the agent.

    Attributes:
        type (Literal[AgentTool.wolfram_alpha.value]): Type of tool (always wolfram_alpha).
        api_key (str): The API key for Wolfram Alpha.
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'wolfram_alpha'
    type: Literal[AgentTool.wolfram_alpha.value] = AgentTool.wolfram_alpha.value
    # The API key required for accessing Wolfram Alpha
    api_key: str
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for PhotogenToolDefinition
class PhotogenToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Photogen tool used by the agent.

    Attributes:
        type (Literal[AgentTool.photogen.value]): Type of tool (always photogen).
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'photogen'
    type: Literal[AgentTool.photogen.value] = AgentTool.photogen.value
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for CodeInterpreterToolDefinition
class CodeInterpreterToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Code Interpreter tool used by the agent.

    Attributes:
        type (Literal[AgentTool.code_interpreter.value]): Type of tool (always code_interpreter).
        enable_inline_code_execution (bool): Whether to enable inline code execution (default is True).
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'code_interpreter'
    type: Literal[AgentTool.code_interpreter.value] = AgentTool.code_interpreter.value
    # Boolean flag to enable or disable inline code execution, defaulting to True
    enable_inline_code_execution: bool = True
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for FunctionCallToolDefinition
class FunctionCallToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Function Call tool used by the agent.

    Attributes:
        type (Literal[AgentTool.function_call.value]): Type of tool (always function_call).
        function_name (str): The name of the function to be called.
        description (str): A description of the function.
        parameters (Dict[str, ToolParamDefinition]): The parameters required for the function.
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'function_call'
    type: Literal[AgentTool.function_call.value] = AgentTool.function_call.value
    # The name of the function to be called
    function_name: str
    # A description of what the function does
    description: str
    # A dictionary of parameters required for the function, mapping parameter names to their definitions
    parameters: Dict[str, ToolParamDefinition]
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for OpenAIToolDefinition
class OpenAIToolDefinition(ToolDefinitionCommon):
    """
    Definition of the OpenAI GPT tool used by the agent.

    Attributes:
        type (Literal[AgentTool.openai_gpt.value]): Type of tool (always openai_gpt).
        api_key (str): The API key for OpenAI GPT.
        model (str): The OpenAI GPT model to use (default is 'davinci').
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'openai_gpt'
    type: Literal[AgentTool.openai_gpt.value] = AgentTool.openai_gpt.value
    # The API key required for accessing OpenAI GPT
    api_key: str
    # The OpenAI GPT model to use, defaulting to 'davinci'
    model: str = "davinci"
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None

@json_schema_type  # Decorator to define JSON schema type for LlamaToolDefinition
class LlamaToolDefinition(ToolDefinitionCommon):
    """
    Definition of the Llama tool used by the agent.

    Attributes:
        type (Literal[AgentTool.llama.value]): Type of tool (always llama).
        api_key (str): The API key for Llama.
        model (str): The Llama model to use (default is 'llama-2').
        remote_execution (Optional[RestAPIExecutionConfig]): Configuration for executing the tool remotely.
    """
    # The type of tool, fixed to 'llama'
    type: Literal[AgentTool.llama.value] = AgentTool.llama.value
    # The API key required for accessing Llama
    api_key: str
    # The Llama model to use, defaulting to 'llama-2'
    model: str = "llama-2"
    # Optional configuration for remote execution of the tool
    remote_execution: Optional[RestAPIExecutionConfig] = None
