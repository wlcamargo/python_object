import pandas as pd

class Excel():
    def __init__(self):
        self.read_data()
        self.add_column()
        self.create_new_spreadsheet()
      
    def read_data(self):
        self.df = pd.read_excel('pedidos.xlsx')
         
    def add_column(self):
        self.df['prioridade'] = self.df['categoria'].apply(self.set_column_python)
        
    def set_column_python(self, categoria):
        if categoria == 'bug':
            return 'prioridade alta'
        else:
            return 'prioridade baixa'
        
    def create_new_spreadsheet(self):
        self.df.to_excel('pedidos_priorizados.xlsx', index=False)
        print('planilha nova criada com sucesso!')
    
start = Excel()
    