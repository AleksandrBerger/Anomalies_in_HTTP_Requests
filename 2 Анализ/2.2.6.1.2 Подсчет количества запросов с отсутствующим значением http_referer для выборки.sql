select count(http_referer)
from access_grouped_new3 agn 
where http_referer = '-'