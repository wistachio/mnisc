import json
import sys

file = r"C:\Users\jss-e\Downloads\Standard Notes Backup - Sun Jul 03 2022 13 10 49 GMT+0100\Standard Notes Backup and Import File.txt"

f2  = r"C:\Users\jss-e\Downloads\standard_notes.txt"
error_file = r"C:\Users\jss-e\Downloads\errors.txt"


def write_text(text,title=None):
    result = ''
    if title:   result = title + '\n'
    result += text+'\n-------------------------\n\n'
    return result

with open(file, encoding='utf-8') as f:
    data = json.load(f) #dic

error = open(error_file,'a')

with open(f2,'a', encoding='utf-8') as g:

        for notes in data['items']:
            try:
                g.write(write_text(notes['content']['text'], notes['content']['title']))
            except KeyError:
                print('key error')
                try:
                    g.write(write_text((notes['content']['text'])))
                    print(f"Succesfully wrote {notes['content']['text'][:30]}", '\n')
                except:
                    print(notes, '\n')
                
            except Exception as e:
                print('---')
                print(notes['content']['title'])
                error.write(write_text(notes['content']['title']))
                print(e, '\n')

    
error.close()
