# 게시판 프로그램에서, 게시물의 총 개수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때, 총 페이지 수를 출력하는 프로그램

def get_total_page(total_posts, posts_per_page):
    if total_posts % posts_per_page:
        return total_posts // posts_per_page + 1
    else:
        return total_posts // posts_per_page
    
print(
    get_total_page(5, 10),
    get_total_page(15, 10),
    get_total_page(25, 10),
    get_total_page(30, 10)
)