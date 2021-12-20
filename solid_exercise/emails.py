from abc import ABC, abstractmethod


class IContent:

    @abstractmethod
    def format(self, format, content, available_formats={}):
        if not format.lower() in available_formats:
            raise TypeError(f"Does not support {format}")
        elif content == None:
            raise TypeError('Empty content')
        return available_formats[format.lower()](content)

    @staticmethod
    def myml_format(content):
        return '\n'.join(['<myML>', content, '</myML>'])

    @staticmethod
    def basic_format(content):
        return content.capitalize()

    @staticmethod
    def html_format(content):
        return 'HTML'

FORMAT_MAPPER = {'myml': IContent.myml_format, 'html': IContent.html_format, 'basic': IContent.basic_format}





class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class Email(IEmail):

    def __init__(self, protocol, content_type=None):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)

class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    def format(self, format, available_formats):
        res = super().format(format, self.content, available_formats=available_formats)
        self.content = ":) " * 15 + '\n' + res
        return self.content



# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content.format('MyMl', available_formats=FORMAT_MAPPER))
print(email)
