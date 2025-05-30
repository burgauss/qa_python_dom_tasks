import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Clase para la página de inicio de sesión
class LoginPageAround:
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()


# Clase para el encabezado
class HeaderPageAround:
    # Crea un localizador para el elemento Correo electrónico en el encabezado
    header_user = (By.CLASS_NAME, 'header__user')

    def __init__(self, driver):
        self.driver = driver

    # Espera a que se cargue la página
    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_user))

    # Método para recuperar el texto del elemento en el encabezado
    def email_in_header(self):
        return self.driver.find_element(*self.header_user).text


# Clase con la prueba automatizada
class TestAround:

    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()

    def test_check_email_in_header(self):
        # Abre la página de la aplicación de prueba
        self.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
        time.sleep(3)

        # Crea una clase de objeto de página para la página de inicio de sesión
        login_page = LoginPageAround(self.driver)

        # iniciar sesión
        correo_electronico = 'burgos.137@gmail.com'
        password = '12345'
        # Pasa estas variables al método.
        login_page.login(correo_electronico, password)

        # Crea un objeto para el encabezado
        header_page = HeaderPageAround(self.driver)
        # Espera a que se cargue el encabezado
        header_page.wait_for_load_header()
        # Recupera el texto de un elemento en el encabezado
        email_from_header = header_page.email_in_header()

        # Comprueba que el valor recuperado coincida con el correo electrónico
        assert email_from_header == correo_electronico, 'Correo electronico en header no es igual al correo ingresado'

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()
