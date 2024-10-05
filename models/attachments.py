# models/attachments.py

from typing import Union

from pydantic import BaseModel, Field
from llama_models.schema_utils import json_schema_type

from llama_models.llama3.api.datatypes import InterleavedTextMedia, URL  # Assuming these are defined

@json_schema_type  # Decorator to define JSON schema type for the Attachment class
class Attachment(BaseModel):
    """
    Represents an attachment that can be part of an agent's interaction.

    Attributes:
        content (InterleavedTextMedia | URL): The content of the attachment.
        mime_type (str): The MIME type of the attachment content.
    """
    # The content of the attachment, which can be either InterleavedTextMedia or a URL
    content: Union[InterleavedTextMedia, URL]
    # The MIME type of the attachment content as a string
    mime_type: str
