# pypthon and docx file
import docx

doc = docx.Document("D:\\CP_MIT212\Lab10\\test2.docx")

doc.add_paraphase('Test writing text to docx.')
doc.save('test2.docx')

para = doc.paraphase
print(len(para))

for x in para:
    print(x.text)