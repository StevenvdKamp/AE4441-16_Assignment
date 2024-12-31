import pandas as pd

class VRP():

    def __init__(self, FILE_NAME):
        self.FILE_NAME = FILE_NAME

        self.df_node_connections = pd.read_excel(FILE_NAME, sheet_name='Node Connections')
        self.df_node_properties = pd.read_excel(FILE_NAME, sheet_name='Node Properties')
        self.df_machine_properties = pd.read_excel(FILE_NAME, sheet_name='Machine Properties')

    def get_s_dict(self):
        return pd.Series(self.df_machine_properties['Start Depot'].values, index=self.df_machine_properties['Machine']).to_dict()

    def get_z_dict(self):
        return pd.Series(self.df_machine_properties['End Depot'].values, index=self.df_machine_properties['Machine']).to_dict()

    def get_a_dict(self, scaling_factor=1):
        return pd.Series(self.df_node_properties['Working Duration'].values * scaling_factor, index=self.df_node_properties['Node']).to_dict()

    def get_u_dict(self, scaling_factor=1):
        a_dict = pd.Series(self.df_node_properties['Working Duration'].values * scaling_factor, index=self.df_node_properties['Node']).to_dict()

        return {key: 480 - value for key, value in a_dict.items()}

    def get_c_dict(self):
        return pd.Series(self.df_node_properties['Customer Cost Coefficient'].values, index=self.df_node_properties['Node']).to_dict()

    def get_d_dict(self, scaling_factor=1):
        start_nodes = self.df_node_connections['From'].values
        end_nodes = self.df_node_connections['To'].values
        travel_costs = self.df_node_connections['Cost'].values

        travel_costs_dict = {}

        for i in range(len(start_nodes)):
            travel_costs_dict[(start_nodes[i], end_nodes[i])] = travel_costs[i] * scaling_factor
            travel_costs_dict[(end_nodes[i], start_nodes[i])] = travel_costs[i] * scaling_factor

        return travel_costs_dict

    def get_r_dict(self, scaling_factor=1):
        start_nodes = self.df_node_connections['From'].values
        end_nodes = self.df_node_connections['To'].values
        travel_times = self.df_node_connections['Time [min]'].values

        travel_times_dict = {}

        for i in range(len(start_nodes)):
            travel_times_dict[(start_nodes[i], end_nodes[i])] = travel_times[i] * scaling_factor
            travel_times_dict[(end_nodes[i], start_nodes[i])] = travel_times[i] * scaling_factor

        return travel_times_dict

    def get_Ns_set(self):
        return set(self.df_machine_properties['Start Depot'].values)

    def get_Nz_set(self):
        return set(self.df_machine_properties['End Depot'].values)

    def get_N_set(self):
        Ns = set(self.df_machine_properties['Start Depot'].values)
        Nz = set(self.df_machine_properties['Start Depot'].values)
        Na = set(self.df_node_properties['Node'].values)

        Ns_and_Nz = Ns.union(Nz)

        return Na.difference(Ns_and_Nz)

    def get_Na_set(self):
        return set(self.df_node_properties['Node'].values)

    def get_M_set(self):
        return set(self.df_machine_properties['Machine'].values)