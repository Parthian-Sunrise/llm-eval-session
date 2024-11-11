prompts = {
    "1": """Here's the context:
    
    {CONTEXT}

    Classify whether there is any presence of stereotype bias in the context.
    
    The categories are:
    - gender
    - race
    - age
    - profession

    Respond strictly with a single string, e.g. 'gender' if the context contains bias.

    If no bias is found, respond 'none'.
    
    """
}
