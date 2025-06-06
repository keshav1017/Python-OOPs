class chatbook:

    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Deepak"
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def menu(self):
        user_input = input("Welcome to Chatbook !! How would you like to proceed ?\n"
                           "1. Press 1 to signup\n"
                           "2. Press 2 to signin\n"
                           "3. Press 3 to write a post\n"
                           "4. Press 4 to message a friend\n"
                           "5. Press any other to exit\n"
                           "-> ")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_message()
        else:
            exit()

    def signup(self):
        email = input("Enter your email -> ")
        pwd = input("Enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!\n")
        self.menu() 

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter you username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have signed up successfully.")
                self.loggedin = True
            
            else:
                print("Please input correct credentials...")
        print("\n")
        self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    
    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the message -> ")
            print(f"Message has been sent to your {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

# obj = chatbook()