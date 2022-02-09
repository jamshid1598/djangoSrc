from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
from .models import Student, TestDB

import xlrd


def read_txt(request):
    file1 = open('/home/jamshid/Documents/django/djangoSrc/apps/studentExam/exam-data/English.txt', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        if line.startswith("25"):
            line = line.replace("25", " ")
            print("savol: ", line.strip())
            q = TestDB(q=line)
        if line.startswith("A."):
            line = line.replace("A.", " ")
            print("A:", line.strip())
            q.a=line
        if line.startswith("B."):
            line = line.replace("B.", " ")
            print("B:", line.strip())
            q.b=line
        if line.startswith("C."):
            line = line.replace("C.", " ")
            print("C:", line.strip())
            q.c=line
        if line.startswith("D."):
            line = line.replace("D.", " ")
            print("D:", line.strip())
            q.d=line
            q.save()
    return HttpResponse("success")


def import_func(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        input_excel = request.FILES['myfile']
        
        fs = FileSystemStorage()
        filename = fs.save(input_excel.name, input_excel)
        uploaded_file_url = fs.url(filename)
        
        # name = "test.xls"
        # name = "Talabalar o'qishini ko'chirish (tiklash) jarayonida aniqlangan fanlar farqi bo'yicha ma'lumot.xls"
        # name = "KB - Fanlar farqi bo'yicha ma'lumot (4).xls"
        # name = "Fanlar farqi bo'yicha ma'lumot.xls"
        name = "iqtisodiyot_fanlar_farqi.xls"
        file_name = f"/home/jamshid/Documents/django/djangoSrc/apps/studentExam/exam-data/{name}"
        book = xlrd.open_workbook(file_name) # file_contents=input_excel.read(), encoding_override = 'utf8'
        # print("The number of worksheets is {0}".format(book.nsheets))
        # print("Worksheet name(s): {0}".format(book.sheet_names()))
        sh = book.sheet_by_index(0)
        # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
        instance = None
        for rx in range(1, sh.nrows):
            id = None
            for idx, cx in enumerate(sh.row(rx)):
                cx = str(cx)
                if idx == 0:
                    cx = int(float(cx.replace("number:", "")))
                    id = cx
                    if cx == 1:
                        instance = Student()
                if idx == 1 and id == 1:
                    cx = cx.replace("text:", "")
                    cx = cx.strip('\"')
                    cx = cx.strip('\'')
                    # name = cx.split(" ")
                    # instance.l_name = name[0]
                    # instance.f_name = name[1]
                    # instance.m_name = " ".join(i for i in name[2:])
                    instance.full_name = cx
                if idx == 2 and id == 1:
                    cx = cx.replace("text:", "")
                    cx = cx.strip('\"')
                    cx = cx.strip('\'')
                    instance.direction = cx
                if idx == 3 and id == 1:
                    cx = cx.replace("text:", "")
                    cx = cx.strip('\"')
                    cx = cx.strip('\'')
                    instance.group = cx
                if idx == 4 and id == 1:
                    cx = cx.replace("text:", "")
                    cx = cx.strip('\"')
                    cx = cx.strip('\'')
                    instance.group = instance.group + " " + cx
                
                if idx == 5:
                    cx = cx.replace("text:", "")
                    cx = cx.strip('\"')
                    cx = cx.strip('\'')
                    # if id in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] and 'Kurs' not in cx:
                    #     if not instance.fan1:
                    #         instance.fan1 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan2:
                    #         instance.fan2 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan3:
                    #         instance.fan3 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan4:
                    #         instance.fan4 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan5:
                    #         instance.fan5 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan6:
                    #         instance.fan6 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan7:
                    #         instance.fan7 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan8:
                    #         instance.fan8 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan9:
                    #         instance.fan9 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan10:
                    #         instance.fan10 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan11:
                    #         instance.fan11 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan12:
                    #         instance.fan12 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan13:
                    #         instance.fan13 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan14:
                    #         instance.fan14 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan15:
                    #         instance.fan15 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan16:
                    #         instance.fan16 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan17:
                    #         instance.fan17 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan18:
                    #         instance.fan18 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan19:
                    #         instance.fan19 = cx
                    #         instance.subject_count = instance.subject_count + 1
                    #     if not instance.fan20:
                    #         instance.fan20 = cx
                    #         instance.subject_count = instance.subject_count + 1
                        
                            
                    if id == 1 and 'Kurs' not in cx:
                        instance.fan1 = cx
                        instance.subject_count += 1
                    if id == 2 and 'Kurs' not in cx:
                        instance.fan2 = cx
                        instance.subject_count += 1
                    if id == 3 and 'Kurs' not in cx:
                        instance.fan3 = cx
                        instance.subject_count += 1
                    if id == 4 and 'Kurs' not in cx:
                        instance.fan4 = cx
                        instance.subject_count += 1
                    if id == 5 and 'Kurs' not in cx:
                        instance.fan5 = cx
                        instance.subject_count += 1
                    if id == 6 and 'Kurs' not in cx:
                        instance.fan6 = cx
                        instance.subject_count += 1
                    if id == 7 and 'Kurs' not in cx:
                        instance.fan7 = cx
                        instance.subject_count += 1
                    if id == 8 and 'Kurs' not in cx:
                        instance.fan8 = cx
                        instance.subject_count += 1
                    if id == 9 and 'Kurs' not in cx:
                        instance.fan9 = cx
                        instance.subject_count += 1
                    if id == 10 and 'Kurs' not in cx:
                        instance.fan10 = cx
                        instance.subject_count += 1
                    if id == 11 and 'Kurs' not in cx:
                        instance.fan11 = cx
                        instance.subject_count += 1
                    if id == 12 and 'Kurs' not in cx:
                        instance.fan12 = cx
                        instance.subject_count += 1
                    if id == 13 and 'Kurs' not in cx:
                        instance.fan13 = cx
                        instance.subject_count += 1
                    if id == 14 and 'Kurs' not in cx:
                        instance.fan14 = cx
                        instance.subject_count += 1
                    if id == 15 and 'Kurs' not in cx:
                        instance.fan15 = cx
                        instance.subject_count += 1
                    if id == 16 and 'Kurs' not in cx:
                        instance.fan16 = cx
                        instance.subject_count += 1
                    if id == 17 and 'Kurs' not in cx:
                        instance.fan17 = cx
                        instance.subject_count += 1
                    if id == 18 and 'Kurs' not in cx:
                        instance.fan18 = cx
                        instance.subject_count += 1
                    if id == 19 and 'Kurs' not in cx:
                        instance.fan19 = cx
                        instance.subject_count += 1
                    if id == 20 and 'Kurs' not in cx:
                        instance.fan20 = cx
                        instance.subject_count += 1
                    instance.save()
                    
                print(cx)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            "succecc":"Done",
        })
    return render(request, 'simple_upload.html')