from selene import have
from tests.data.data import User
from tests.demoqa_tests.application_manager import app
import logging
import allure
from allure_commons.types import Severity


logging.getLogger('WDM').setLevel(logging.NOTSET)



@allure.tag('student_registration')
@allure.severity(Severity.CRITICAL)
@allure.story('Проверяем форму регистрации студента')
@allure.link('https://demoqa.com/automation-practice-form')
@allure.label('owner', 'Helpmerunaway')
@allure.description('Заполнение валидными данными и их проверка в модальном окне')
@allure.feature('Регистрация студента')
@allure.epic("Регистрация")
@allure.title('Проверка формы регистрации студента')
def test_register_student_dev_patel(setup_browser):
	browser = setup_browser
	student = User()
	form = app.registration_form
	results = app.results_modal.table
	with allure.step("Open registrations form"):
		browser.open("https://demoqa.com/automation-practice-form")
		browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
		browser.driver.execute_script("$('footer').remove()")
		browser.driver.execute_script("$('#fixedban').remove()")

	with allure.step("Заполняем поле First name"):
		form.set_first_name(student.first_name)

	with allure.step("Заполняем поле Last name"):
		form.set_last_name(student.last_name)

	with allure.step("Заполняем поле email"):
		form.set_email(student.email)

	with allure.step("Указываем пол"):
		form.set_male_gender()

	with allure.step("Заполняем поле Mobile"):
		form.set_mobile_number(student.mobile_number)

	with allure.step("Указываем дату рождения: день, месяц, год"):
		form.set_date_of_birth(student.birthday_day,
		                       student.birthday_month, student.birthday_year)

	with allure.step("Указываем дисциплины"):
		form.add_subject(student.subject_computer_science)\
			.add_subject(student.subject_social_studies)\
			.add_subject(student.subject_chemistry)\
			.add_subject(student.subject_maths)\
			.add_subject(student.subject_physics)

	with allure.step("Выбираем хобби"):
		form.add_hobbies(student.hobby_sports)\
			.add_hobbies(student.hobby_reading)\
			.add_hobbies(student.hobby_music)

	with allure.step("Загружаем изображение"):
		form.browse_picture(student.picture)

	with allure.step("Указываем текущий адрес"):
		form.set_address(student.address)

	with allure.step("Выбираем штат"):
		form.select_state(option=student.state)

	with allure.step("Выбираем город"):
		form.select_city(option=student.city)

	with allure.step("Клик на кнопку отправить"):
		form.submit()

	with allure.step("Проверка данных в модальном окне"):
		results.check_cells_of_row(1).should(have.exact_texts(
			'Student Name', f'{student.first_name} {student.last_name}'))
		results.check_cells_of_row(2).should(have.exact_texts(
			'Student Email', f'{student.email}'))
		results.check_cells_of_row(3).should(have.exact_texts(
			'Gender', f'{student.gender}'))
		results.check_cells_of_row(4).should(have.exact_texts(
			'Mobile', f'{student.mobile_number}'))
		results.check_cells_of_row(5).should(have.exact_texts(
			'Date of Birth', f'{student.birthday_day}'
			                 f' {student.birthday_month_name},'
			                 f'{student.birthday_year}'))
		results.check_cells_of_row(6).should(have.exact_texts(
			'Subjects',
			f'{student.subject_computer_science},'
			f' {student.subject_social_studies}, '
			f'{student.subject_chemistry},'
			f' {student.subject_maths}, {student.subject_physics}'))
		results.check_cells_of_row(7).should(have.exact_texts(
			'Hobbies', f'{student.hobby_sports},'
			           f' {student.hobby_reading}, {student.hobby_music}'))
		results.check_cells_of_row(8).should(have.exact_texts(
			'Picture', student.picture))
		results.check_cells_of_row(9).should(have.exact_texts(
			'Address', student.address))
		results.check_cells_of_row(10).should(have.exact_texts(
			'State and City', f'{student.state} {student.city}'))

	with allure.step("Закрываем окно"):
		app.results_modal.close_modal_and_check_result()