

from openpyxl import Workbook

wb = Workbook() # 워크북 객체 -> 엑셀 파일
ws = wb.active

cell_range = ws['B2':'D4']

# 이중리스트 -> 행렬을 표현할 때 사용.
# num = 1
# for row in cell_range:
#     for cell in row:
#         cell.value = num
#         num += 1

for row in ws.iter_rows(min_row = 3, max_row = 20, min_col = 2, max_col = 4):
    for cell in row:
        cell.value = 'aaa'

for row in ws.iter_cols(min_row = 3, max_row = 20, min_col = 2, max_col = 4):
    for cell in row:
        cell.value = 'aaa'
        
        
# 전체 행 조회
for row in ws.rows:
    for cell in row:
        cell.value = 'bb'

# 전체 열 조회

wb.save("test2.xlsx")