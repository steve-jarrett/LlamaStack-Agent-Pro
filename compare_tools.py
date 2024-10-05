# compare_tools.py

import os  # For accessing environment variables
import logging  # For logging information and errors
from typing import List

from services.metrics_service import MetricsService  # Service to retrieve tool metrics
from services.tool_selector import ToolSelector  # Service to select tools based on metrics
from plugins.openai_client import OpenAIClient  # Client to interact with OpenAI GPT
from plugins.llama_client import LlamaClient  # Client to interact with Llama AI
from models.tools import AgentTool  # Enum of available tools
from config.security import load_env_variables  # Function to load environment variables securely

def setup_logging():
    """
    Configure the logging settings for the application.
    Logs are displayed with timestamp, logger name, log level, and message.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def get_available_tools() -> List[AgentTool]:
    """
    Define and return the list of available tools for comparison.
    
    Returns:
        List[AgentTool]: A list containing AgentTool enums for OpenAI GPT and Llama.
    """
    return [
        AgentTool.openai_gpt,
        AgentTool.llama,
    ]

def main():
    """
    Main function to run the sample application.
    
    It performs the following steps:
    1. Sets up logging.
    2. Loads environment variables securely.
    3. Initializes services and clients.
    4. Prompts the user for a query.
    5. Processes the query using both OpenAI GPT and Llama.
    6. Retrieves and compares metrics.
    7. Displays the comparison to the user.
    """
    # Step 1: Set up logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Step 2: Load environment variables securely
    try:
        load_env_variables()
    except EnvironmentError as e:
        logger.error(f"Environment configuration error: {e}")
        return
    
    # Step 3: Initialize MetricsService
    metrics_service = MetricsService()
    
    # Step 4: Initialize ToolSelector with MetricsService
    tool_selector = ToolSelector(metrics_service)
    
    # Step 5: Initialize API Clients with API keys from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    llama_api_key = os.getenv('LLAMA_API_KEY')
    
    if not openai_api_key or not llama_api_key:
        logger.error("API keys for OpenAI or Llama are not set in environment variables.")
        return
    
    openai_client = OpenAIClient(api_key=openai_api_key)
    llama_client = LlamaClient(api_key=llama_api_key)
    
    # Step 6: Initialize AgentService with ToolSelector and API clients
    from services.agent_service import AgentService  # Import here to avoid circular imports
    agent_service = AgentService(
        tool_selector=tool_selector,
        openai_client=openai_client,
        llama_client=llama_client
    )
    
    # Step 7: Define available tools
    available_tools = get_available_tools()
    
    # Step 8: Prompt the user for a query
    user_query = input("Enter your query to describe: ").strip()
    if not user_query:
        logger.error("No query entered. Exiting application.")
        return
    
    # Step 9: Execute the query using both tools and collect metrics
    results = {}
    metrics = {}
    
    for tool in available_tools:
        try:
            # Record the start time for latency measurement
            start_time = time.time()
            
            # Execute the query using the respective tool
            if tool == AgentTool.openai_gpt:
                response = openai_client.execute(prompt=user_query)
            elif tool == AgentTool.llama:
                response = llama_client.execute(prompt=user_query)
            else:
                logger.warning(f"Tool {tool.value} is not supported in this comparison.")
                continue
            
            # Calculate latency
            latency = time.time() - start_time
            
            # Retrieve metrics from MetricsService
            tool_metrics = metrics_service.get_metrics(tool)
            
            # Update latency in metrics
            tool_metrics.latency = latency
            
            # Store the response and metrics
            results[tool.value] = response.content
            metrics[tool.value] = tool_metrics
            
        except Exception as e:
            logger.error(f"Error executing tool {tool.value}: {e}")
            continue
    
    # Step 10: Display the results and metrics comparison
    if not results:
        logger.error("No successful tool executions to compare.")
        return
    
    print("\n=== Query Results ===")
    for tool_name, content in results.items():
        print(f"\n-- {tool_name.upper()} --")
        print(content)
    
    print("\n=== Metrics Comparison ===")
    print(f"{'Tool':<15}{'Cost ($)':<10}{'Latency (s)':<12}{'Quality':<10}{'CO2 Impact (kg)':<15}")
    print("-" * 62)
    for tool_name, metric in metrics.items()
