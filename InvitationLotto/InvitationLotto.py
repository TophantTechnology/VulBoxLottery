# --** coding="UTF-8" **--
# !/usr/bin/python3
import hashlib
from collections import OrderedDict

# Vulbox 7.0  奖券抽奖公开程序
# 活动结束后修改实际total,hash_seed
# 程序自动对奖券随机排序，奖券排序先后作为抽奖结果
# VULBOX 保留最终解释权

# 总奖券数，修改实际
base = 100000
total = 805
# 随机种子seed，取自活动结束后比特币链上hash
hash_seed = '000000000000000000085caefaa2eb088b184bd48e71948bebffc5e81a53fa39'


def random_rum_for_lottery_id(luckynum, lottery_id):
    h = hashlib.sha512()
    h.update(luckynum)
    h.update(bytes(lottery_id))

    mod = 10 ** 10
    random_rum = int(h.hexdigest(), 16) % mod
    return random_rum


def cal_reward():
    r = {}
    luckynum = luckynum_from_seed(seed)

    for lottery_id in range(base, total + base):
        s = random_rum_for_lottery_id(luckynum, lottery_id)
        r[lottery_id] = s
    return r


def luckynum_from_seed(h):
    hash_names = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

    repeat = 1000000
    r = h
    print('calculating seed...')
    for i in range(repeat):
        if i % 100000 == 0:
            print(str(i) + ' times')
        for n in hash_names:
            h = hashlib.new(n)
            h.update(r)
            r = h.digest()

    return r


def lottery_format(n):
    return prefix + '-' + str(n).zfill(6)


def save_file(rewards):
    print("-----------抽奖结果------------")
    c = 1
    f = open('Vulbox_lucky.csv', 'w')
    for r in rewards:
        f.write(str(r) + ',' + str(rewards[r]) + '\n') # 一行一个号码，按每个奖项数量顺序从前往后取n个
        print('%s,%s' % (str(r), str(rewards[r])))
        c += 1

    f.close()


if __name__ == "__main__":

    prefix = 'VB'
    seed = bytes.fromhex(hash_seed)
    
    reward_map = cal_reward()
    reward_sorted = OrderedDict(sorted(reward_map.items(), key=lambda t: t[1], reverse=True))
    save_file(reward_sorted)
