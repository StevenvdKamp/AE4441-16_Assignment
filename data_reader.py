import pandas as pd

class Case():

    def __init__(self, FILE_NAME):
        self.FILE_NAME = FILE_NAME

        self.df_node_connections = pd.read_excel(FILE_NAME, sheet_name='Node Connections')
        self.df_node_properties = pd.read_excel(FILE_NAME, sheet_name='Node Properties')
        self.df_machine_properties = pd.read_excel(FILE_NAME, sheet_name='Machine Properties')

    def get_s_dict(self):
        return pd.Series(self.df_machine_properties['Start Depot'].values, index=self.df_machine_properties['Machine']).to_dict()

    def get_z_dict(self):
        return pd.Series(self.df_machine_properties['End Depot'].values, index=self.df_machine_properties['Machine']).to_dict()



    def get_travel_cost(self, i, j):
        return 0

    def get_travel_duration(self, i, j):
        return 0

case = Case("test_case_1.xlsx")

print(case.get_s_dict())