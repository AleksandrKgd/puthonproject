"""ДЗ"""
"""Задание 1
Дан текстовый файл. Необходимо создать новый файл
убрав из него все неприемлемые слова. Список неприемлемых слов находится в другом файле."""
from logging import exception

#открываем файл text.txt для добовления текста и даём псевдоним myFaile:



# with open("text.txt","r+") as myFile:
#     myFile.write("aiogram os os os aiogram os")
#     with open("text1.txt","r+") as myFile1:
#         myFile1.write(" os ")
#
#         with open("text.txt", "r+") as myFile:
#             myFile_string = myFile.read()
#             print(myFile_string)
#             with open("text1.txt", "r+") as myFile1:
#                 myFile1_string = myFile1.read()
#                 print(myFile1_string)
#                 myFile_list = myFile_string.split(" ")
#                 print(myFile_list)
#                 myFile1_list = myFile1_string.split(" ")
#                 print(myFile1_list)
#                 myFile2_list=[] #список заполненый нужными словами
#                 #прошли циклом по файлу text.txt и если слова нет в файле
#                 #text1.txt то добавляем его в новый файл
#                 for i in myFile_list:
#                     #есть ли слово исключение в списке
#                     if i !=myFile1_list[1]:
#                         myFile2_list.append(i)
#                 print(f"Список с нужными словами:{myFile2_list}")
#                 with open("text2.txt","w+") as myFile2:
#                     for i in range(0,len(myFile2_list)):
#                         myFile2.writelines(myFile2_list[i])
#                         myFile2.write(" ")
#


"""Задание 1
Дан текстовый файл. Подсчитать количество символов в нём."""
with open("text.txt","r+") as myFile:
    myFile.write("aiogram os os os aiogram os")
    myFile.seek(0)
    content =myFile.read()
    print(f"{len(content)}")

"""Задание 2
Дан текстовый файл. Подсчитать количество строк
в нём."""
with open("text3.txt","r+") as myFile3:
    myFile3.write("aiogram os os \n os aiogram os")
    #myFile.seek(0)
    list1 = myFile3.readlines()
    print(f"{len(list1)}")

"""Задание 3
Дан списка строк. Записать их в файл, расположив
каждый элемент списка на отдельной строке с сохранением порядка
"""
with open("text4.txt","r+") as myFile4:
    myFile4.write("aiogram os os os aiogram os")

    myFile4_string=myFile4.readline()
    print(myFile4_string)
    myFile4_list=myFile4_string.split(" ")
    print(myFile4_list)

    with open("text5.txt", "w+") as myFile5:

        for i in range(0, len(myFile4_list)):
           myFile5.writelines(myFile4_list[i])
           myFile5.write("\n")


"""Задание 4
Дан текстовый файл. Добавить в него строку из
двенадцати звездочек (************), поместив ее после последней
строки, в которых нет запятой. Если таких строк нет,
то новая строка должна быть добавлена после всех строк
имеющегося файла. Результат записать в другой файл.
'''"""
list1=["\n*************"]
with open("text6.txt","w") as myFile6:
    myFile6.write("aiogram os os ,os aiogram os")
    myFile6.writelines(list1)










































