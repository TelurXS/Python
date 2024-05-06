import pandas as pd

class CsvHandler:
    def __init__(self, path: str) -> None:
        self.__path = path
        return
    
    def read(self) -> pd.DataFrame:
        data = pd.read_csv(self.__path)
        data['numbers'] = data['numbers'].apply(lambda x: x.split('|'))
        return data
    
    def write(self, data: pd.DataFrame) -> None:
        data = data.copy()
        data['numbers'] = data['numbers'].apply(lambda x: '|'.join(x))
        data.to_csv(self.__path, index=False)
