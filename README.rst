============
饿了吗面试题
============

题目
====

饿了么用户在下单完成点评会拿到积分, 积分可以在积分商城消费掉.
目前商城推出了新的抽奖玩法.
用户点击「立即抽奖」换取抽奖号，如抽奖号与开奖后的中奖号码一致即为中奖
以下为某一抽奖的示例:

| **活动奖品：** Apple MacBook Air 13.3英寸笔记本电脑 1台
| **活动时间：** 2016年1月18日至2016年1月31日
| **开奖及公布时间：** 2016年2月2日
| **活动参与：** 用户点击「立即抽奖」换取抽奖号，如抽奖号与开奖后的中奖号码一致即为中奖

抽奖规则:
为了保证抽奖过程公正透明，中奖号码计算规则如下

1. 开奖日收盘时的上证指数 x 收盘时的深证指数 x 10000 =12位数。（指数以证交所公布数字为准）
2. 将此12位数的数字倒序排列后（如首位是0，则直接抹去），再除以开奖截止时间发放的抽奖号总数，得到的余数加1即为本次活动的最终中奖号码。
3. 若您的抽奖号与最终中奖号码完全一致，就可以获得本次活动的大奖！
4. 饿了么工作人员及家属不得参加抽奖！

中奖号码计算示例

* 假设截止到1月31日，总共发放了150000个抽奖号
* 2月2日收盘的上证指数为2894.47，深证指数为9975.42
* 2894.47 x 9975.42 x 10000=288735539274
* 倒序得到数字472935537882
* 除以150000，余数87882，87882＋1＝87883
* 所以本次活动中奖号码为87883

简单来说！获得抽奖码越多中奖概率越大哦，快去获取抽奖号吧！

数据库设计
==========

.. code-block:: sql

    BEGIN;
    CREATE TABLE `number_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `number` integer NOT NULL UNIQUE, `create_time` datetime NOT NULL);
    CREATE TABLE `ele_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(64) NOT NULL);
    CREATE TABLE `wining_record` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `sh_index` integer NOT NULL, `sz_index` integer NOT NULL, `wining_number` integer NOT NULL, `create_time` datetime NOT NULL);
    ALTER TABLE `number_user` ADD COLUMN `user_id` integer NOT NULL;
    ALTER TABLE `number_user` ALTER COLUMN `user_id` DROP DEFAULT;
    CREATE INDEX `number_user_e8701ad4` ON `number_user` (`user_id`);
    ALTER TABLE `number_user` ADD CONSTRAINT `number_user_user_id_53d4bb1edf121ccb_fk_ele_user_id` FOREIGN KEY (`user_id`) REFERENCES `ele_user` (`id`);

    COMMIT;
