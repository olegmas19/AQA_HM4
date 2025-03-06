from datetime import datetime
import os
from selene import browser, have, be


def test_filling_sending_forms():
    pass
    # browser.open('/')
    # # Для мест, где есть баннеры.
    # browser.driver.execute_script("$('#fixedban').remove()")
    # browser.driver.execute_script("$('footer').remove()")
    # browser.should(have.title('DEMOQA'))
    #
    # browser.element('#firstName').should(be.blank).type('Иван')
    # browser.element('#lastName').should(be.blank).type('Иванов')
    # browser.element('#userEmail').should(be.blank).type('Ivan@mail.ru')
    # browser.element('[for="gender-radio-1"]').click()
    # browser.element('#userNumber').should(be.blank).type('8989567666')
    # browser.element('#dateOfBirthInput').should(
    #     have.value(datetime.now().strftime('%d %b %Y'))
    # ).click()
    # browser.element('.react-datepicker__month-select').element('[value="1"]').should(
    #     have.exact_text('February')
    # ).click()
    # browser.element('.react-datepicker__year-select').element('[value="1992"]').should(
    #     have.exact_text('1992')
    # ).click()
    # browser.all('.react-datepicker__week')[4].all('[role="option"]')[6].should(
    #     have.exact_text('29')
    # ).click()
    # browser.element('#subjectsInput').type('History').press_enter()
    # browser.element('[for="hobbies-checkbox-1"]').click()
    # browser.element('[for="hobbies-checkbox-2"]').click()
    # browser.element('[for="hobbies-checkbox-3"]').click()
    # browser.element('#uploadPicture').send_keys(
    #     os.path.abspath('../data/IMG_1332.JPEG')
    # )
    # browser.element('#currentAddress').should(be.blank).type(
    #     'Россия, г. Сызрань, Солнечная ул., д. 12 кв.137'
    # )
    # browser.element('#state').click().element('#react-select-3-option-0').click()
    # browser.element('#city').click().element('#react-select-4-option-0').click()
    # browser.element('#submit').click()
    #
    # browser.element('.table').should(have.text('Иван Иванов'))
    # browser.element('.table').should(have.text('Ivan@mail.ru'))
    # browser.element('.table').should(have.text('Male'))
    # browser.element('.table').should(have.text('8989567666'))
    # browser.element('.table').should(have.text('29 February,1992'))
    # browser.element('.table').should(have.text('History'))
    # browser.element('.table').should(have.text('Sports, Reading, Music'))
    # browser.element('.table').should(have.text('IMG_1332.JPEG'))
    # browser.element('.table').should(
    #     have.text('Россия, г. Сызрань, Солнечная ул., д. 12 кв.137')
    # )
    # browser.element('.table').should(have.text('NCR Delhi'))
    # browser.element('#closeLargeModal').click()
