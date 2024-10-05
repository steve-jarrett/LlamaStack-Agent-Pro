# main.py

import logging
import os
from typing import List

from models.attachments import Attachment
from models.tools import AgentTool
from services.agent_service import AgentService
from services.metrics_service import MetricsService
from services.tool_selector import ToolSelector
from plugins.openai_client import OpenAIClient
from plugins.llama_client import LlamaClient
from config.security import load_env_variables

def setup_logging():
    """Configure the logging settings."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    """Main function to run the Agentic System."""
    setup_logging()
    load_env_variables()  # Load environment variables securely

    # Initialize MetricsService
    metrics_service = MetricsService()

    # Initialize ToolSelector with MetricsService
    tool_selector = ToolSelector(metrics_service)

    # Initialize API Clients with API keys from environment variables
    openai_client = OpenAIClient(api_key=os.getenv('OPENAI_API_KEY'))
    llama_client = LlamaClient(api_key=os.getenv('LLAMA_API_KEY'))

    # Initialize AgentService with ToolSelector and API clients
    agent_service = AgentService(
        tool_selector=tool_selector,
        openai_client=openai_client,
        llama_client=llama_client
    )

    # Define available tools
    available_tools: List[AgentTool] = [
        AgentTool.openai_gpt,
        AgentTool.llama,
        AgentTool.brave_search,
        AgentTool.wolfram_alpha,
        AgentTool.photogen,
        AgentTool.code_interpreter,
        AgentTool.function_call,
        AgentTool.memory,
    ]

    # Example prompt
    prompt = "Explain the theory of relativity."

    # Manual Mode
    print("=== Manual Mode ===")
    agent_service.set_selection_mode("manual")
    response_manual = agent_service.handle_request(prompt, available_tools)
    print("Manual Mode Response:", response_manual.content)

    # Automated Mode
    print("\n=== Automated Mode ===")
    agent_service.set_selection_mode("automated")
    response_automated = agent_service.handle_request(prompt, available_tools)
    print("Automated Mode Response:", response_automated.content)

if __name__ == "__main__":
    main()
