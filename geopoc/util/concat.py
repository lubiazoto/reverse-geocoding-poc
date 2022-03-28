import pandas as pd


class Concat:

    def __init__(self):
        pass

    @staticmethod
    def test():
        df1 = pd.DataFrame([['abc', 'rua1', 'nro1', 'site1'], ['def', 'rua1b', 'nro1b', 'site1']])
        print(df1)
        df2 = pd.DataFrame([['abc2', 'rua2', 'nro2', 'site2'], ['def2', 'rua2b', 'nro2b', 'site2']])
        print(df2)
        df3 = pd.concat([df1, df2], axis=0)
        print(df3)


Concat.test()
