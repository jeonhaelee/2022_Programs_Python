
from openpyxl import Workbook

wb = Workbook() # 워크북 객체 

ws = wb.active # 가장 앞쪽 시트 활성화
ws["C6"] = 100 # C6 셀에 100 기입
target_cell = ws.cell(row = 6, column = 3) # 6번째 행, 3번째 열 행정보 가져오기

print(target_cell.value) # 해당 셀의 값 추출

wb.save("test.xlsx")