### douban_reviews 

douban_reviews is a simple spider to crawl reviews of a movie on douban.com(url=https://movie.douban.com/subject/10831445/reviews) using scrapy

#### review properties
based on api.douban.com/v2:
* reviewer 影评作者
* reviewer_link 影评作者url
* rating_title	评价
* rating	影评评分
* review_link	影评url	
* time	日期	
* review_full	长评
* review_short	短评，200字以内	
* review_useful	有用数
* review_unuserful	无用数

#### start spider
`scrapy crawl douban`

#### results
the results in douban_reviews.json:
![image](https://github.com/hoikin-yiu/douban_reviews/blob/master/img/003.jpg)
![image](https://github.com/hoikin-yiu/douban_reviews/blob/master/img/004.jpg)




