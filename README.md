# Differential Tracking Across Topical Webpages of Indian News Media

This repository is to support the research community (for non-commercial purposes) to obtain topical subpages from the homepage of a website in a semi-automated manner and study tracking across these different topical subpages. The codes open-sourced here are related to our research paper titled _"Differential Tracking Across Topical Webpages of Indian News Media"_ and accepted to the _"13th ACM Web Science Conference 2021"_. However, these can be applied to other contexts and studies by minor modifications. 
Our DiBETS Methodology (Dictionary-Based Extraction of Topical Subpages), open source framework and dataset can promote further research and help policy makers or fellow researchers to supplement a deeper investigation of the understudied Indian news websites for a variety of different purposes. The codes and link to the tools used in our paper are listed below. This work is an extension to our research titled _"Under the Spotlight: Web Tracking in Indian Partisan News Websites"_. For further details rearding this previous work, you may visit this [page](https://nms.kcl.ac.uk/netsys/datasets/india-tracking/).

**Note: The topic labelled dataset of the subpages extracted from Indian News Websites and the manually created Topical Dictionary for DiBETS along with OpenWPM crawls can be requested from our dataset page [https://nms.kcl.ac.uk/netsys/datasets/india-topic/](https://nms.kcl.ac.uk/netsys/datasets/india-topic/) (Please abide to our listed T&C).**

### Abstract
Online user privacy and tracking have been extensively studied in recent years, especially due to privacy and personal data-related legislations in the EU and the USA, such as the General Data Protection Regulation, ePrivacy Regulation, and California Consumer Privacy Act. Research has revealed novel tracking and personal identifiable information leakage methods that first- and third-parties employ on websites around the world, as well as the intensity of tracking performed on such websites. However, for the sake of scaling to cover a large portion of the Web, most past studies focused on homepages of websites, and did not look deeper into the tracking practices on their topical subpages. The majority of studies focused on the Global North markets such as the EU and the USA. Large markets such as India, which covers 20% of the world population and has no explicit privacy laws, have not been studied in this regard.

We aim to address these gaps and focus on the following research questions: Is tracking on topical subpages of Indian news websites different from their homepage?
Do third-party trackers prefer to track specific topics? How does this preference compare to the similarity of content shown on these topical subpages? To answer these questions, we propose a novel method for automatic extraction and categorization of Indian news topical subpages based on the details in their URLs. We study the identified topical subpages and compare them with their homepages with respect to the intensity of cookie injection and third-party embeddedness and type. We find differential user tracking among subpages, and between subpages and homepages. We also find a preferential attachment of third-party trackers to specific topics. Also, embedded third-parties tend to track specific subpages simultaneously, revealing possible user profiling in action.

### DiBETS Methodology Implementation
* `get_homepage_content.py` script checks if a input website's homepage URL is valid and crawls its content.
* `extract_internal_external_urls` script extracts all the urls from the HTML content of the homepage of a website (obtained from the above code) and segregates them into internal and external URLs. It stores internal URLs and external URLs of a website separately.
* `plot_parameter_histogram.py` script helps to determine the cut-off (i.e., the separating point of the two modes in a bi-modal distribution) for each URL parameter by plotting its distribution for the internal URLs.
* `filter_internal_urls.py` script uses the parameters and associated cut-offs inferred using the above code. These cut-offs ensure that only section URLs are retained as a separate .txt file (i.e., article urls are rejected).
* `url_topical_categorization.py` script uses a manually generated topical dictionary and word2Vec approach to assign a topic to each of the filtered internal URLs for each website and predicts a single-best URL for each topic per website as the final output.

For additional details of our DiBETS model, please refer to the paper. The paper PDF is available [here](https://arxiv.org/pdf/2103.04442.pdf).

### Citation
Please cite our paper:
```
@inproceedings{vekaria2021differential,
  title={Differential Tracking Across Topical Webpages of Indian News Media},
  author={Vekaria, Yash and Agarwal, Vibhor and Agarwal, Pushkal and Mahapatra, Sangeeta and Muthiah, Sakthi Balan and Sastry, Nishanth and Kourtellis, Nicolas},
  booktitle={Proceedings of the ACM WebSci},
  year={2021}
}
```
