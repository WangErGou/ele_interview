# -*- coding:utf-8 -*-

from lottery.models import NumberUser, WiningRecord


# ----------------------------------------------------------------------------
#       计算中奖号码
# ----------------------------------------------------------------------------

def calculate_wining_number(stop_datetime, lottery_date):
    '''
    计算指定发放截止日期和指定抽奖日期的中奖号码

    :param stop_datetime: 停止发放抽奖号码的时间
    :type: datetime.datetime

    :param lottery_date: 抽奖的日期
    :type: datetime.date

    :returns: 中奖号码
    :rtype: int
    '''
    number_count = count_numbers(stop_datetime)
    sh_index = get_market_index('shanghai', lottery_date)
    sz_index = get_market_index('shenzheng', lottery_date)

    wining_number = _calculate_wining_number(
        sh_index=sh_index, sz_index=sz_index, number_count=number_count)

    WiningRecord(
        sh_index=sh_index,
        sz_index=sz_index,
        win_number=wining_number).save()


def _calculate_wining_number(sh_index=None,
                             sz_index=None,
                             number_count=None):
    '''
    实际计算中奖号码的部分

    Ps: 采用 postition args 防止传参时弄混
    '''
    # 注意，此处应该使用四舍五入
    nose_number = int(round(sh_index * sz_index * 10000))
    # 确保是12位
    assert 99999999999 < nose_number < 1000000000000
    nose_number = reverse_integer(nose_number)
    wining_number = nose_number % number_count + 1

    return wining_number


def get_market_index(market, date_):
    '''
    从外部接口获取指定股市指定日期的 **收盘** 指数
    '''
    # TODO: date
    if market == 'shanghai':
        return 2894.47
    elif market == 'shenzheng':
        return 9975.42
    else:
        raise TypeError()


def count_numbers(datetime_):
    '''
    统计某个时间点之前发送的抽奖号码数量
    '''
    return NumberUser.objects.filter(create_time__lte=datetime_).count()


def reverse_integer(a):
    '''
    将整数倒序排列，末位为0则抹去

    e.g. input: 123456789010 --> output: 10987654321
    '''
    a_s = str(a).rstrip('0')
    return int(a_s[::-1])


# ----------------------------------------------------------------------------
#       分批放出抽奖号码
# ----------------------------------------------------------------------------
# 既然是抽奖，那么抽奖号码最好不要采用一个一个增加的方法放出，给人的抽奖感觉会
# 很假。
# 可以采取这样一种策略：
# 
#   1. 在开始之前估计一个保守数字，生成对应数量的抽奖号码
#   2. 随后在消耗了 x% 的抽奖号码后，再生成 y% 的抽奖号码
#   3. 为了避免最后未被抽中的抽奖号码尽可能的少，x 渐渐增大，y 渐渐减小
#   4. 具体参数的制定，可以在尝试后变更
def get_random_number():
    '''
    获取一个随机的抽奖号码
    
    注意不要出现重复抽取，我仅仅依靠 MySQL 的事务机制来实现了
    '''
    pass


def need_new_number():
    '''
    是否需要新的抽奖号码
    '''
    pass


def generate_new_number():
    '''
    生成一批抽奖号码
    '''
    pass


def get_random_record():
    pass
