select remote_addr, count(remote_addr)
from access_grouped_new3 agn
GROUP by remote_addr
order by 2 desc