import time
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
)

class MatchLearning:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver  # webdriver

    def get_score(self) -> int:
        driver = self.driver
        score = driver.find_element(
            By.XPATH, "//*[@id='match-wrapper']/div[1]/div[2]/span[2]"
        ).text
        return int(score)

    def is_substring(self, s1: str, s2: str) -> bool:
        return s1 in s2 or s2 in s1

    def run(self, num_d: int, word_d: list) -> None:  # 핸들러 실행
        driver = self.driver
        da_e, da_k, _ = word_d
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[5]"
        ).click()  # 세트 화면에서 매칭게임 버튼 클릭
        time.sleep(1)
        driver.find_element(  # 매칭게임 시작 버튼 클릭
            By.CSS_SELECTOR,
            "#wrapper-learn > div.vertical-mid.center.fill-parent > div.start-opt-body > div > div > div.start-opt-box > div:nth-child(4) > a",
        ).click()
        time.sleep(2)

        while self.get_score() < 3000:
            time.sleep(2)
            kor_word = []
            for i in range(4):
                kword = driver.find_element(
                        By.XPATH,
                        f"/html/body/div[2]/div[1]/div[3]/div[3]/div[2]/div[{i+1}]",
                    ).text
                kword = kword.split("\n")[0].replace('"', '')
                kor_word.append(kword)

            answer_l = -1
            answer_r = -1
            for i in range(4):
                word_str = driver.find_element(
                        By.XPATH,
                        f"/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div[{i+1}]",
                    ).text
                word_str = word_str.split("\n")[0]

                word_idx = da_e.index(word_str)

                if word_idx > 0:
                    ans_str = da_k[word_idx]
                    for j in range(4):
                        if ans_str == kor_word[j]:
                            answer_r = j
                            answer_l = i
                            break

            try:
                left_element = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div[{answer_l+1}]",
                )
                right_element = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[2]/div[1]/div[3]/div[3]/div[2]/div[{answer_r+1}]",
                )

                left_element.click()
                right_element.click()
            except:
                time.sleep(1)
                pass

            time.sleep(1)