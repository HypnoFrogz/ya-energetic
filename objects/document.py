from datetime import datetime

class Document:

    DocumentNumber = None
    DocumentDate = None
    DocumentExpiresIn = None

    def GetNewDocument(self, documentNumber:str, documentDate:str, documentExpiresIn:str):

        if not all(isinstance(arg, str) for arg in [documentNumber, documentDate, documentExpiresIn]):
            raise TypeError("Все параметры должны быть строками (str)")

        supported_formats = ["%Y-%m-%d", "%d.%m.%Y"]
        parsed_date = None

        for fmt in supported_formats:
            try:
                parsed_date = datetime.strptime(documentDate, fmt)
                break
            except ValueError:
                continue

        if parsed_date is None:
            raise ValueError("DocumentDate должен быть в формате 'ГГГГ-ММ-ДД' или 'ДД.ММ.ГГГГ'")

        formatted_date_document = parsed_date.strftime("%Y-%m-%d")

        for fmt in supported_formats:
            try:
                parsed_date = datetime.strptime(documentExpiresIn, fmt)
                break
            except ValueError:
                continue

        if parsed_date is None:
            raise ValueError("DocumentExpiresIn должен быть в формате 'ГГГГ-ММ-ДД' или 'ДД.ММ.ГГГГ'")

        formatted_expires_document = parsed_date.strftime("%Y-%m-%d")


        self.DocumentNumber = documentNumber
        self.DocumentDate = formatted_date_document
        self.DocumentExpiresIn = formatted_expires_document

        return {'DocumentNumber':self.DocumentNumber,
                'DocumentDate':self.DocumentDate,
                'DocumentExpiresIn':self.DocumentExpiresIn}