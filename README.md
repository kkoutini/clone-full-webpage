#Requirments
-using Python Micro Interceptor Proxy https://github.com/allfro/pymiproxy

-chrome browser (or any)

-bash

-curl

#How
1-first start chrome use our proxy and no sec
    open /Applications/Google\ Chrome.app --args --disable-web-security --proxy-server="127.0.0.1:8080"



2-start proxy server 
    python proxy.py 

3-Now all requests stored in urlss file, grep all Get remove some extras
     cat urlss | grep GET | sed 's/GET //g' | sed 's/ HTTP\/1.1//g'   > urlfinal

4-Now we get in the file all requests which were sent (you may still need to fix / to /index.html etc...)

5- you can convert them into curl commands

    cat urlfinal | while read ln; do echo  " curl  \"http://www.yourhost.com${ln:0:${#ln}-1}\" --create-dirs -o \".${ln:0:${#ln}-1}\""; done > ko
6-or just excute curls
        
    cat urlfinal | while read ln; do curl  "http://www.yourhost.com${ln:0:${#ln}-1}" --create-dirs -o ".${ln:0:${#ln}-1}"; done 

7-your website will be downloaded
