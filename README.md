# DynST: Large-Scale Spatial-Temporal Dataset for Traffic Forecasting with Dynamic Road Networks
This work is under review.

## Table of Contents
  - [Introduction](#introduction)
  - [Dataset Description](#dataset-description)
  - [Download Link](#download-link)
  - [Usage](#usage)
  - [License](#license)
  - [Charts&Figures](#charts-and-figures)

## Introduction
We introduce a large-scale spatial-temporal dataset for traffic forecasting, DynST, encompassing 20.35 billion data points covering approximately 20 years. Unlike traditional datasets that accumulate data over time on a fixed road network, ours provides rich spatial information with dynamically evolving road networks, alongside diverse temporal data. 

This is the offical repo for DynST.

You can check the basic temporal statistical analysis results in `charts/`. 

As the PEMS official website is often down, we provide a snapshot of the regulation webpage.

## Dataset Description

- **Number of Records:** DynST record 12,220 sensors, over 20 years, totally 20.35 billion data points.
- **Features:** The main feature data has two files, `data` and `stations`. `data` is the processed data. `stations` is the Sensor ID. They are stored in np.float16 and np.int32 format respectively.
- **Format:** The main feature data is compress in `npz` farmat. The adjacency matrix and the metadata is stored as `csv` file. They are all compiled as zip package.
- **Size:** Totally about 79GB.

## Download Link

You can download the dataset from the following [OneDrive link](https://32znz5-my.sharepoint.com/:f:/g/personal/planckchang_32znz5_onmicrosoft_com/Es7CpYcA01dOo2z-mxkFNrcBHIwcoWKM7wJiiYwiT5ff4w?e=XPndWo). The password is `BJTUcocacola`.

The directory tree is:
``` plaintext
├── dataset/
│   ├── DynamicVersion/       # Dynamic version of DynST
│   │   ├── D03.zip           # 9 districts data compiled as zip package
│   │   ├── D04.zip
│   │   ├── DXX.zip
│   ├── Metadata.zip            # Metadata file
│   └── AdjacencyMatrix.zip     # Adjacency matrix file
```

## Usage

Download the dataset from OneDrive and unzip it. If you want to use DynST as traditional setting, e.g., Target-only and Transfer-static setting mentioned in our paper, you should run the `merge.py` to gain the static version of DynST.

Basic usage of the dataset is as follows:

```python
import pandas as pd
import numpy as np


metadata = pd.read_csv('metadata.csv')

data = np.load("data.npz")['data'].astype(np.float32) # the feature data is stored in np.float16 
```

run the `merge.py`

```shell
python merge.py -i d03
```

generate ajacency table.

```shell
cd gen_adj_table
python gen.py --dataset D05
```


## License
DynST is released under a [CC BY-NC 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0). Our code implementation is released under the [MIT License](https://opensource.org/licenses/MIT). Please obey the regulation of [PEMS](https://pems.dot.ca.gov/?directory=Help&dnode=Help&content=var_terms). 

## Charts and Figures

### Temporal Characteristics

To help users better understand the temporal characteristics of the dataset, we have conducted several statistical analyses and generated corresponding charts. Each chart is linked below:

For each sub-dataset, we calculate the spatial average of the data at each time frame for further use.

#### Year View

Annual variations in average traffic flow. Initially, we calculated the daily average for each time segment, from which the annual average was subsequently derived.

| Chart Link |
|------------|
| [Annual Patterns of Average Traffic Flow](charts/annual_patterns_of_avg_traffic.pdf) |
| [Annual Patterns of Average Occupancy](charts/annual_patterns_of_avg_occupancy.pdf) |
| [Annual Patterns of Average Speed](charts/annual_patterns_of_avg_speed.pdf) |

#### Week View

Difference between weekdays and weekends

| Chart Link |
|------------|
| [2001 WeekView](charts/2001_weekview.pdf) |
| [2002 WeekView](charts/2002_weekview.pdf) |
| [2003 WeekView](charts/2003_weekview.pdf) |
| [2004 WeekView](charts/2004_weekview.pdf) |
| [2005 WeekView](charts/2005_weekview.pdf) |
| [2006 WeekView](charts/2006_weekview.pdf) |
| [2007 WeekView](charts/2007_weekview.pdf) |
| [2008 WeekView](charts/2008_weekview.pdf) |
| [2009 WeekView](charts/2009_weekview.pdf) |
| [2010 WeekView](charts/2010_weekview.pdf) |
| [2011 WeekView](charts/2011_weekview.pdf) |
| [2012 WeekView](charts/2012_weekview.pdf) |
| [2013 WeekView](charts/2013_weekview.pdf) |
| [2014 WeekView](charts/2014_weekview.pdf) |
| [2015 WeekView](charts/2015_weekview.pdf) |
| [2016 WeekView](charts/2016_weekview.pdf) |
| [2017 WeekView](charts/2017_weekview.pdf) |
| [2018 WeekView](charts/2018_weekview.pdf) |
| [2019 WeekView](charts/2019_weekview.pdf) |
| [2020 WeekView](charts/2020_weekview.pdf) |
| [2021 WeekView](charts/2021_weekview.pdf) |
| [2022 WeekView](charts/2022_weekview.pdf) |
| [2023 WeekView](charts/2023_weekview.pdf) |
| [2024 WeekView](charts/2024_weekview.pdf) |

