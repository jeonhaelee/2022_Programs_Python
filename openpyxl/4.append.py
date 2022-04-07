

from openpyxl import Workbook

wb = Workbook() 
ws = wb.active

# 행단위 추가
# 가장 마지막 행에 추가됨
ws.append(["번호", "제목", "내용"])
ws.append([1, "안녕하세요", "반갑습니다."])
ws.append([2, "질문있어요", "엑셀 어떻게 다루죠?"])

# 빈 행 추가
ws.insert_rows(3)

# 한 행을 선택 ws[행번호]
row = ws[3]
row[0].value = 3
row[1].value = "추가된 게시물"
row[2].value = "추가된 게시물 내용"

# 한 열을 추가
ws.insert_cols(3)

# 한 열을 선택
col = ws['C']
col[0].value = "작성자"
col[1].value = "작성자1"
col[2].value = "작성자2"
col[3].value = "작성자3"

# 행 삭제
ws.delete_rows(4)

# 열 삭제
ws.delete_cols(3)

# 판다스...

wb.save("test3.xlsx")