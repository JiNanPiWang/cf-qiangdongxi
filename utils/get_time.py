from datetime import datetime, timedelta, time


def get_next_minute() -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_minute = current_time + timedelta(minutes=1)
    next_minute_ceiling = next_minute.replace(second=0, microsecond=0)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S:%f')


def get_next_minute_micro_early(microseconds: int = 800000) -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_minute = current_time
    next_minute_ceiling = next_minute.replace(second=59, microsecond=microseconds)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S:%f')


def get_next_2minute() -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_minute = current_time + timedelta(minutes=2)
    next_minute_ceiling = next_minute.replace(second=0, microsecond=0)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S:%f')


def get_next_hour() -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_hour = current_time + timedelta(hours=1)
    next_minute_ceiling = next_hour.replace(minute=0, second=0, microsecond=0)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S:%f')


def get_next_hour_micro_early(microseconds: int = 800000) -> str:
    # 使用函数获取下一分钟的时间
    current_time = datetime.now()
    next_hour = current_time
    next_minute_ceiling = next_hour.replace(minute=59, second=59, microsecond=microseconds)
    return next_minute_ceiling.strftime('%Y-%m-%d %H:%M:%S:%f')


def get_formatted_time(hour: int, minute: int, second: int = 0, microsecond: int = 0) -> str:
    # 得到当天的时分秒
    current_date = datetime.now().date()
    formatted_time = datetime.combine(current_date, time(hour, minute, second, microsecond))
    return formatted_time.strftime('%Y-%m-%d %H:%M:%S:%f')


def is_time_out_of_limit(target_time: str, limit: int) -> bool:
    # 查看当前时间是否超过target_time limit秒
    target_datetime = datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S:%f')
    current_time = datetime.now()
    time_difference = current_time - target_datetime
    return time_difference <= timedelta(seconds=limit)
