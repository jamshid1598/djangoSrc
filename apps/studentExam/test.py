import xlrd
book = xlrd.open_workbook("exam-data/test.xls")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(1, sh.nrows):
    for idx, cx in enumerate(sh.row(rx)):
        cx = str(cx)
        if idx == 0:
            cx = int(float(cx.replace("number:", "")))
        if idx == 1:
            cx = cx.replace("text:", "")
            cx = cx.strip('\"')
            cx = cx.strip('\'')
            name = cx.split(" ")
            print(name)
        if idx == 2:
            cx = cx.replace("text:", "'")
            cx = cx.strip('\"')
            cx = cx.strip('\'')
        if idx == 3:
            cx = cx.replace("text:", "")
            cx = cx.strip('\"')
            cx = cx.strip('\'')
        if idx == 4:
            cx = cx.replace("text:", "")
            cx = cx.strip('\"')
            cx = cx.strip('\'')
        if idx == 5:
            cx = cx.replace("text:", "")
            cx = cx.strip('\"')
            cx = cx.strip('\'')
        print(cx)
    # print(sh.row(rx))
    if rx == 5:
        break