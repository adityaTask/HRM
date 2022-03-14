from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_by_id = 'txtUsername'
        self.password_by_id = 'txtPassword'
        self.login_button_by_id = 'btnLogin'
        self.welcome_by_id = 'welcome'
        self.logout_by_link_text = 'Logout'
        self.invalid_username_by_id = 'spanMessage'
        self.invalid_username_message = 'Invalid credentials'

    def enter_user_name(self,username):
        self.send_keys(data=username , locator=self.username_by_id)

    def enter_password(self,password):
        self.send_keys(data=password,locator=self.password_by_id)

    def click_login_button(self):
        self.element_click(locator=self.login_button_by_id)

    def login(self,username,password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login_button()

    def logout(self):
        self.element_click(self.welcome_by_id)
        self.element_click(self.logout_by_link_text,'LinkText')

    def check_valid_login(self):
        return self.is_displayed(self.welcome_by_id)

    def check_valid_logout(self):
        return self.is_displayed(self.login_button_by_id)

    def check_invalid_login(self):
        return self.invalid_username_message == self.get_text(self.invalid_username_by_id)


