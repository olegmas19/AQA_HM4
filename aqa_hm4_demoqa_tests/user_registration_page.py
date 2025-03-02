from datetime import datetime

from selene import browser, have, be

from aqa_hm4_demoqa_tests import resourse
from aqa_hm4_demoqa_tests.user import User
from tests.conftest import removing_banner


class UserRegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('[name=gender][value=Male]+label')
        self.phone_number = browser.element('#userNumber')
        self.dateOfBirth = browser.element('#dateOfBirthInput')
        self.subject = browser.element('#subjectsInput')
        self.hobbies1 = browser.element('[for="hobbies-checkbox-1"]')
        self.hobbies2 = browser.element('[for="hobbies-checkbox-2"]')
        self.hobbies3 = browser.element('[for="hobbies-checkbox-3"]')
        self.attachment = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, email):
        self.email.type(email)

    def fill_gender_male(self):
        self.gender.click()

    def fill_phonenumber(self, number):
        self.phone_number.type(number)

    def fill_dateOfBirth(self, day, month, year):
        self.dateOfBirth.should(have.value(datetime.now().strftime('%d %b %Y'))).click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.all('.react-datepicker__week')[4].all('[role="option"]')[6].should(
            have.exact_text(day)
        ).click()

    def fill_subject(self, subject):
        self.subject.type(subject).press_enter()

    def fill_hobbies1(self, hobbies1):
        self.hobbies1.should(have.text(hobbies1)).click()

    def fill_hobbies2(self, hobbies2):
        self.hobbies2.should(have.text(hobbies2)).click()

    def fill_hobbies3(self, hobbies3):
        self.hobbies3.should(have.text(hobbies3)).click()

    def fill_attachment(self, attachment):
        self.attachment.set_value(resourse.path(attachment))

    def fill_address(self, address):
        self.current_address.should(be.blank).type(address)

    def fill_state(self, state):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def fill_city(self, city):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def fill_submit(self):
        self.submit.click()


class UserRegistrationSteps:

    def __init__(self):
        self.page = UserRegistrationPage()

    def open(self):
        browser.open('/')
        removing_banner()

    def register(self, user: User):
        self.page.fill_first_name(user.first_name)
        self.page.fill_last_name(user.last_name)
        self.page.fill_email(user.email)
        self.page.fill_gender_male()
        self.page.fill_phonenumber(user.pnonenumber)

        day, month, year = user.dateOfBirth

        self.page.fill_dateOfBirth(day, month, year)
        self.page.fill_subject(user.subject)
        self.page.fill_hobbies1(user.hobbies1)
        self.page.fill_hobbies2(user.hobbies2)
        self.page.fill_hobbies3(user.hobbies3)
        self.page.fill_attachment(user.attachment)
        self.page.fill_address(user.address)
        self.page.fill_state(user.state)
        self.page.fill_city(user.city)

        self.page.fill_submit()

    def should_have_registered(self, user: User):
        day, month, year = user.dateOfBirth
        browser.all('table td:nth-of-type(2)').should(
            have.texts(
                user.first_name + ' ' + user.last_name,
                user.email,
                'Male',
                user.pnonenumber,
                f'{day} {month},{year}',
                user.subject,
                f'{user.hobbies1}, {user.hobbies2}, {user.hobbies3}',
                user.attachment,
                user.address,
                f'{user.state} {user.city}',
            )
        )
        browser.element('#closeLargeModal').click()
