from selene import browser, command, have
import os



def test_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Nataly')
    browser.element('#lastName').type('Isaeva')
    browser.element('#userEmail').type('lady.astashina@yandex.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('9123006789')
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select').click().element('[value="2"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1990"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Comp').press_enter()
    browser.element('#subjectsInput').type('eco').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').with_(timeout=15).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../1.jpg'))
    browser.element('#currentAddress').type('London').press_enter()
    browser.element('#react-select-3-input').type("Haryana").press_enter()
    browser.element('#react-select-4-input').type("Panipat").press_enter()
    browser.element('#submit').press_enter()
    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts('Nataly Isaeva', 'lady.astashina@yandex.ru', 'Female', '9123006789', '31 March,1990',
         'Computer Science, Economics', 'Reading', '1.jpg', 'London', 'Haryana Panipat'))
