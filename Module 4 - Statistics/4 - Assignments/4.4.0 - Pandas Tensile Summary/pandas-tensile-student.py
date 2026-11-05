import numpy as np
import pandas as pd

"""
Pandas Tensile Summary

The tensile data from the previous module was written to a single CSV file with one row per
sample and these columns:

    Sample_Name, Material_Type, Tensile_Strength, Fracture_Strain, Elastic_Modulus, Yield_Strength

Complete the six functions below using Pandas. Each function is graded separately, so you can
work on them in any order. Your functions will be tested on tensile files with different
materials, a different number of samples, and rows in a different order than the course file,
so do not write code that only works for 1045CR, 2024 and PMMA.

Submit this file to Gradescope.
"""


def load_tensile_data(_path: str):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(_path)
    return df


def select_material(_df, _material: str):
    # Keep only rows matching the selected material
    df = _df[_df['Material_Type'] == _material]
    return df


def select_strong(_df, _material: str, _min_yield: float):
    # Keep rows matching both conditions
    df = _df[(_df['Material_Type'] == _material) &
             (_df['Yield_Strength'] > _min_yield)]
    return df


def get_values(_df, _material: str, _column: str):
    # Select material and extract column as NumPy array
    df = select_material(_df, _material)
    values = df[_column].to_numpy()
    return values


def material_statistics(_df, _material: str, _column: str):
    # Select material and column
    df = select_material(_df, _material)

    # Calculate mean and sample standard deviation
    avg = df[_column].mean()
    std = df[_column].std()

    return (avg, std)


def summary_table(_df, _columns: list):
    # Create empty dictionary
    table = {}

    # Find all unique materials
    materials = _df['Material_Type'].unique()

    # Loop through each material
    for material in materials:
        table[material] = {}

        # Loop through each requested column
        for column in _columns:
            avg, std = material_statistics(_df, material, column)
            table[material][column] = (avg, std)

    return table


if __name__ == '__main__':
    # Use this section to check your work. It is not graded and is not run by Gradescope.
    # When it is working you should see (rounded):
    #   Material   Elastic_Modulus        Yield_Strength
    #   1045CR     199.19 +/- 10.69       606.03 +/- 17.53
    #   2024       74.61 +/- 15.63        342.71 +/- 24.2
    #   PMMA       3.09 +/- 0.2           49.41 +/- 3.04
    path_to_file = 'data/tensile/tensile_data.csv'

    data = load_tensile_data(path_to_file)
    if data is None:
        print('load_tensile_data() is not complete yet')
    else:
        print(data)

        table = summary_table(data, ['Elastic_Modulus', 'Yield_Strength'])
        if table is None:
            print('summary_table() is not complete yet')
        else:
            for material in table:
                print(material, end='\t')
                for column in table[material]:
                    (avg, std) = table[material][column]
                    print(column, round(avg, 2), '+/-', round(std, 2), end='\t')
                print()
