class programmer:
    company = "Microsoft"

    def __init__(self, name, langueage):
        self.name = name
        self.language = langueage

harry = programmer("harry", "python")
print(harry.company,harry.name, harry.language)
rohan = programmer("rohan", "java")
print(rohan.company,rohan.name, rohan.language)