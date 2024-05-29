# data


## object of the crawler

- root website: https://www.haodf.com/hospital/list.html

- last update time of crawling: 2024.3.23

- steps

  - get the  root URL of each province

    for instance, 北京: https://www.haodf.com/hospital/list-11.html

  - from the root URL, get the name and sub URL of each hospital

    for instance, 中日医院: https://www.haodf.com/hospital/72.html

  - from the sub URL, get the comment url

    for instance, https://www.haodf.com/hospital/72/pingjia.html

  - from the comment URL, get JSON data from the dynamic list

  - from the pageInfo, get the whole information which is essential owing to it provides the basic information of the dynamic list

  - from the commentInfoList, get complete information of each comment



## descriptive statistics

- 数据总数：606947

- 医院总数：2344

| hospital_name                          | count |
| :------------------------------------- | ----: |
| 上海交通大学医学院附属仁济医院（东院） | 15072 |
| 上海第九人民医院                       | 14759 |
| 复旦大学附属华山医院                   | 14101 |
| 复旦大学附属肿瘤医院                   | 12345 |
| 北医三院                               | 11119 |
| 北京协和医院                           |  9917 |
| 北京大学人民医院                       |  9212 |
| 中日医院                               |  7746 |
| 中国医学科学院肿瘤医院                |  7680 |
| 上海中山医院                           |  7303 |



- 医生总数：33773
- 医生排名：

|  doctor_ID | count |
| ---------: | ----: |
|      61271 |  1268 |
|     131963 |  1077 |
| 6964463739 |   989 |
| 4425451596 |   986 |
|  115678048 |   832 |
|      17597 |   825 |
| 2320248143 |   801 |
|     274384 |   790 |
|  155415911 |   789 |
|     279611 |   788 |

- 城市数：287

- 城市评论数：

| hospital_city |  count |
| :------------ | -----: |
| 上海市        | 157467 |
| 北京市        | 142165 |
| 广州市        |  33288 |
| 南京市        |  22785 |
| 天津市        |  19702 |
| 济南市        |  19632 |
| 杭州市        |  19620 |
| 西安市        |  16572 |
| 武汉市        |  15094 |
| 沈阳市        |  15082 |



- 来源地数：361

- 来源地评论数：

| origin_city | count |
| :---------- | ----: |
| 上海市      | 84315 |
| 北京市      | 75834 |
| 天津市      | 15530 |
| 广州市      | 14568 |
| 杭州市      | 11461 |
| 苏州市      | 10474 |
| 南京市      | 10243 |
| 沈阳市      |  8655 |
| 重庆市      |  8653 |
| 武汉市      |  8352 |
