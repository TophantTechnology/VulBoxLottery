# README

本脚本为2022-01-04，漏洞盒子白帽能力觉醒，邀请体验活动奖券码抽奖脚本。  

执行前需修改指定参数：  
``` python
base = 100000 # 本次活动奖券码起始地址
total = 0 # 本次活动总共发放的奖券码数量
hash_seed = "" # 2022-01-17 12:00后，比特币区块链生成的第一个区块HASH值
# hash值列表参考：https://www.blockchain.com/btc/blocks?page=1
```

使用方式：  
``` shell
./InvitationLotto.py
```

最终结果输出为随机列表  
格式为：`奖券码,随机值`  
输出结果会保存到当前目录`Vulbox_lucky.csv` 文件  

中奖列表对应奖项如下：
第1行为一等奖
第2行至第5行为二等奖
第6行至第15行为三等奖
第16行至第35行为四等奖
第36行至第65行为五等奖
所有参与活动者，均可获得内侧限定礼


本活动最终解释权归[斗象科技](https://www.tophant.com/)[漏洞盒子团队](https://www.vulbox.com)所有。  
