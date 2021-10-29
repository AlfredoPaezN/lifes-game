class Message:
    # Main method of the class
    def __init__(self, content, message_type):
        assert isinstance(content, str), f"{content} is not an string"
        assert message_type == 1 or type == 2, f"{type} is not known"

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
        if self.__message_type == 1:
            return "GREETING"
        else:
            return "FORBIDDEN"

    @message_type.setter
    def message_type(self, value):
        self.__message_type = value

    def show(self):
        return self.content
