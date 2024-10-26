# 网络设置

## route 数据通过路径网关等
route中 添加上网目的ip，指定vlan6 接口  
sudo route add -host  上网目的ip  dev vlan6  
这样  （上网目的ip） 数据包是通过 vlan6 转发，源地址就是vlan6 

## arp  设置目的mac找目的物理主机 
arp中 添加 添加上网目的ip MAC地址为B板的网卡MAC地址  
arp -s   上网目的ip   B板的网卡MAC地址  
这样  （上网目的ip数据包） 可以到达B板网卡   
