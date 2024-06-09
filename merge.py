import numpy as np
import os
import datetime
import argparse



    
file1 = None
station1 = None
data1    = None
start = None
end = None
count = 1


get_date_from_file_name = lambda x: '_'.join(x.split(".")[0].split("_")[-3:])
get_datestamp = lambda x: datetime.datetime.strptime(x, "%Y_%m_%d")
get_datestamp_from_file_name = lambda x: get_datestamp(get_date_from_file_name(x))
get_date_str  = lambda x: x.strftime("%Y_%m_%d")

def read_npz(base, file):
    path = os.path.join(base, file)
    data = np.load(path, allow_pickle=True)
    station = data['stations']
    data = data['data']
    
    return data, station

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", type=str, default="d03")
    args = parser.parse_args()
    
    
    base = args.input+"_processed"
    target = args.input+"_merge"
    
    print("now starting merge dataset")
    print("base directory ", base)
    print("target directory", target)
    
    
    if not os.path.exists(base):
        print(f"Path {base} does not exist.")
        exit(1)
        # or create the folder, call process func first
    if not os.path.exists(target):
        os.makedirs(target)
   
    #  should keep file ls is sorted
    file_ls = sorted(os.listdir(base))

    file1 = None
    station1 = None
    data1    = None
    start = None
    end = None
    count = 1
    day = None 
    for file in file_ls:
        if not file.endswith(".npz"):
            continue
        elif file.endswith(" (1).npz"):
            continue
        elif file.endswith(").npz"):
            continue
        
        if not file1:
            file1 = file
            data1, station1 = read_npz(base, file1)
            start = get_date_from_file_name(file1)
            end   = start
            day = get_datestamp(start)
            continue
        day = day + datetime.timedelta(days=1)
        file2 = file

        
        
        data2, station2 = read_npz(base, file2)
        if day == get_datestamp_from_file_name(file2) and len(station2) == len(station1) and ((station1 == station2).sum() == len(station1)):
            # same stations, merge two files
            data1 = np.concatenate([data1, data2], axis=0)
            end = get_date_from_file_name(file2)
            count += 1
        else:
            # different stations, save the first file with start and end date joined the base path
            print(f"{start}_{end} ", count, " days merged.")
            # start day to end day with count days merged
            path = os.path.join(target, f"{start}_{end}_{count}.npz")    
            np.savez_compressed(path, data=data1, stations=station1)
            file1, station1, data1 = file2, station2, data2
            start = get_date_from_file_name(file1)
            end = start
            count = 1
            day = get_datestamp(start)
    
    # merge final batch npz file
    if len(station1) > 0: 
        print(f"{start}_{end} ", count, " days merged.")
        # start day to end day with count days merged
        path = os.path.join(target, f"{start}_{end}_{count}.npz")    
        np.savez_compressed(path, data=data1, stations=station1)
        file1, station1, data1 = file2, station2, data2
        start = get_date_from_file_name(file1)
        end = start
        count = 1
        day = get_datestamp(start)
    
    print("Finished processing ", base)
