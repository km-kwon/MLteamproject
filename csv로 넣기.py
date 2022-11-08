from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import csv
browser = wd.Chrome(executable_path="chromedriver.exe")

dic = {
    '시동': '183876'#,
    #'리얼스틸': '76460',
    #'리멤버':'191657'
}
dic1 = {
    '건축학개론': 'm5Gvy2d'
}

f = open(r"C:\Users\kkm\Desktop\대학\2-2\기계학습\팀플\파이썬\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['reple','star_score'])
for value in dic.values():
    for i in range(15):
        if i==0:
            continue
        url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code="+str(value)+"&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="+str(i)
        browser.get(url)
        browser.implicitly_wait(10)
        score_board = browser.find_element(By.CLASS_NAME, 'score_result')
        scores = score_board.find_elements(By.TAG_NAME, 'li')
        k = 0
        for score in scores:
            star = score.find_element(By.CLASS_NAME,'star_score')
            star_score = star.find_element(By.TAG_NAME,'em').text
            reple_block = score.find_element(By.CLASS_NAME, 'score_reple')
            reple = reple_block.find_element(By.ID,'_filtered_ment_'+str(k)).get_attribute("innerText")
            reple = reple.strip()
            k+=1
            if not reple:
                continue
            csvWriter.writerow([reple, star_score])
for value in dic1.values():
    url= "https://pedia.watcha.com/ko-KR/contents/"+str(value)+"/comments"
    browser.get(url)
    browser.implicitly_wait(10)
    score_boards = browser.find_elements(By.CLASS_NAME,'css-bawlbm')
    for score_board in score_boards:
        star = score_board.find_element(By.CLASS_NAME, 'css-yqs4xl')
        star_score = star.find_element(By.TAG_NAME, 'span').text
        reple_block = score_board.find_element(By.CLASS_NAME, 'css-1g78l7j')
        reple = reple_block.find_element(By.TAG_NAME,'span').text

f.close()
    #로딩이 끝날때까지 기다림