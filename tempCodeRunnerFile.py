letter = """dear  <|name|>
you are not able to select
is meeting on <|date|>"""
final_letter = letter.replace("<|name|>", "kumar ji").replace("<|date|>", "25 december 2024")
print(final_letter)
