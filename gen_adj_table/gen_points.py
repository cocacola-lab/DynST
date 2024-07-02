import pandas as pd
import numpy as np
import argparse

# 读取命令行参数
parser = argparse.ArgumentParser()
# 添加参数
parser.add_argument('--in_dir', type=str)
parser.add_argument('--npz', type=str)
parser.add_argument('--txt', type=str)
parser.add_argument('--out_path', type=str)
args = parser.parse_args()

npz = np.load(args.npz)
df = pd.read_csv(args.txt, sep='\t', index_col='ID')[["Latitude","Longitude"]]
df = df.reindex(npz["stations"])
data = df.loc[npz["stations"]]

latitudes = data['Latitude'].values
longitudes = data['Longitude'].values

points = np.column_stack((latitudes, longitudes))

points[np.isnan(points)] = -1e9
output_file = args.out_path

with open(output_file, 'w') as file:
    file.write(str(len(points))+'\n')
    for row in points:
        file.write(' '.join(map(str, row)) + '\n')

points[points == -1e9] = np.nan

print(f"Data has been successfully written to {output_file}")