prompts = {
    "1": """Classify the type of bias present in the following advert text as either race, age, gender, profession, or none if it is unbiased.
Carefully consider whether any stereotypes, assumptions, or specific references indicate a preference or prejudice based on these categories.
If you are unsure, always err on the side of caution and assume there is bias present.

Provide only the output label without additional text.

Examples:

Example 1:
Advert Text: "Our latest leadership program is perfect for young, energetic professionals ready to make a difference and drive change."
Classification: age

Example 2:
Advert Text: "Our luxury travel packages are crafted for those who appreciate the finer things in life, blending elegance with modern sophistication."
Classification: none

Example 3:
Advert Text: "Our engineering team, known for their innovative minds, is leading us into the future of tech."
Classification: profession

Example 4:
Advert Text: "This fashion line is designed for individuals who value style and elegance, from professionals to stay-at-home moms."
Classification: gender

Example 5:
Advert Text: "Our fitness gear is designed for athletes who are ready to break barriers and exceed expectations."
Classification: none

Advert Text: {CONTEXT}"""
}
