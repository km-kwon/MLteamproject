from selenium import webdriver as wd
from selenium.webdriver.common.by import By
browser = wd.Chrome(executable_path="chromedriver.exe")

dic = {
    '시동': '183876'
    #'리얼스틸': '76460'
}
scores = {}
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
            reple = reple_block.find_element(By.ID,'_filtered_ment_'+str(k)).text
            k+=1

    #로딩이 끝날때까지 기다림