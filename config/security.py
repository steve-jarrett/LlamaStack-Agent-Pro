# config/security.py

import os
from dotenv import load_dotenv

def load_env_variables():
    """
    Load environment variables from a .env file if present.
    Ensures that API keys and other sensitive information are securely loaded.
    """
    load_dotenv()  # Load variables from .env into environment
    # Validate essential environment variables
    required_vars = ['OPENAI_API_KEY', 'LLAMA_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
