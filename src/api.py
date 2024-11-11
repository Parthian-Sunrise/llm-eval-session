import openai
from openai import OpenAI
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from config import settings


def get_openai_client():
    """
    Validate OpenAI token and generate OpenAI client if valid token exists.

    Returns:
        client: OpenAI client
    """

    if settings.api_key == "":
        raise ValueError(
            """Invalid OpenAI token. If you are running locally, please make sure you replace the placeholder
            with the actual api key in the .env file."""
        )

    client = OpenAI(api_key=settings.api_key)
    return client


def log_attempt_number(retry_state):
    """
    Print the retry attempt number.

    Args:
        retry_state: tenacity retry state

    """
    print("Retrying: %s", retry_state.attempt_number)


@retry(
    wait=wait_exponential(min=4),
    retry=retry_if_exception_type(openai.RateLimitError),
    stop=stop_after_attempt(5),
    after=log_attempt_number,
)
def generate_outputs_openai(system_prompt: str = None):
    """
    Generate OpenAI response with given system prompt.

    Args:
        system_prompt: system prompt used to generate OpenAi response.

    Returns:
        response: OpenAI response
    """

    client = get_openai_client()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
        ],
    )

    return response.choices[0].message.content
