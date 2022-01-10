# README

本脚本为2022-01-04，漏洞盒子白帽能力觉醒，邀请体验活动乐透码抽奖脚本。  

执行前需修改指定参数：  
``` python
base = 100000 # 本次活动乐透码起始地址
total = 0 # 本次活动总共发放的乐透码数量
hash_seed = "" # 2022-01-17 12:00后，比特币区块链生成的第一个区块HASH值
# hash值列表参考：https://www.blockchain.com/btc/blocks?page=1
```

使用方式：  
``` shell
./InvitationLotto.py
```

最终结果输出为随机列表，一行一个码，输出结果会保存到当前目录`Vulbox_lucky.csv` 文件。  

中奖列表为按奖项数量，从上往下读取对应的行数，即：  
第一行为一等奖  
第二行为二等奖，第一个码  
第三行为二等奖，第二个码  
以此类推。

本活动最终解释权归[斗象科技](https://www.tophant.com/)[漏洞盒子团队](https://www.vulbox.com)所有。  
