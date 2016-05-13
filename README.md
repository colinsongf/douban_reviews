### douban_reviews 

douban_reviews is a simple spider to crawl reviews of a movie on douban.com(url=https://movie.douban.com/subject/10831445/reviews) using scrapy

#### review properties(the results in douban_reviews.json)
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

#### start spider:
`scrapy crawl douban`

#### results：
![image](douban_reviews/img/003.jpg)
![image](douban_reviews/img/004.jpg)




