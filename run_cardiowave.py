import pandas as pd
from cdwave import data
from cdwave import derive
import os

# Load and convert
data_path = 'Parameter_Setup_Calcium_Flux.csv'
df = pd.read_csv(data_path)
loader = data.StandardCSVLoader(data=df)
dataset = loader.transfer()

params_desired = [
    'std_amplitude',
    'std_intensity',
    'std_lambda',
    'std_inner_lambda',
    'up_length',
    'down_length',
    'n_peak',
    'n_all_peaks',
    'maximum',
    'max_intensity',
    'avg_amplitude',
    'avg_intensity',
    'min_intensity',
]

# dataset.parameters_to_calculate = [param for param in params_desired if param in derive.PARAMETERS_AVAILABLE]
# Calculate parameters
# The calculated parameters will be included in the dataset
derive.calc_parameters_for_waveforms(dataset)


# Export parameters
parameter_df = dataset.get_parameter_df()
data_path_save = 'output_data'
if not os.path.exists(data_path_save):
    os.makedirs(data_path_save)
parameter_df.to_csv(os.path.join(data_path_save, 'parameters.csv'))
