import os

from selene import browser, be, have
from selene.core import command
from selene.support.shared.jquery_style import s


def test_dificult_form():
    browser.open('automation-practice-form')

    # заполнение формы
    s('#adplus-anchor').perform(command.js.remove)
    s('#fixedban').perform(command.js.remove)

    browser.element('[id=firstName]').should(be.blank).type('Ivan')
    browser.element('[id=lastName]').should(be.blank).type('Ivanov')
    browser.element('[id=userEmail]').should(be.blank).type('ivan@co.com')
    browser.element('.custom-control-label').click()
    browser.element('[id=userNumber]').should(be.blank).type('9999999999')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1989"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__day--028').click()
    browser.element('[id="subjectsInput"]').click().send_keys("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('tests/images/picture.jpeg'))
    browser.element('[id=currentAddress]').type('Москва, ул. Тверская, дом 1')
    browser.element('input#react-select-3-input').type("Haryana").press_enter()
    browser.element('input#react-select-4-input').type("Panipat").press_enter()
    browser.element('[id="submit"]').click()
    browser.element('[id="closeLargeModal"]').click()


    # Проверка формы
    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-body tr td')[1].should(have.exact_text('Ivan Ivanov'))
    browser.all('.modal-body tr td')[3].should(have.exact_text('ivan@co.com'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Male'))
    browser.all('.modal-body tr td')[7].should(have.exact_text('9999999999'))
    browser.all('.modal-body tr td')[9].should(have.exact_text('28 Dec, 1989'))
    browser.all('.modal-body tr td')[11].should(have.exact_text('Maths'))
    browser.all('.modal-body tr td')[13].should(have.exact_text('Sports'))
    browser.all('.modal-body tr td')[15].should(have.exact_text('picture.jpeg'))
    browser.all('.modal-body tr td')[17].should(have.exact_text('Москва, ул. Тверская, дом 1'))
    browser.all('.modal-body tr td')[19].should(have.text('Haryana'))
    browser.all('.modal-body tr td')[20].should(have.text('Panipat'))

    # Закрытие модального окна
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
