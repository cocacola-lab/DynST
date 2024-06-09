# DynST: Large-Scale Spatial-Temporal Dataset for Traffic Forecasting with Dynamic Road Networks
This work is under review.

## Table of Contents
  - [Introduction](#introduction)
  - [Dataset Description](#dataset-description)
  - [Download Link](#download-link)
  - [Usage](#usage)
  - [License](#license)

## Introduction
We introduce a large-scale spatial-temporal dataset for traffic forecasting, DynST, encompassing 20.35 billion data points covering approximately 20 years. Unlike traditional datasets that accumulate data over time on a fixed road network, ours provides rich spatial information with dynamically evolving road networks, alongside diverse temporal data. 

This is the offical repo for DynST.

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

Download the dataset from OneDrive and unzip it. If you want to use DynST as traditional setting, e.g., Target-only and Transfer-static setting mentioned in our paper, you should run the `merget.py` to gain the static version of DynST.

Basic usage of the dataset is as follows:

```python
import pandas as pd
import numpy as np


metadata = pd.read_csv('metadata.csv')

data = np.load("data.npz")['data'].astype(np.float32) # the feature data is stored in np.float16 
```

## License
DynST is released under a [CC BY-NC 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0). Our code implementation is released under the [MIT License](https://opensource.org/licenses/MIT). Please obey the regulation of [PEMS](https://pems.dot.ca.gov/?directory=Help&dnode=Help&content=var_terms). 
