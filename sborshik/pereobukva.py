from transliterate import translit
text = 'Съешь ещё этих мягких французских булок, да выпей чаю.'
ru_text = translit(text, 'ru', reversed=True)
ru_text

text = translit('S\'esh\' esche etih mjagkih frantsuzskih bulok, da vypej chaju. Shurshunchik', 'ru')
text

print(ru_text)
print(text)