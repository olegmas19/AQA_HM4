from datetime import datetime

import allure
from selene import browser, have, be
from aqa_hm4_demoqa_tests import resourse
from aqa_hm4_demoqa_tests.resourse import DATA_DIR

# from tests.conftest import removing_banner


class RegistrationPage:

    @allure.step("Открываем форму регистрации")
    def open(self):
        browser.open('/')

    def removing_banner(self):
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step("Заполняем поле - First Name")
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    @allure.step("Заполняем поле - Last Name")
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    @allure.step("Заполняем поле - Date of Birth")
    def fill_dateOfBirth(self, month, day, year):
        browser.element('#dateOfBirthInput').should(
            have.value(datetime.now().strftime('%d %b %Y'))
        ).click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.all('.react-datepicker__week')[4].all('[role="option"]')[6].should(
            have.exact_text(day)
        ).click()

    @allure.step("Проверяем результаты заполнения")
    def should_have_registered(
        self,
        name_nl,
        email,
        gender,
        phone_number,
        dateOfBirth,
        subject,
        hobbies,
        attachment,
        address,
        state_city,
    ):
        browser.all('table td:nth-of-type(2)').should(
            have.texts(
                name_nl,
                email,
                gender,
                phone_number,
                dateOfBirth,
                subject,
                hobbies,
                attachment,
                address,
                state_city,
            )
        )
        browser.element('#closeLargeModal').click()

    @allure.step("Заполняем поле - Email")
    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    @allure.step("Заполняем поле - Gender")
    def fill_gender_male(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    @allure.step("Заполняем поле - Mobile Number")
    def fill_phonenumber(self, number):
        browser.element('#userNumber').should(be.blank).type(number)

    @allure.step("Заполняем поле - Subjects")
    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    @allure.step("Заполняем поле - Hobbies")
    def fill_hobbies(self, hobbies1, hobbies2, hobbies3):
        browser.element('[for="hobbies-checkbox-1"]').should(
            have.text(hobbies1)
        ).click()
        browser.element('[for="hobbies-checkbox-2"]').should(
            have.text(hobbies2)
        ).click()
        browser.element('[for="hobbies-checkbox-3"]').should(
            have.text(hobbies3)
        ).click()

    @allure.step("Заполняем поле - Picture")
    def fill_attachment(self, attachment):
        browser.element('#uploadPicture').set_value(DATA_DIR + f'/{attachment}')

    @allure.step("Заполняем поля - Current address, State and City")
    def fill_address(self, address, state, city):
        browser.element('#currentAddress').should(be.blank).type(address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    @allure.step("Нажимаем - Submit")
    def fill_submit(self):
        browser.element('#submit').click()
