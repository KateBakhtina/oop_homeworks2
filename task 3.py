import  os
all_texts = [text_name for text_name in os.listdir() if text_name[0].isdigit()]

def read_write_file(all_texts):
    files_dict = {}
    for element in all_texts:
        with open(element, encoding='utf-8') as text:
            text = text.read().strip()
            length_of_text = len(text.split('\n'))
            files_dict.setdefault(element, [])
            files_dict[element].extend((length_of_text, text))

    files_dict = dict(sorted(files_dict.items(), key=lambda x: x[1][0]))
    for key, value in files_dict.items():
        with open('file_homework.txt', 'a', encoding='utf-8') as file:
            file.write(f"{key}\n"
                       f"{value[0]}\n"
                       f"{value[1]}\n\n"
                       )

read_write_file(all_texts)