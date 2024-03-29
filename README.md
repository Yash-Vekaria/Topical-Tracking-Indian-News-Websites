# Differential Tracking Across Topical Webpages of Indian News Media

This repository is to support the research community (for non-commercial purposes) to obtain topical subpages from the homepage of a website in a semi-automated manner and study tracking across these different topical subpages. The codes open-sourced here are related to our research paper titled [_"Differential Tracking Across Topical Webpages of Indian News Media"_](https://nms.kcl.ac.uk/netsys/datasets/india-topic/). The codes and link to the tools used in our paper are detailed below. This work is an extension to our research titled [_"Under the Spotlight: Web Tracking in Indian Partisan News Websites"_](https://arxiv.org/pdf/2102.03656.pdf). For further details regarding this previous work, you may visit this [page](https://nms.kcl.ac.uk/netsys/datasets/india-tracking/).


**Note: The topic labeled dataset of the subpages extracted from Indian News Websites by our model - DiBETS (Dictionary-Based Extraction of Topical Subpages) along with the [OpenWPM](https://github.com/mozilla/OpenWPM) crawls and gathered cookie information can be requested from our dataset page [https://nms.kcl.ac.uk/netsys/datasets/india-topic/](https://nms.kcl.ac.uk/netsys/datasets/india-topic/) (Please cite our paper and abide to our listed T&C).**

<p align="center">
  <img width="550" height="550" src="https://user-images.githubusercontent.com/30694521/120553423-1a082c80-c416-11eb-930d-d92d95f0fc3c.png">
</p>

### Pre-requisites
1. Installing certain python packages is essential to run the below mentioned codes. Use the following command to install necessary python modules:
   ```
   pip install -r requirements.txt
   ```
2. DiBETS is a _Word2Vec-enhanced_ dictionary-based model. We use _model.bin_ file of the downloaded pre-trained Word2Vec model specified below from the website: [_http://vectors.nlpl.eu/repository/_](http://vectors.nlpl.eu/repository/)
   ![image](https://user-images.githubusercontent.com/30694521/115953533-aebf6680-a509-11eb-9ada-b9d2a4f23f75.png)
3. If your study is in Indian context and uses the same 112 Indian News Websites that we used, then you may use the following manually generated dictionary from top 25 Indian News Websites (based on followers of their FB pages). For applying our work to some other context, you may refer to our dictionary and create a similar one for your context using top _x_ websites for the training purposes.
   ```
   manual_topical_dictionary.csv
   ```
   Following is the description of different columns in the above _.csv_:
   - `id`: It uniquely identifies the news website of the train set.
   - `news_website_homepage`: URL of the homepage of the news website.
   - `extracted_keywords`: Keywords and other related words/phrases extracted or identified based on the URL meta data (i.e., the words present in the URL itself) depending upon the topic to which the given internal URL seems related to as per the human experts' discretion.
   - `internal_urls`: The internal URLs of the train website extracted by DiBETS.
   - `manual_topic_label`: The topical label assigned by the human expert based on the topic to which the URL seems associated with. The expert may visit the actual website to assign the most suitable topic (in case meta-data doesn't present a clear picture).
4. Create the following empty directories inside the folder `DiBETS Methodology Codes` before implementing DiBETS (since these will be used by the DiBETS codes to generate and utilize the intermediate outputs).
   * `HTML Dump`
   * `Internal URLs`
   * `External URLs`
   * `Filtered URLs`
5. Our study in Indian Context consisted of 112 Indian News Websites, whose homepage URLs were specified in the following _.txt_ file. However, for applying DiBETS to some other context, please specify the homepage URLs of those websites in this file.
   ```
   websites_homepage_urls.txt
   ```
   
   
### DiBETS Methodology Implementation
1. `get_homepage_content.py` script checks if an input website's homepage URL is valid and crawls its content.
2. `extract_internal_external_urls` script extracts all the urls from the HTML content of the homepage of a website (obtained from the above code) and segregates them into internal and external URLs. It stores internal URLs and external URLs of a website separately.
3. `plot_parameter_histogram.py` script helps to determine the cut-off (i.e., the separating point of the two modes in a bi-modal distribution) for each URL parameter by plotting its distribution for the internal URLs.
4. `filter_internal_urls.py` script uses the parameters and associated cut-offs inferred using the above code. These cut-offs ensure that only section URLs are retained as a separate .txt file (i.e., article urls are rejected).
5. `url_topical_categorization.py` script uses a manually generated topical dictionary and word2Vec approach to assign a topic to each of the filtered internal URLs for each website and predicts a single-best URL for each topic per website as the final output.

For additional details about the DiBETS model, please refer to our paper. The paper PDF is available [here](https://arxiv.org/pdf/2103.04442.pdf).

### Citation
Please cite our papers:
```
@inproceedings{10.1145/3447535.3462497,
author = {Vekaria, Yash and Agarwal, Vibhor and Agarwal, Pushkal and Mahapatra, Sangeeta and Balan Muthiah, Sakthi and Sastry, Nishanth and Kourtellis, Nicolas},
title = {Differential Tracking Across Topical Webpages of Indian News Media},
year = {2021},
isbn = {9781450383301},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3447535.3462497},
doi = {10.1145/3447535.3462497},
abstract = {Online user privacy and tracking have been extensively studied in recent years, especially due to privacy and personal data-related legislations in the EU and the USA, such as the General Data Protection Regulation, ePrivacy Regulation, and California Consumer Privacy Act. Research has revealed novel tracking and personally identifiable information leakage methods that first- and third-parties employ on websites around the world, as well as the intensity of tracking performed on such websites. However, for the sake of scaling to cover a large portion of the Web, most past studies focused on homepages of websites, and did not look deeper into the tracking practices on their topical subpages. The majority of studies focused on the Global North markets such as the EU and the USA. Large markets such as India, covering 20% of the world population and has no explicit privacy laws, have not been studied in this regard. We aim to address these gaps and focus on the following research questions: Is tracking on topical subpages of Indian news websites different from their homepage? Do third-party trackers prefer to track specific topics? How does this preference compare to the similarity of content shown on topical subpages? To answer these questions, we propose a novel method for semi-automatic extraction and categorization of Indian news topical subpages based on the details in their URLs. We study the identified topical subpages and compare them with their homepages with respect to the intensity of cookie injection and third-party embeddedness and type. We find differential user tracking among subpages, and between subpages and homepages. We also find a preferential attachment of third-party trackers to specific topics. Also, embedded third-parties tend to track specific subpages simultaneously, revealing possible user profiling in action. },
booktitle = {13th ACM Web Science Conference 2021},
pages = {299–308},
numpages = {10},
keywords = {Indian news websites, User web tracking, Topical tracking, Homepages, Topical subpages, Cookies, Third-party preferences},
location = {Virtual Event, United Kingdom},
series = {WebSci '21}
}
```
```
@inproceedings{agarwal2021under,
  title={Under the Spotlight: Web Tracking in Indian Partisan News Websites},
  author={Agarwal, Vibhor and Vekaria, Yash and Agarwal, Pushkal and Mahapatra, Sangeeta and Set, Shounak and Muthiah, Sakthi Balan and Sastry, Nishanth and Kourtellis, Nicolas},
  booktitle={Proceedings of the International AAAI Conference on Web and Social Media},
  volume={15},
  pages={26--37},
  year={2021}
}
```
