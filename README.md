# InclusiveCodingFestivalJA
Our submission for the inclusive coding festival - team J&amp;A.

Description:
A distributed denial-of-service (DDoS) attack is an attack that targets servers and websites by interfering with network services. A number of bots bombard a website or service with HTTP requests and traffic during a DDoS attack. Basically, during an attack, several computers attack a single computer and drive away authorized users. As a result, service may be prolonged or otherwise interfered with. A benign attack is simply normal traffic on a website that is not malicious in nature, like a DDoS attack. Our goal is to use our data set of 12.79 million attacks (DDoS and Benign) to predict DDoS attacks based on a number of predictors. The data set we are using comes from 3 separate datasets open to the public by the Canadian Insititute for Cybersecurity.

The current predictors are as follows: 
"country_name_{insert country name dummy here}
"Flow Duration"
"Flow IAT Min"
"Src Port"
"Tot Fwd Pkts”
"Init Bwd Win Byts"
"Label": type of attack (DDoS or Benign)

In order to extract the location from the IP addresses, a get request will be performed from a website (https://geolocation-db.com/jsonp/) that extracts IP address locations. The variable of interest in this request is just the country name. 

An efficient machine learning approach, known as XGBoost, frequently outperforms competing models. XGBoost stands for "Extreme Gradient Boosting", and is a scalable, distributed gradient-boosted decision tree (GBDT) model. In addition to offering parallel tree boosting, it is the top machine learning package for regression, classification, and ranking issues. We will use this model in our submission. Additionally, since “country_name” is not a numerical value, the variable needs to be transformed into a dummy variable before entering it in the algorithms. 

Python will be the programming language used, while also incorporating Microsoft Azure (when possible, mostly as an IDE) and Github. In keeping in line with the project's correct git and coding practices guidelines, a goal of this project will be to learn the correct GitHub/coding practices. Another goal will be figuring out how to host the dataset as it is extremely large. A smaller portion of the dataset will be used as a sample to test the code before using the full dataset. Also, if time permits, a geolocation map of attacks may be created using either python or Google Data Studio. 

The paper outlining how others approached this dataset: https://www.ijcseonline.org/pdf_paper_view.php?paper_id=4011&28-IJCSE-06600.pdf

The merged dataset is available at: 
https://www.kaggle.com/datasets/devendra416/ddos-datasets
The base Datasets are available at:
CSE-CIC-IDS2018-AWS: https://www.unb.ca/cic/datasets/ids-2017.html
CICIDS2017: https://www.unb.ca/cic/datasets/ids-2018.html
CIC DoS dataset(2016) : https://www.unb.ca/cic/datasets/dos-dataset.html

Sources:
https://www.microsoft.com/en-us/security/business/security-101/what-is-a-ddos-attack
https://www.nvidia.com/en-us/glossary/data-science/xgboost/
https://www.mygreatlearning.com/blog/xgboost-algorithm/
https://towardsdatascience.com/performance-metrics-confusion-matrix-precision-recall-and-f1-score-a8fe076a2262#:~:text=The%20confusion%20matrix%2C%20precision%2C%20recall%2C%20and%20F1%20score,values%20on%20one%20axis%20and%20predicted%20on%20another.

