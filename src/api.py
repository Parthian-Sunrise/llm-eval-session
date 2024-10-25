from openai import OpenAI
from local_variables import token

client = OpenAI(api_key=token)


def generate_outputs_openai(system_prompt, context, response):

    template_values = {"CONTEXT": context, "RESPONSE": response}

    system_content = system_prompt.format(**template_values)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_content},
        ],
    )

    return response.choices[0].message.content
