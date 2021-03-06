# Deep Learning in NILM in Taiwan
Digital Transformation Institute / III is the FIRST team in Taiwan applying Deep Learning in NILM. Our goal is to help Taiwanese to save energy in a low-cost way.

https://web.iii.org.tw/About/Department.aspx?dp_sqno=15&fm_sqno=36

Due to the No-Nuclear policy in Taiwan, saving energy, especially domestic energy, is urge for Taiwan.

# III_PowerNILM_DeepLearning
III_PowerNILM_DeepLearning is a module for estimating the energy consumed by individual appliances from aggregate consumption data. In this project, unlike REDD or UKDALE, the sample rate of III's power data is 60/sec or 180/sec.

In this project, we only take five appliances into consideration:
- [ ] AC
- [ ] Frideg
- [ ] Washing Machine
- [ ] TV
- [ ] bottle warmer 

Other appliances are labeled as others.

# training process 
We take REDD dataset as reference, which can be found in the below link:

http://redd.csail.mit.edu/

Here is the brief summary:

|database|   |data/REDD.foramt|   | data/HDF.format|  | models and output |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|   | `III.py`|  |`III_convert_hdf.py`|  | `train.py`|  |

The first row represents folder name except for database, and database represents the db in SQL.<br />
The second row represents python codes which use the data from the left-above folder and save the resulting files in the right-above folder.

## From database to REDD format
- [ ] III.py 

## From REDD format to HDF
- [ ] III_convert_hdf.py:<br />
`./III_convert_hdf.py -d data_type`<br />
where `data_type` is III, III_Commercial or HEMS_PongHu. The output will be named 'data_type_yy_mm_dd.h5' in the data folder.

## train
- [ ] train.py 

## Model
- [ ] dae.py 
- [ ] LSTM*.py 
- [ ] Washing Machine > Fridge > AC >>> TV >>> bottle warmer

# Evaluate the models
|eval/test_data|   |eval/model_name_folder| 
|:---:|:---:|:---:|
|   | `evaluation_model.py`|  |

## evaluate
- [ ] evaluation_model.py

# Future(by the end of this year)
Develop a hybrid DNN-HMM model to our dataset

# Challanges
Now, we are at THE VERY BEGINNING. One of our big challanges is to estimate the consumption of air conditioner from aggregate consumption, because electric behavior of air conditioners(AC) vary with brand, environmental temperature and size. In the future, we must enhance our model performance to the point with acc above 70% over the dataset provided by Taiwan Power Company with sample rate 15/min.

# Python note
We use pandas==0.16.2 instead of 0.19.2 . Though pandas==0.19.2 is better in resampling, neuralnilm is based on pandas==0.16.2. There is a bug when using pandas==0.19.2
