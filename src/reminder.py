class PrefixedReminder:

    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    def__init__(self.text):
        super().__init__(prefix="Please remember to ")