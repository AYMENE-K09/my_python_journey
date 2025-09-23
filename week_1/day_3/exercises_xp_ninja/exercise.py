class phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self,other_phone):
        info = f"{self.phone_number} called {other_phone}"
        self.call_history.append(info)
        print(info)

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone):
        info = {
            'to' : other_phone,
            'from': self.phone_number,
            'message content' : input("enter message content: ")
        }
        print(info)
        self.messages.append(info)

    def show_outgoing_messages(self):
        for msg in self.messages:
            if msg['from'] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        for msg in self.messages:
            if msg['to'] == self.phone_number:
                print(msg)

    def show_messages_from(self, number):
        print("85756594744924249240234820489")
        for msg in self.messages:
            if (msg['from']) == number:
                print(msg)


person = phone("333-3333-333")
person.call("222-2222-222")
person.send_message("222-2222-222")
person.send_message("222-xxx-222")
person.send_message("222-mmmm-222")
person.show_call_history()
person.show_outgoing_messages()
person.show_incoming_messages()
person.show_messages_from("222-2222-222")


