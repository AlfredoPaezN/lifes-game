class Message:
    # Main method of the class
    def __init__(self, content, message_type):
        self.message_types = {1: "GREETING", 2: "FORBIDDEN", 3: "OPTION"}
        assert isinstance(content, str), f"{content} is not an string"
        assert message_type in self.message_types, f"{message_type} is not known"

        self.__content = content
        self.__message_type = message_type

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def message_type(self):
        return self.message_types[self.__message_type]

    @message_type.setter
    def message_type(self, value):
        self.__message_type = value

    def show(self):
        return print(self.content)

    def __repr__(self):
        return f"{self.message_type} | {self.content}"
