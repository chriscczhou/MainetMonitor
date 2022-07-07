# MainetMonitor
The project listens for transactions whose status is pending on the Ethereum mainnet.

# 想要解决什么样的问题？
主要是想解决2个问题：
 - 在冲新土狗时，想要第一时间获取到合约地址：获取主网处于pending状态的交易哈希，获取交易哈希中input字段是否为0xf305d719，即增加流动性。
 - 在冲新土狗时，最大程度保证投资资金的安全：LP锁定+放弃合约所有权是两个重要指标，因此我给脚本也加了0x7d533c1e、0xf305d719。
