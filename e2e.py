from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url: str) -> bool:
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        score_element = driver.find_element(By.ID, 'score')
        score_text = score_element.text
        score = int(score_text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except:
        return False
    finally:
        driver.quit()


def main_function():
    url = 'http://127.0.0.1:5000'
    result = test_scores_service(url)

    if result:
        return 0
    else:
        return -1


if __name__ == '__main__':
    exit_code = main_function()
    exit(exit_code)
