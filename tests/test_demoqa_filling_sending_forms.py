from aqa_hm4_demoqa_tests.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Регистрация пользователя")
@allure.story("Пользователь может заполнить форму и зарегистрироваться")
@allure.description("Тестовая аннотация")
@allure.suite("UI-Тесты")
@allure.link("https://demoqa.com/automation-practice-form", name="Testing")
@allure.title("Заполнение формы/Регистрация пользователя")
def test_filling_sending_forms():
    registration_page = RegistrationPage()
    # GIVEN
    registration_page.open()
    registration_page.removing_banner()

    # WHEN
    registration_page.fill_first_name('Иван')
    registration_page.fill_last_name('Иванов')
    registration_page.fill_email('Ivan@mail.ru')
    registration_page.fill_gender_male('Male')
    registration_page.fill_phonenumber('8989567666')
    registration_page.fill_dateOfBirth('February', '29', '1992')
    registration_page.fill_subject('History')
    registration_page.fill_hobbies('Sports', 'Reading', 'Music')
    registration_page.fill_attachment('IMG_1332.JPEG')
    registration_page.fill_address('Солнечная ул., д. 12 кв.137', 'Haryana', 'Karnal')
    registration_page.fill_submit()

    # THEN
    registration_page.should_have_registered(
        'Иван Иванов',
        'Ivan@mail.ru',
        'Male',
        '8989567666',
        '29 February,1992',
        'History',
        'Sports, Reading, Music',
        'IMG_1332.JPEG',
        'Солнечная ул., д. 12 кв.137',
        'Haryana Karnal',
    )
