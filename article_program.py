# 프로그램 기본 구조
# 입력-처리-출력 -> 반복

import article_mod as am
        
while True:
    cmd = input("명령어를 입력해주세요 : ")
    
    if cmd == "help":
        am.print_help()
        
    elif cmd == "exit":
        print("프로그램을 종료합니다.")
        break
    
    elif cmd == "add":
        am.add_article()
        
    elif cmd == "list":
        am.print_articles()
    
    elif cmd == "update":
        am.update_article()
    
    elif cmd == "delete":
        am.delete_article()
        
    else :
        print("알 수 없는 명령어. 명령어 목록을 보시려면 help를 입력하세요.")
    