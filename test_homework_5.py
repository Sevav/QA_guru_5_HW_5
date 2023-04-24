from selene import browser, have
import os


def test_form():
    browser.open('/automation-practice-form')

    browser.element('[id=firstName]').type('Sergey')
    browser.element('[id=lastName]').type('Petrov')
    browser.element('[id=userEmail]').type('Petrov@mail.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('[id=userNumber]').set('8999777777')

    browser.element('[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value = "9"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value = "1991"]').click()
    browser.element('.react-datepicker__day--019').click()

    browser.element('[id=subjectsInput]').type('History').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[id=uploadPicture]').send_keys(os.getcwd() + '/test.jpg')

    browser.element('[id=currentAddress]').type('Moscow')
    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    browser.element('[id=react-select-4-input]').type('Delhi').press_enter()
    browser.element('[id=submit]').press_enter()

    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Sergey Petrov', 'Student Email Petrov@mail.ru', 'Gender Male', 'Mobile 8999777777',
        'Date of Birth 19 October,1991', 'Subjects History', 'Hobbies Sports',
        'Picture test.jpg', 'Address Moscow', 'State and City NCR Delhi'))

    print('Тест прошел успешно!')










