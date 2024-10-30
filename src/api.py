from openai import OpenAI
from local_variables import token


def get_openai_client():
    """
    Validate OpenAI token and generate OpenAI client if valid token exists.

    Returns:
        client: OpenAI client
    """

    if token == "":
        raise ValueError(
            "Invalid OpenAI token. Please make sure you replace the placeholder with the actual token."
        )
    else:
        client = OpenAI(api_key=token)
        return client


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
