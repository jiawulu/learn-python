## 模拟实现一个ATM + 购物商城程序

1. 额度 15000或自定义
2. 实现购物商城，买东西加入 购物车，调用信用卡接口结账
3. 可以提现，手续费5%
4. 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
5. 支持多账户登录
6. 支持账户间转账
7. 记录每月日常消费流水
8. 提供还款接口
9. ATM记录操作日志
10. 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
11. 用户认证用装饰器


store_dir

{
    name : [ pwd, amount, [消费记录], cash， type]
}

login

takeoutmoney

transfer

refund

manager

log

checkAccount


creditPay