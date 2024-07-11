import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Visualisation:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def viz_pairplot(self, id:int,  targets: list, features: list):
        """
        Visualise the relationship between the target and features
        """
        
        for target in targets:
            df_tmp = self.df[self.df['profile_id'] == id]
            # Create a pairplot
            sns.pairplot(df_tmp, x_vars=features, y_vars=target, kind='reg');
            
        plt.show();

    def viz_scatter(self, target: str, feature: str):
        """
        Visualise the relationship between the target and feature
        """
        grpd = {id: df_ for id, df_ in self.df.groupby('profile_id')}
        n_cols = 4
        n_rows = len(grpd) // n_cols + 1

        fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 20))
        for i, (pid, df_) in enumerate(grpd.items()):
            ax = axs[i // n_cols, i % n_cols]
            #df_['motor_speed'].iloc[0:2000].plot(ax=ax)
            df_[feature].plot(ax=ax)
            df_[target].plot(ax=ax)
            ax.set_title(f'profile_id: {pid}')