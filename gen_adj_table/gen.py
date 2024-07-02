import os
import pandas as pd
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--dataset', type=str, default='D05')
args = parser.parse_args()
dataset = args.dataset

dir = f"../Metadata/{dataset}/"

txt_files = [f for f in os.listdir(dir) if f.endswith('.txt') and f.startswith(dataset)]


print("Start merging coordinates file")
df = pd.DataFrame()
for file in txt_files:
    try:
        df1 = pd.read_csv(dir+file, sep='\t', index_col='ID')[["Latitude","Longitude"]]
    except:
        continue
    print(file)
    df1 = df1.dropna()
    # 纵向合并 df 和 df1
    df = pd.concat([df, df1], axis=0, join='outer')
    # 去重
    df = df.loc[~df.index.duplicated(keep='first')]
if not os.path.exists("txt"): 
    os.mkdir("txt")
df.to_csv(f'./txt/{dataset}.txt',sep='\t')
print("Coordinates file merging finished")


in_dir = f"../StaticVersion/{dataset}/"
out_dir = f"{dataset}_adj/"
txt_file = f"txt/{dataset}.txt"

if not os.path.exists(out_dir):
    os.mkdir(out_dir)
if not os.path.exists("cache"): 
    os.mkdir("cache")

print("Start compiling")
os.system("g++ -std=c++11 -O2 gen_edges.cpp -o gen_edges")
print("Compiling finished")

# 读取 dir 下所有 .npz 后缀文件
files = [f for f in os.listdir(in_dir) if f.endswith('.npz')]
files = sorted(files)

# 遍历所有文件，生成边
for file in files:
    print(file)
    save_name = file.split('.')[0]
    print("Start generating points")
    os.system(f"python gen_points.py --in_dir {in_dir} --npz {in_dir+file} --txt {txt_file} --out_path cache/{dataset}_points.txt")
    print("Generating points finished")
    print("Start generating edges")
    os.system(f"gen_edges cache/{dataset}_points.txt {out_dir}/{save_name}.csv")
    print("Generating edges finished")