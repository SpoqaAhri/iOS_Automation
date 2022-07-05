
import time
from selenium.webdriver.common.by import By
from ConfigSet import *

class Home(unittest.TestCase):

    def setUp(self):
        ConfigSet.testConfig(Home)

    # DCI-0197_분석 FNB
    def test_DCI_0197(self):
        driver = self.driver
        time.sleep(2)
        tabNameText = driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="분석"]').text
        time.sleep(2)
        self.assertEqual(tabNameText, "분석")
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="분석"]').click()
        time.sleep(2)
        titleNameText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="내역"]').text
        time.sleep(2)
        self.assertEqual(titleNameText, "내역")
        time.sleep(2)


    # DCI-0200_더보기 FNB
    def test_DCI_0200(self):
        driver = self.driver
        time.sleep(2)
        tabNameText = driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').text
        time.sleep(2)
        self.assertEqual(tabNameText, "더 보기")
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)
        titleNameText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        time.sleep(2)
        self.assertEqual(titleNameText, "더 보기")
        time.sleep(2)


    # DCI-0198_전체 내역 FNB
    def test_DCI_0198(self):
        driver = self.driver
        time.sleep(2)
        tabNameText = driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="전체 내역"]').text
        time.sleep(2)
        self.assertEqual(tabNameText, "전체 내역")
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="전체 내역"]').click()
        time.sleep(2)
        titleNameText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="월별 내역"]').text
        time.sleep(2)
        self.assertEqual(titleNameText, "월별 내역")
        time.sleep(2)



    #   DCI-0090_업로드 플로팅 메뉴 - 직접 입력 클릭
    def test_DCI_0090(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]').click()
        time.sleep(2)


        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="직접 입력"]').text
        self.assertEqual(titleText, "직접 입력")
        time.sleep(2)

    #    DCI-0091_업로드 플로팅 메뉴 - 직접 입력 화면 이동
    def test_DCI_0091(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]').click()
        time.sleep(2)

        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="직접 입력"]').text
        self.assertEqual(titleText, "직접 입력")
        time.sleep(2)



    #    DCI-0092_업로드 플로팅 메뉴 - 업로드 가이드 화면 이동
    def test_DCI_0092(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]').click()
        time.sleep(2)

        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="업로드 가이드"]').text
        self.assertEqual(titleText, "업로드 가이드")
        time.sleep(2)


    #    DCI-0124_업로드 내역 화면 - 명세표 등록 순서 안내
    def test_DCI_0124(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeOther[@name="명세표 등록 상황"]/XCUIElementTypeButton[5]').click()
        time.sleep(2)

        listText = driver.find_element(By.XPATH, '(//XCUIElementTypeStaticText[@name="도도 카트로 명세표 전달 완료"])[1]').text
        self.assertEqual(listText, "도도 카트로 명세표 전달 완료")
        time.sleep(2)

    # DCI-0122_업로드 내역 화면 - 뒤로가기
    def test_DCI_0122(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[6]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[1]').click()
        time.sleep(2)

        listText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="업로드 내역"]').text
        self.assertEqual(listText, "업로드 내역")
        time.sleep(2)


    # DCI-0252_명세표 업로드 메뉴 확인
    def test_DCI_0252(self):
        driver = self.driver
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
        time.sleep(2)
        
        driver.find_element(By.XPATH,'//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]').click()
        time.sleep(2)

        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="명세표 업로드 (0/30)"]').text
        self.assertEqual(titleText, "명세표 업로드 (0/30)")
        time.sleep(2)


        addButtonText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="명세표 추가"]').text
        self.assertEqual(addButtonText, "명세표 추가")
        time.sleep(2)


        commitButtonDisplayOK = driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="완료"]')
        self.assertTrue(commitButtonDisplayOK)
        time.sleep(2)



    #  DCI-0253_명세표 업로드 메뉴 닫기
    def test_DCI_0253(self):
        driver = self.driver
        time.sleep(2)


        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton').click()
        time.sleep(2)


        homeText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="식재료 주문 전 시세를 확인하세요"]').text
        self.assertEqual(homeText, "식재료 주문 전 시세를 확인하세요")
        time.sleep(2)



    #  DCI-0253_명세표 업로드 메뉴 닫기
    def test_DCI_(self):
        driver = self.driver
        time.sleep(2)





    def tearDown(self):
      self.driver.quit()


if __name__ == '__main__':
    unittest.main()


