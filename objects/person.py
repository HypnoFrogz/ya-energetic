from datetime import datetime

class Person:

    FirstName = None
    LastName = None
    Address = None
    DocumentNumber = None
    DocumentDate = None

    def GetNewPerson(self, FirstName: str, LastName: str, Address: str, DocumentNumber: str, DocumentDate: str):
        # Проверка, что все значения — строки
        if not all(isinstance(arg, str) for arg in [FirstName, LastName, Address, DocumentNumber, DocumentDate]):
            raise TypeError("Все параметры должны быть строками (str)")

        # Попытка распарсить дату в одном из допустимых форматов
        supported_formats = ["%Y-%m-%d", "%d.%m.%Y"]
        parsed_date = None

        for fmt in supported_formats:
            try:
                parsed_date = datetime.strptime(DocumentDate, fmt)
                break
            except ValueError:
                continue

        if parsed_date is None:
            raise ValueError("DocumentDate должен быть в формате 'ГГГГ-ММ-ДД' или 'ДД.ММ.ГГГГ'")

        formatted_date = parsed_date.strftime("%Y-%m-%d")

        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        self.DocumentNumber = DocumentNumber
        self.DocumentDate = formatted_date

        return {'FirstName':self.FirstName,
                'LastName':self.LastName,
                'Address':self.Address,
                'DocumentNumber':self.DocumentNumber,
                'DocumentDate':self.DocumentDate}

"""p = Person()
print(p.GetNewPerson("Герасимчук", 'Кирилл', 'Москва', '1234-1234','24.05.1996'))"""