from openai import OpenAI
from local_variables import token

client = OpenAI(api_key=token)


def generate_outputs_openai(system_prompt):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
        ],
    )

    return response.choices[0].message.content
