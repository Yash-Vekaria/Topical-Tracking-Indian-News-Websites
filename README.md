# Differential Tracking Across Topical Webpages of Indian News Media

This repository is to support the research community (for non-commercial purposes) to obtain topical subpages from the homepage of a website in a semi-automated manner and study tracking across these different topical subpages. The codes open-sourced here are related to our research paper titled "Differential Tracking Across Topical Webpages of Indian News Media" and accepted to the "13th ACM Web Science Conference 2021". However, these can be applied to other contexts and studies by minor modifications. 
This open source framework and dataset can promote further research and help policy makers or fellow researchers to further investigate the understudied Indian news websites for a variety of different purposes. The codes and links to the tools used in our paper are listed below.

**Note: The labelled dataset of the Indian News Websites and crawls using these scripts can be requested from our dataset page [https://nms.kcl.ac.uk/netsys/datasets/india-tracking/](https://nms.kcl.ac.uk/netsys/datasets/india-tracking/) (Please abide to our listed T&C).**

### Abstract
India is experiencing intense political partisanship and sectarian divisions. The paper performs, to the best of our knowledge, the first comprehensive analysis on the Indian online news media with respect to tracking and partisanship. We build a dataset of 103 online, mostly mainstream news websites. With the help of two experts, alongside data from the Media Ownership Monitor of the Reporters without Borders, we label these websites according to their partisanship (Left, Right, or Centre). We study and compare user tracking on these sites with different metrics: numbers of cookies, cookie synchronizations, device fingerprinting, and invisible pixelbased tracking. We find that Left and Centre websites serve more cookies than Right-leaning websites. However, through cookie synchronization, more user IDs, are synchronized in Left websites than Right or Centre. Canvas fingerprinting is used similarly by Left and Right, and less by Centre. Invisible pixel-based tracking is 50% more intense in Centre-leaning websites than Right, and 25% more than Left. Desktop versions of news websites deliver more cookies than their mobile counterparts. A handful of third-parties are tracking users in most websites in this study. This paper, by demonstrating intense web tracking, has implications for research on overall privacy of users visiting partisan news websites in India.

The paper PDF is available [here](https://arxiv.org/pdf/2102.03656.pdf).

### Methodology Implementation
* `Dataset Curation` folder contains crawling scripts used in curating the news websites' list and dataset.
* `Cookie Analysis` folder contains analysis scripts used in cookie-based tracking analysis.
* `Cookie Synchronization` folder contains analysis scripts used in cookie synchronization.
* `Device Fingerprinting` folder contains analysis scripts used in device fingerprinting analysis.
* `Invisible Pixels` folder contains analysis scripts used in invisible pixel-based tracking analysis.

### Citation
Please cite our paper:
```
@misc{agarwal2021spotlight,
title={Under the Spotlight: Web Tracking in Indian Partisan News Websites}, 
author={Vibhor Agarwal and Yash Vekaria and Pushkal Agarwal and Sangeeta Mahapatra and Shounak Set and Sakthi Balan Muthiah and Nishanth Sastry and Nicolas Kourtellis},
year={2021},
eprint={2102.03656},
archivePrefix={arXiv},
primaryClass={cs.CY}
}
```
