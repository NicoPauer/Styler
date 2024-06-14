class Abstractor:

    def __init__(self, path:str, author:str):

        '''
            ·······························································
            Take like arguments two text strings: file path and author name
            ·······························································
            From a file path extract redaction style by
            the description of author cointaned in it ("authors.csv" format).
        '''
        # I don't know the author until that search for
        self.name = author

        source = open(path, 'r')
        # Save the line with only the data about requested author

        raw = source.readlines()

        self.line = ''

        self.words = []

        for dataLine in raw[1::]:
        # The line with author data contains his name in the text (only columns and row values to optimize)
            if (dataLine.startswith(author)):
            # Update propertie with the new data and accurate data
            # Delete '\n' character because this is redundant
                self.line = dataLine.replace('\n', '')
                # LIST TO SAVE THE MOST USED WORDS BY THE AUTHOR (five column of the CSV file)
                self.words = self.line.split(',')[4].split('.')
                break
        # Ends with the file because at this point doesn't needed any more
        source.close()
        # Delete unnecesary variables
        del source, raw

    def could_write(self, article:str) -> bool:

        '''
            Get the author could have written an text article.

            Return the boolean result of the question.
        '''
        result = False
        # Use the most commons words by the author to check if the probability get ok
        for word in self.words:
            # Make realtime check to fix mistakes
            result = (result or (article.count(word) >= 2))
           
        return result
