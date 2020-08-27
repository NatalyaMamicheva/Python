from googletrans import Translator
translator = Translator()

with open("text_4.txt", 'r', encoding="utf-8") as f_obj:
    lines = f_obj.readlines()
    result = translator.translate(''.join(lines), src='en', dest='ru')

with open('text_4_2.txt', 'w') as file_obj_2:
    file_obj_2.writelines(result.text)