import xlwt



def main():
    nums = [43664, 43634, 43054, 43459, 43758, 42912, 42226, 42646, 42944, 42858, 43091, 43095, 44205, 43563, 43242, 42700, 42200, 44419, 45142, 43085, 43067, 43319, 45539, 45180, 45512, 45472, 43494, 44051, 43409, 43650, 45079]
    dates = ['2021-05-01', '2021-05-02', '2021-05-03', '2021-05-04', '2021-05-05', '2021-05-06', '2021-05-07', '2021-05-08', '2021-05-09', '2021-05-10', '2021-05-11', '2021-05-12', '2021-05-13', '2021-05-14', '2021-05-15', '2021-05-16', '2021-05-17', '2021-05-18', '2021-05-19', '2021-05-20', '2021-05-21', '2021-05-22', '2021-05-23', '2021-05-24', '2021-05-25', '2021-05-26', '2021-05-27', '2021-05-28', '2021-05-29', '2021-05-30', '2021-05-31']
    base = 25441304

    nums = [43001, 42580, 43034, 42396, 42969, 41341, 41386, 42154, 42490, 41409, 40939, 41322, 40608, 41114, 41898, 41328, 42280, 42281, 42725, 42753, 43820, 44597, 42421, 43738, 43216, 42802, 42495, 42159, 42832, 43128]
    dates = ['2021-06-01', '2021-06-02', '2021-06-03', '2021-06-04', '2021-06-05', '2021-06-06', '2021-06-07', '2021-06-08', '2021-06-09', '2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13', '2021-06-14', '2021-06-15', '2021-06-16', '2021-06-17', '2021-06-18', '2021-06-19', '2021-06-20', '2021-06-21', '2021-06-22', '2021-06-23', '2021-06-24', '2021-06-25', '2021-06-26', '2021-06-27', '2021-06-28', '2021-06-29', '2021-06-30']
    base = 26794973

    nums = [42417, 41369, 41407, 41531, 42232, 40745, 40302, 40173, 39813, 40249, 42648, 42087, 41812, 42070, 41697, 41266, 41664, 41324, 40846, 41100, 42159, 42745, 44406, 43215, 43294, 42129, 42109, 43292, 43608, 42918, 42171]
    dates = ['2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04', '2021-07-05', '2021-07-06', '2021-07-07', '2021-07-08', '2021-07-09', '2021-07-10', '2021-07-11', '2021-07-12', '2021-07-13', '2021-07-14', '2021-07-15', '2021-07-16', '2021-07-17', '2021-07-18', '2021-07-19', '2021-07-20', '2021-07-21', '2021-07-22', '2021-07-23', '2021-07-24', '2021-07-25', '2021-07-26', '2021-07-27', '2021-07-28', '2021-07-29', '2021-07-30', '2021-07-31']
    base = 28066189

    nums = [41655, 41955, 41574, 41190, 41221, 41560, 41503, 42028, 40804, 41292, 42089, 42601, 42913, 42660, 43075, 41614, 41001, 40644, 41866, 41652, 43515, 43200, 42249, 41556, 41938, 41237, 41658, 41945, 42499, 42172, 42139]
    dates = ['2021-08-01', '2021-08-02', '2021-08-03', '2021-08-04', '2021-08-05', '2021-08-06', '2021-08-07', '2021-08-08', '2021-08-09', '2021-08-10', '2021-08-11', '2021-08-12', '2021-08-13', '2021-08-14', '2021-08-15', '2021-08-16', '2021-08-17', '2021-08-18', '2021-08-19', '2021-08-20', '2021-08-21', '2021-08-22', '2021-08-23', '2021-08-24', '2021-08-25', '2021-08-26', '2021-08-27', '2021-08-28', '2021-08-29', '2021-08-30', '2021-08-31']
    base = 29364987
    newa = []

    for index in range(len(dates)):
        base = base + nums[index]
        newa.append(base)

    print(newa)

    book = xlwt.Workbook()
    sheet = book.add_sheet('project_export')

    for index in range(len(newa)):
        sheet.write(0, index, newa[index])

    book.save("demo.xls")

    total = 0
    for i in nums:
        total += i

    print(total, total/31)


if __name__ == "__main__":
    main()