
from selenium.webdriver.common.by import By
import time
import StringMetaData
from StringMetaData import *
from ConfigSet import *


class More(unittest.TestCase):

    def setUp(self):
        ConfigSet.testConfig(More)



    #   DCI-0649_더보기 화면 구성
    def test_DCI_0649(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        driver.swipe(866, 742, 882, 2178)
        time.sleep(2)

        # 더보기 타이틀 확인
        moreDisplayTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        time.sleep(2)
        self.assertEqual(moreDisplayTitle, StringMetaData.more_title)
        time.sleep(2)

        # 매장 추가 버튼 확인
        shopAddTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="매장 추가"]').text
        time.sleep(2)
        self.assertEqual(shopAddTitle, StringMetaData.more_store_add)
        time.sleep(2)

        # 매장 정보 영역, 매장 이름 확인 (최상단 매장)
        firstShopName = driver.find_element(By.XPATH, '(//XCUIElementTypeStaticText[@name="아리테스트매장"])[2]').text
        time.sleep(2)
        self.assertEqual(firstShopName, StringMetaData.store_name)
        time.sleep(2)


        # 서비스 설정 - 알림 설정 메뉴 노출 여부 확인
        notificationSettingTitle = driver.find_element(By.XPATH,
                                                       '//XCUIElementTypeStaticText[@name="알림 설정"]').text
        time.sleep(2)
        self.assertEqual(notificationSettingTitle, StringMetaData.more_noti_set)
        time.sleep(2)

        # 고객센터 - 카카오톡 문의 메뉴 노출 여부 확인
        kakaoChatTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="카카오톡 문의"]').text
        time.sleep(2)
        self.assertEqual(kakaoChatTitle, StringMetaData.more_kakao_chat)
        time.sleep(2)

        # 고객센터 - 자주 묻는 질문 메뉴 노출 여부 확인
        faqTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="자주 묻는 질문"]').text
        time.sleep(2)
        self.assertEqual(faqTitle, StringMetaData.more_faq)
        time.sleep(2)

        # 데이터 관리 - 데이터 내보내기 메뉴 노출 여부 확인
        termsItemLayoutTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="데이터 내보내기"]').text
        time.sleep(2)
        self.assertEqual(termsItemLayoutTitle, StringMetaData.more_data_output)
        time.sleep(2)

        # 더보기 페이지 하단으로 스크롤 - swipe로 변경 & 고정 슬립 by jude
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        # 약관 및 정책 - 도도 카트 이용약관 메뉴 노출 여부 확인
        dodoTermsTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="도도 카트 이용약관"]').text
        time.sleep(2)
        self.assertEqual(dodoTermsTitle, StringMetaData.more_dodoTerms)
        time.sleep(2)

        # 약관 및 정책 - 개인정보 취급 방침 메뉴 노출 여부 확인
        privacyInfoTitle = driver.find_element(By.XPATH,
                                               '//XCUIElementTypeStaticText[@name="개인정보 취급방침"]').text
        time.sleep(2)
        self.assertEqual(privacyInfoTitle, StringMetaData.more_privacyInfo)
        time.sleep(2)

        # 약관 및 정책 - 오픈 소스 라이선스 메뉴 노출 여부 확인
        openSourceTitle = driver.find_element(By.XPATH,
                                              '//XCUIElementTypeStaticText[@name="오픈소스 라이선스"]').text
        time.sleep(2)
        self.assertEqual(openSourceTitle, StringMetaData.more_openSource)
        time.sleep(2)

        # 버전 정보 메뉴 노출 여부 확인
        versionViewTitle = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="버전 정보 (1.9.0)"]')
        time.sleep(2)
        self.assertTrue(versionViewTitle)
        time.sleep(2)



    #   DCI-0694_데이터 내보내기 이동
    def test_DCI_0694(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 데이터 내보내기 클릭
        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]').click()
        time.sleep(2)

        # 데이터 내보내기 페이지 이동 확인
        titleText = driver.find_element(By.XPATH,'//XCUIElementTypeStaticText[@name="데이터 내보내기"]').text
        self.assertEqual(titleText, "데이터 내보내기")
        time.sleep(2)



    #   DCI-0695_데이터 내보내기 화면 구성
    def test_DCI_0695(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 데이터 내보내기 클릭
        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]').click()
        time.sleep(2)

        # 데이터 내보내기 페이지 이동 확인
        subcategoryText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="아리테스트매장의 지출 내역을 엑셀로 받아보세요."]').text
        self.assertEqual(subcategoryText, "아리테스트매장의 지출 내역을 엑셀로 받아보세요.")
        time.sleep(2)

        # 이메일 입력필드 확인
        emailEditTextBoxDisplayOK = driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="React App"]/XCUIElementTypeTextField')
        self.assertTrue(emailEditTextBoxDisplayOK)
        time.sleep(2)

        # 월별 버튼 확인
        monthButtonDisplayOK = driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="React App"]/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]')
        self.assertTrue(monthButtonDisplayOK)
        time.sleep(2)

        # 직접 설정 버튼 확인
        directSettingButtonDisplayOK = driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="React App"]/XCUIElementTypeOther[5]/XCUIElementTypeOther[2]')
        self.assertTrue(directSettingButtonDisplayOK)
        time.sleep(2)

        # 내보내기 버튼 확인
        sendButtonDisplayOK = driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="내보내기"]')
        self.assertTrue(sendButtonDisplayOK)
        time.sleep(2)



    #  DCI-0683_알림 설정 화면 구성
    def test_DCI_0683(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 알림 설정 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]').click()
        time.sleep(2)

        recipeNotiText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="명세표 등록 완료 안내 메시지"]').text
        self.assertEqual(recipeNotiText, "명세표 등록 완료 안내 메시지")
        time.sleep(2)

        subjectNotiText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="품목 가격 안내 메시지"]').text
        self.assertEqual(subjectNotiText, "품목 가격 안내 메시지")
        time.sleep(2)

        markettingNotiText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="마케팅 정보 메시지"]').text
        self.assertEqual(markettingNotiText, "마케팅 정보 메시지")
        time.sleep(2)




    #  DDCI-0684_알림 설정 화면 뒤로가기
    def test_DCI_0684(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 알림 설정 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[4]').click()
        time.sleep(2)

        # 뒤로가기 버튼 클릭
        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton').click()

        # 페이지 이동 확인
        moreTitleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        self.assertEqual(moreTitleText, "더 보기")
        time.sleep(2)



    #  DCI-0692_자주 묻는 질문
    def test_DCI_0692(self):
        driver = self.driver
        time.sleep(2)


        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 페이지 하단으로 스크롤
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]').click()
        time.sleep(2)


        titleText = driver.find_element(By.XPATH, '(//XCUIElementTypeStaticText[@name="자주 묻는 질문"])[1]').text
        self.assertEqual(titleText, "자주 묻는 질문")
        time.sleep(2)



    #  DCI-0693_자주 묻는 질문 - 닫기
    def test_DCI_0693(self):
        driver = self.driver
        time.sleep(2)


        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 페이지 하단으로 스크롤
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]').click()
        time.sleep(2)


        titleText = driver.find_element(By.XPATH, '(//XCUIElementTypeStaticText[@name="자주 묻는 질문"])[1]').text
        self.assertEqual(titleText, "자주 묻는 질문")
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="icn arrow left gray"]').click()
        time.sleep(2)

        moreTitleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        self.assertEqual(moreTitleText, "더 보기")
        time.sleep(2)



    #  DCI-0731_개인정보 취급방침 확인
    def test_DCI_0731(self):
        driver = self.driver
        time.sleep(2)


        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 페이지 하단으로 스크롤
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]').click()
        time.sleep(2)


        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="개인정보 취급방침"]').text
        self.assertEqual(titleText, "개인정보 취급방침")
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="icn arrow left gray"]').click()
        time.sleep(2)

        moreTitleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        self.assertEqual(moreTitleText, "더 보기")
        time.sleep(2)



    #  DCI-0732_오픈 소스 라이선스 확인
    def test_DCI_0732(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 페이지 하단으로 스크롤
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[9]').click()
        time.sleep(2)

        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="오픈소스 라이선스"]').text
        self.assertEqual(titleText, "오픈소스 라이선스")
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="icn arrow left gray"]').click()
        time.sleep(2)

        moreTitleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        self.assertEqual(moreTitleText, "더 보기")
        time.sleep(2)




    #  DCI-0730_도도 카트 이용약관 확인
    def test_DCI_0730(self):
        driver = self.driver
        time.sleep(2)

        # 더보기 이동
        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="더 보기"]').click()
        time.sleep(2)

        # 페이지 하단으로 스크롤
        driver.swipe(268, 618, 286, 343)
        time.sleep(2)

        driver.find_element(By.XPATH,
                            '//XCUIElementTypeApplication[@name="도도 카트 QA"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[7]').click()
        time.sleep(2)


        titleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="도도 카트 이용약관"]').text
        self.assertEqual(titleText, "도도 카트 이용약관")
        time.sleep(2)

        driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="icn arrow left gray"]').click()
        time.sleep(2)

        moreTitleText = driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="더 보기"]').text
        self.assertEqual(moreTitleText, "더 보기")
        time.sleep(2)




    def tearDown(self):
      self.driver.quit()



if __name__ == '__main__':
    unittest.main()