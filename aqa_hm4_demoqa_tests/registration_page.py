from datetime import datetime
from selene import browser, have, be

from aqa_hm4_demoqa_tests import resourse
from aqa_hm4_demoqa_tests.resourse import path
from tests.conftest import removing_banner


class RegistrationPage:

    def open(self):
        browser.open('/')
        removing_banner()

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_dateOfBirth(self, month, day, year):
        browser.element('#dateOfBirthInput').should(
            have.value(datetime.now().strftime('%d %b %Y'))
        ).click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.all('.react-datepicker__week')[4].all('[role="option"]')[6].should(
            have.exact_text(day)
        ).click()

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

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def fill_gender_male(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def fill_phonenumber(self, number):
        browser.element('#userNumber').should(be.blank).type(number)

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

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

    def fill_attachment(self, attachment):
        browser.element('#uploadPicture').set_value(resourse.path(attachment))

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

    def fill_submit(self):
        browser.element('#submit').click()
