from datetime import datetime, timedelta, time


def get_next_minute() -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_minute = current_time + timedelta(minutes=1)
    next_minute_ceiling = next_minute.replace(second=0, microsecond=0)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S')

def get_formatted_time(hour: int, minute: int, second: int) -> str:
    # 得到当天的时分秒
    current_date = datetime.now().date()
    formatted_time = datetime.combine(current_date, time(hour, minute, second))
    return formatted_time.strftime('%Y-%m-%d %H:%M:%S')

def is_time_out_of_limit(target_time: str, limit: int) -> bool:
    # 查看当前时间是否超过target_time limit秒
    target_datetime = datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.now()
    time_difference = current_time - target_datetime
    return time_difference <= timedelta(seconds=limit)
