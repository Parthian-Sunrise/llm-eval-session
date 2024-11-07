error_prompts = {
    "brevity": "You should make the text unnecessarily verbose and excede any sensible word limit when summarising",
    "hallucination": "You must introduce some false information not present in the text",
    "formatting": "You must awkwardly format dates or numbers in the text using incorrect or bohemian approaches",
    "coverage": "You must purposefully not cover a key factual element of the text in your summary",
    "fluency": "You must purposefully making some grammatical and spelling mistakes in the text, but do not make these too jarring",
}

unerror_prompts = {
    "brevity": "You should make a concise and direct summary without unnecessary tangents or diversions, try to keep to a short word limit of 100-200 words",
    "hallucination": "The text must not contain any hallucinations. DO NOT HALLUCINATE!",
    "formatting": "Format all dates as DD/MM/YYYY and numbers in the general foramt x,xxx.xx",
    "fluency": "Do not make any spelling or grammatical mistakes",
    "coverage": "Make sure to cover all important facts of the article.",
}
