

from openpyxl import Workbook

wb = Workbook() # 워크북 객체 -> 엑셀 파일

# 시트 만들기
wb.create_sheet("my_sheet1")
wb.create_sheet("my_sheet2")

ws = wb.active # 가장 앞쪽 시트를 활성화. ws를 가지고 작업하면 가장 앞쪽 시트에 적용됨.
ws2 = wb["my_sheet2"] # 이름이 my_sheet2인 시트 선택. ws2를 가지고 작업하면 my_sheet2에 적용됨.

# 파일 저장 <- 이걸 해야 반영이 됨.
wb.save("test.xlsx")