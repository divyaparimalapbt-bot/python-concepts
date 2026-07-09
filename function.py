def user_module():
    def login():
        print("login success")
    def logout():
        print("logout sucesfully")

        login()
        login()

    user_module()
    