from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
from .models import Student

import xlrd



def import_func(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        input_excel = request.FILES['myfile']
        
        fs = FileSystemStorage()
        filename = fs.save(input_excel.name, input_excel)
        uploaded_file_url = fs.url(filename)
        
        # name = "test.xls"
        # name = "Talabalar o'qishini ko'chirish (tiklash) jarayonida aniqlangan fanlar farqi bo'yicha ma'lumot.xls"
        # name = "KB - Fanlar farqi bo'yicha ma'lumot (4).xls"
        name = "Fanlar farqi bo'yicha ma'lumot.xls"
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
                    name = cx.split(" ")
                    instance.l_name = name[0]
                    instance.f_name = name[1]
                    instance.m_name = " ".join(i for i in name[2:])
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
                    if id == 1:
                        instance.fan1 = cx
                    if id == 2:
                        instance.fan2 = cx
                    if id == 3:
                        instance.fan3 = cx
                    if id == 4:
                        instance.fan4 = cx
                    if id == 5:
                        instance.fan5 = cx
                    if id == 6:
                        instance.fan6 = cx
                    if id == 7:
                        instance.fan7 = cx
                    if id == 8:
                        instance.fan8 = cx
                    if id == 9:
                        instance.fan9 = cx
                    if id == 10:
                        instance.fan10 = cx
                    if id == 11:
                        instance.fan11 = cx
                    if id == 12:
                        instance.fan12 = cx
                    if id == 13:
                        instance.fan13 = cx
                    if id == 14:
                        instance.fan14 = cx
                    if id == 15:
                        instance.fan15 = cx
                    if id == 16:
                        instance.fan16 = cx
                    if id == 17:
                        instance.fan17 = cx
                    if id == 18:
                        instance.fan18 = cx
                    if id == 19:
                        instance.fan19 = cx
                    if id == 20:
                        instance.fan20 = cx
                    instance.save()
                    
                print(cx)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            "succecc":"Done",
        })
    return render(request, 'simple_upload.html')