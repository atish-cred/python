class ChaiUtils:
    def clean_ingredients(self, text):
        return [item.strip() for item in text.split(",")]

raw = "water , milk , ginger , honey"
obj = ChaiUtils()
cleaned = obj.clean_ingredients(raw)
print(cleaned)


class ChaiUtilsNew:
    @staticmethod # this decorator needs to be define for static method 
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

cleaned = ChaiUtilsNew.clean_ingredients(raw)
print(cleaned)

