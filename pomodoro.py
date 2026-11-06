#!/usr/bin/env python3
"""命令行番茄钟计时器（仅使用 Python 标准库）。

默认一轮：专注 25 分钟，短休息 5 分钟；每完成 4 轮专注后长休息 15 分钟。
使用示例：
    python pomodoro.py
    python pomodoro.py --work 25 --short-break 5 --long-break 15 --cycles 4
    python pomodoro.py --work 1 --short-break 1 --cycles 1  # 快速演示
按 Ctrl+C 可随时退出。
"""

import argparse
import sys
import time


def format_time(seconds: int) -> str:
    """把秒数格式化为 MM:SS。"""
    minutes, secs = divmod(max(0, seconds), 60)
    return f"{minutes:02d}:{secs:02d}"


def countdown(label: str, minutes: float) -> None:
    """倒计时并在同一行刷新剩余时间。"""
    total = int(round(minutes * 60))
    print(f"\n{label}：{minutes:g} 分钟，开始！", flush=True)
    for remaining in range(total, -1, -1):
        print(f"\r{label} 剩余 {format_time(remaining)} ", end="", flush=True)
        if remaining:
            time.sleep(1)
    print(f"\n{label}结束！", flush=True)
    print("\a", end="", flush=True)  # 响铃提示（终端支持时）


def run(work: float, short_break: float, long_break: float, cycles: int) -> int:
    """按番茄工作法运行指定轮数，返回 0。"""
    if work <= 0 or short_break <= 0 or long_break <= 0 or cycles <= 0:
        print("错误：所有时长和轮数都必须大于 0。", file=sys.stderr)
        return 2
    try:
        for cycle in range(1, cycles + 1):
            countdown(f"第 {cycle}/{cycles} 轮专注", work)
            if cycle == cycles:
                break
            if cycle % 4 == 0:
                countdown("长休息", long_break)
            else:
                countdown("短休息", short_break)
    except KeyboardInterrupt:
        print("\n已退出番茄钟，下次继续加油！")
        return 130
    print(f"\n完成 {cycles} 轮番茄钟，辛苦了！")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="命令行番茄钟计时器")
    parser.add_argument("--work", type=float, default=25, help="专注时长（分钟），默认 25")
    parser.add_argument("--short-break", type=float, default=5, help="短休息时长（分钟），默认 5")
    parser.add_argument("--long-break", type=float, default=15, help="长休息时长（分钟），默认 15")
    parser.add_argument("--cycles", type=int, default=4, help="专注轮数，默认 4")
    args = parser.parse_args(argv)
    return run(args.work, args.short_break, args.long_break, args.cycles)


if __name__ == "__main__":
    raise SystemExit(main())
