# LlamaStack-Agent-Pro
A fork of LlamaAgent to enable the management of many AI mdoels and to make tradeoffs between cost, latency, quality, and CO2 impact.

# Agentic System
Overview
The Agentic System is a flexible and scalable framework designed to manage interactions between agents and various AI tools, including Large Language Models (LLMs) like OpenAI's GPT and Llama AI, as well as other specialized AI services such as Brave Search and Wolfram Alpha. This system intelligently assigns tasks to the most suitable tool based on dynamic metrics including cost, latency, response quality, and CO₂ impact, promoting both efficiency and sustainability.

# Features
Dynamic Tool Selection: Automatically or manually select the optimal AI tool for each task based on real-time metrics.
Scalable Plugin Architecture: Easily add new AI tools and services with minimal changes to the core system.
Comprehensive Metrics Tracking: Monitor and evaluate cost, latency, quality, and CO₂ impact for each tool.
Manual and Automated Modes: Provide developers with the flexibility to choose tools manually or let the system make intelligent selections automatically.
Robust Error Handling: Gracefully handle API failures and other potential errors to ensure system reliability.
Secure Configuration: Safeguard API keys and sensitive information using environment variables and secure loading mechanisms.

# File Structure
agentic_system/
├── main.py
├── config/
│   ├── __init__.py
│   └── security.py
├── models/
│   ├── __init__.py
│   ├── attachments.py
│   ├── tools.py
│   ├── memory_banks.py
│   └── steps.py
├── services/
│   ├── __init__.py
│   ├── metrics_service.py
│   ├── agent_service.py
│   └── tool_selector.py
├── plugins/
│   ├── __init__.py
│   ├── openai_client.py
│   └── llama_client.py
├── utils/
│   ├── __init__.py
│   └── error_handling.py
├── tests/
│   ├── __init__.py
│   ├── test_metrics_service.py
│   ├── test_tool_selector.py
│   └── test_agent_service.py
└── docs/
    └── README.md



# Modules Description
main.py: The entry point of the application. Initializes services, configures logging, and demonstrates usage in both manual and automated modes.

config/

security.py: Handles the secure loading of environment variables, ensuring API keys and other sensitive information are managed safely.
models/

attachments.py: Defines the Attachment model representing media attachments in agent interactions.
tools.py: Contains the AgentTool enum and ToolDefinitionCommon base class, along with specific tool configurations.
memory_banks.py: Defines configurations for various types of memory banks (vector, key-value, keyword, graph) used by agents.
steps.py: (Assumed) Defines different steps involved in an agent's action sequence, such as inference, tool execution, shield calls, and memory retrieval.
services/

metrics_service.py: Implements the MetricsService class responsible for retrieving and managing dynamic metrics for each tool.
agent_service.py: Manages the overall agent behavior, orchestrating tool selection and execution based on configurations.
tool_selector.py: Contains the ToolSelector class that handles the logic for selecting the best tool, either manually or automatically.
plugins/

openai_client.py: Implements the OpenAIClient class to interact with OpenAI's GPT API.
llama_client.py: Implements the LlamaClient class to interact with Llama AI's API.
utils/

error_handling.py: (Assumed) Provides utilities for robust error handling across the system.
tests/

test_metrics_service.py: Unit tests for the MetricsService.
test_tool_selector.py: Unit tests for the ToolSelector.
test_agent_service.py: Unit and integration tests for the AgentService.
docs/

README.md: Contains detailed documentation and usage instructions for the system.
# Installation
# Prerequisites
Python 3.8 or higher
pip package manager
Steps
Clone the Repository

bash
git clone https://github.com/yourusername/agentic_system.git
cd agentic_system
Create a Virtual Environment

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the root directory and add your API keys:

env
OPENAI_API_KEY=your_openai_api_key
LLAMA_API_KEY=your_llama_api_key
Configuration
Environment Variables
The system relies on environment variables to securely manage API keys and other sensitive information.

OPENAI_API_KEY: Your OpenAI API key.
LLAMA_API_KEY: Your Llama AI API key.
Ensure that these variables are set in your environment or defined in a .env file in the project's root directory.

# Selection Modes
The Agentic System supports two selection modes for choosing tools:

# Manual Mode: Developers are presented with the metrics of each available tool and can manually select the desired tool.
Automated Mode: The system automatically selects the best tool based on predefined heuristics that consider cost, latency, quality, and CO₂ impact. The selection decision is logged for transparency.
You can switch between modes by setting the selection mode in the AgentService:

python
agent_service.set_selection_mode("manual")  # or "automated"
Usage
Running the Application
To run the application and see both manual and automated tool selection in action:

bash
python main.py

# Example Output
=== Manual Mode ===
Tool: openai_gpt
  Cost: $0.03
  Latency: 0.65s
  Quality: 0.95
  CO2 Impact: 0.000600kg

Tool: llama
  Cost: $0.025
  Latency: 0.55s
  Quality: 0.90
  CO2 Impact: 0.000550kg

...

Select a tool by typing its name: openai_gpt
Manual Mode Response: [Model response]

# Automated Mode 
Automated selection: llama
Automated Mode Response: [Model response]
Integrating with Your Application
You can integrate the Agentic System into your application by initializing the necessary services and using the AgentService to handle requests.

python
from services.agent_service import AgentService
from services.metrics_service import MetricsService
from services.tool_selector import ToolSelector
from plugins.openai_client import OpenAIClient
from plugins.llama_client import LlamaClient
from models.tools import AgentTool

# Initialize services
metrics_service = MetricsService()
tool_selector = ToolSelector(metrics_service)
openai_client = OpenAIClient(api_key="your_openai_api_key")
llama_client = LlamaClient(api_key="your_llama_api_key")

# Initialize AgentService
agent_service = AgentService(
    tool_selector=tool_selector,
    openai_client=openai_client,
    llama_client=llama_client
)

# Define available tools
available_tools = [
    AgentTool.openai_gpt,
    AgentTool.llama,
    AgentTool.brave_search,
    # Add other tools as needed
]

# Handle a request
prompt = "Explain the theory of relativity."
response = agent_service.handle_request(prompt, available_tools)
print(response.content)
Architecture
Modular Design
The Agentic System is designed with a modular architecture, where each module encapsulates specific functionalities:

# Models: Define the data structures and enums used across the system.
Services: Implement core functionalities such as metrics tracking, tool selection, and agent orchestration.
Plugins: Provide integrations with external AI services like OpenAI and Llama.
Config: Manage configurations and security aspects, ensuring sensitive information is handled securely.
Utils: Offer utility functions and error handling mechanisms.
Tests: Contain unit and integration tests to ensure system reliability and correctness.
Plugin Architecture
The system supports a plugin-based architecture, allowing for easy addition of new tools without modifying the core codebase. Each new tool should implement the ToolPlugin protocol, ensuring consistency and compatibility with the AgentService.

# Metrics Tracking
The MetricsService dynamically retrieves and manages metrics for each tool, enabling informed decision-making during tool selection. Metrics include:

Cost: Estimated cost per request.
Latency: Time taken to receive a response from the tool.
Quality: Quality score of the response.
CO₂ Impact: Estimated carbon footprint of the request.
Tool Selection Logic
The ToolSelector class handles the logic for selecting the best tool based on the current mode:

# Manual Mode: Presents metrics to developers for manual selection.
Automated Mode: Uses a heuristic to select the optimal tool, prioritizing cost and CO₂ impact while maximizing quality.
Security
Sensitive information, such as API keys, is managed securely through environment variables. The config/security.py module ensures that essential environment variables are loaded and validated at startup.

# Testing
Unit Tests
Unit tests ensure that individual components function as expected. They are located in the tests/ directory and cover services like MetricsService, ToolSelector, and AgentService.

Integration Tests
Integration tests verify that different modules interact correctly. These tests simulate real-world scenarios, ensuring that tool selection and execution workflows operate seamlessly.

# Running Tests
To run the tests, navigate to the project directory and execute:

bash
ytest tests/
Ensure that all tests pass to confirm the system's reliability.

Contributing
Contributions are welcome! To contribute to the Agentic System:

Fork the Repository

Create a Feature Branch

bashgit checkout -b feature/your-feature-name
Commit Your Changes

bash
git commit -m "Add your feature"
Push to the Branch

bash
git push origin feature/your-feature-name
Open a Pull Request

Please ensure that your contributions adhere to the project's coding standards and include appropriate tests and documentation.

# License
This project is licensed under the MIT License.

# Acknowledgements
OpenAI for providing powerful language models.
Llama AI for their innovative AI solutions.
Pydantic for data validation and management.
Requests library for simplifying HTTP requests.
Python community for continuous support and development resources.

# Error Handling
Robust error handling is implemented across the system to gracefully manage API failures and other unexpected issues. Errors are logged appropriately to aid in debugging and system monitoring.

# Sample app in compare_tools.py

Explanation of the Sample Application
Imports and Setup:

Standard Libraries: For handling environment variables, logging, and HTTP requests.
Custom Modules: Importing services, models, plugins, and configuration modules from the agentic_system package.
Function: setup_logging:

Configures the logging format and level to ensure that all important information and errors are logged appropriately.
Function: get_available_tools:

Returns a list containing the AgentTool enums for OpenAI GPT and Llama. This can be extended to include more tools as needed.
Function: main:

Step 1: Initializes logging.
Step 2: Loads environment variables securely. If essential variables are missing, it logs an error and exits.
Step 3: Initializes the MetricsService to handle metric retrieval.
Step 4: Initializes the ToolSelector with the MetricsService.
Step 5: Retrieves API keys from environment variables and initializes the respective API clients. Logs an error and exits if keys are missing.
Step 6: Initializes the AgentService, which orchestrates tool selection and execution.
Step 7: Defines the available tools for comparison.
Step 8: Prompts the user to input a query. Exits if no input is provided.
Step 9: Iterates over each available tool, executes the query, measures latency, retrieves metrics, and stores the results. Handles any exceptions during execution.
Step 10: Displays the responses from each tool and a tabulated comparison of the metrics.
Execution:

When the script is run, it executes the main function, facilitating user interaction and displaying comparative metrics.

# Running the Sample Application
1. Ensure Environment Variables are Set
Before running the application, ensure that your environment variables for OPENAI_API_KEY and LLAMA_API_KEY are set. You can set them in your terminal session or define them in a .env file at the root of your project.

Example .env File:
OPENAI_API_KEY=your_openai_api_key_here
LLAMA_API_KEY=your_llama_api_key_here

2. Install Dependencies
Ensure all required Python packages are installed. If you have a requirements.txt file, you can install dependencies using:

pip install -r requirements.txt
If you don't have a requirements.txt, ensure you have the necessary packages installed:

pip install pydantic requests python-dotenv
3. Run the Sample Application
Execute the compare_tools.py script:

python compare_tools.py
4. Follow the Prompts
The application will prompt you to enter a query. After entering your query, it will process the request using both OpenAI GPT and Llama, then display the responses along with a comparison of the metrics.
