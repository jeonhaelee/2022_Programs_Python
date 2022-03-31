# 프로그램 기본 구조

# 입력-처리-출력 -> 반복


articles = []
# article 딕셔너리들이 들어갈 articles 리스트.

def print_articles():
    print("======================================")
    for i in range(len(articles)):
        target = articles[i]
        print("번호 : {}".format(i+1))
        print("제목 : {}".format(target["title"]))
        print("======================================")



while True:
    cmd = input("명령어를 입력해주세요 : ")
    
    if cmd == "help":
        print("도움말 목록")
        print("add : 게시물 등록")
        print("list : 게시물 목록 조회")
        
    elif cmd == "exit":
        print("프로그램을 종료합니다.")
        break
    
    elif cmd == "add":
        
        title = input("제목을 입력해주세요 : ")
        body = input("내용을 입력해주세요 : ")
        
        article = {"title" : title, "body" : body}
        articles.append(article)
        
        print("게시물이 저장되었습니다.")
        
    elif cmd == "list":
        print_articles()
    
    elif cmd == "update":
        
        no = input("수정할 게시물 번호 : ")
        no = int(no)
        
        target_idx = no-1
        if target_idx >= len(articles):
            print("없는 게시물 번호입니다.")
            
        else:
            update_target = articles[target_idx]
        
            new_title = input("새제목 : ")
            new_body = input("새내용 : ")
            update_target["title"] = new_title
            update_target["body"] = new_body
        
            print("수정이 완료되었습니다.")
            print_articles()
    
    elif cmd == "delete":
        no = input("삭제할 게시물 번호 : ")
        no = int(no)
        
        target_idx = no-1
        if target_idx >= len(articles):
            print("없는 게시물 번호입니다.")
            
        else:
            del articles[target_idx]

            print("삭제가 완료되었습니다.")
            print_articles()
        
    else :
        print("알 수 없는 명령어. 명령어 목록을 보시려면 help를 입력하세요.")
    