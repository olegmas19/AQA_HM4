from aqa_hm4_demoqa_tests import user
from aqa_hm4_demoqa_tests.user_registration_page import UserRegistrationSteps


def test_filling_sending_forms():
    registration_page = UserRegistrationSteps()
    ivan = user.ivan

    # GIVEN
    registration_page.open()
    # WHEN
    registration_page.register(ivan)
    # THEN
    registration_page.should_have_registered(ivan)
