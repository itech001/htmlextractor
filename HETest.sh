#!/bin/bash

#python HEDownloadCli.py -u http://blog.sina.com.cn/s/articlelist_1353758960_7_1.html -t articles -c 力哥说理财 -r http://blog.sina.com.cn/s/blog_.*
#python HEDownloadCli.py -u http://blog.sina.com.cn/s/articlelist_1353758960_7_2.html -t articles -c 力哥说理财 -r http://blog.sina.com.cn/s/blog_.*


for (( i=1; i <= 23; i++ ))
do
 url=http://blog.sina.com.cn/s/articlelist_1215172700_0_$i.html
 echo $url
 #python HEDownloadCli.py -u  $url -t articles -c 缠中说禅 -r http://blog.sina.com.cn/s/blog_.* -i 教你炒股票
done
