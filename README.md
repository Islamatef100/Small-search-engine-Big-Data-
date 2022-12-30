# Small-search-engine-Big-Data-
this project to do search engine at 100000 page but you can work at any amount of pages you want and here i will talk about the projct Briefly

1 -> i run code crawling 1 and get content of any amount of pages so now i have some pages content

2 -> use this pages as input to inverted index to get output file which have all word and its pags 
     
     (inverted index)
                   mapper --> take page and give word and the page name and 1
                   combine --> take mapper output and give word and the page name and times it repeats in this page
                   reducer --> take conbine output and give word and all pages this word exist.
         
3 --> now i work at input of page rank so i will run crawling 2 with the same start like and the same amount of pages and get from this code file have links and realtions and in the first line have number of links and realtions

4 --> now run page rank code and get file have all links and its weight and all tartget links
               
                 (page rank)
                    step 1
                          mapper --> take crawling 2 output and  and work at relations and return all soirce and target
                          reducer --> tahe cource and targrt retutn all cource + initial weight and all targets
                    step 2
                           mapper --> take reducer outpyt and return source and ranke for all targer by equation in the code
                           reducer --> take mapper outpute and return source and weight of source by equation in the code and all target
                    
5 --> now take search word from the user and by invertd index output file get number of links and by page rank outpyt file get the weight for each link and sort it and by page rank input fil get the link and print it.
                           
islam atef
software engineer
ia1900@fayoum.edu.eg
