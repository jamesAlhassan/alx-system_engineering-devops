# 0x19. Postmortem
<img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fglobal.discourse-cdn.com%2Fcloudflare%2Foriginal%2F2X%2Fe%2Fe86fee28b56104f676114df33d7b53f82d1831df.jpeg&tbnid=RW28aBE3spRbpM&vet=12ahUKEwjz19-SsPX-AhWBpicCHbD1AyYQMyhFegUIARCPAQ..i&imgrefurl=https%3A%2F%2Fcommunity.cloudflare.com%2Ft%2Fviewen-server-521-web-server-down%2F38109&docid=dAh31wXdu9u82M&w=480&h=360&q=server%20down%20image&ved=2ahUKEwjz19-SsPX-AhWBpicCHbD1AyYQMyhFegUIARCPAQ" alt="error 500" width="1000" height="400">

## Issue Summary:
On the 1st May, 2023 from 8:03 AM to 8:25 AM GMT, requests to webservers for content resulted in HTTP Status Code 503 - Service Unavailable. As a result, users were not able to access web services provided by those servers successfully.

## Timeline (all times GMT)
* 08:03 AM: An alert e-mail and text message was sent to e-mail address and personal phone of the engineer on duty respectively when our monitoring tool(datadog) detected that the serveers were down
* 08:05 AM: the engineer responded and start his diagnostics
* 08:10 AM: engineer begun reading through Apache configuration and log files
* 08:15 AM: It was found out that the issue was caused by over a million concurrent requests to the Apache server. Apache's inability to handle the huge concurrent requests led to the servers breakdown.
* 8:22 AM: Apacher webserver was replaced with Nginx
* 08:25 AM: Nginx was configured and the website was back online

## Root Cause
The root cause was the c10k problem. The C10k problem is the problem of optimizing network sockets to handle a large number of clients at the same time.The name C10k is a numeronym for concurrently handling ten thousand connections. Handling many concurrent connections is a different problem to handling many requests per second: the latter requires high throughput (processing them quickly), while the former does not have to be fast, but requires efficient scheduling of connections.

## Resolution and Recovery
Apache webserver was replaced with Nginx

## Corrective and Prevantative Measures
It was decided that Nginx with be the web server going forward with Ha Proxy as a load balancer
