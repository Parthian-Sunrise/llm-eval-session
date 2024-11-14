error_prompts = {
    "brevity": "You should make the text unnecessarily verbose and occassionally pompous, use more passive language and excede any sensible word limit when summarising",
    "hallucination": "You must introduce some false information not present in the text",
    "formatting": "You must awkwardly format dates or numbers in the text using incorrect or bohemian approaches",
    "coverage": "You MUST purposefully NOT cover a key factual element of the text in your summary",
    "fluency": "You MUST purposefully make some grammatical and spelling MISTAKES in the text",
}

unerror_prompts = {
    "brevity": "You MUST make a concise and direct summary without unnecessary tangents or diversions, try to keep to a short word limit of 100-200 words",
    "hallucination": "The text must not contain any hallucinations. DO NOT HALLUCINATE!",
    "formatting": "Format all dates as DD/MM/YYYY and numbers in the general foramt x,xxx.xx",
    "fluency": "Do NOT make any spelling or grammatical mistakes",
    "coverage": "Make sure to cover all important facts of the article and do not miss any.",
}
