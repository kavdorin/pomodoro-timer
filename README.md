# 番茄钟计时器（pomodoro-timer）

一个简单的命令行番茄钟计时器，使用 Python 标准库实现，无需安装任何第三方依赖。

## 功能

- 专注 25 分钟，短休息 5 分钟；每完成 4 轮专注后长休息 15 分钟
- 倒计时实时显示剩余时间（MM:SS），结束时响铃提示
- 可自定义专注时长、短休息、长休息和轮数
- 按 Ctrl+C 可随时退出

## 环境要求

- Python 3.8 及以上版本

## 使用方法

使用默认设置运行（25 分钟专注、5 分钟短休息、15 分钟长休息、4 轮）：

```bash
python pomodoro.py
```

自定义时长和轮数：

```bash
python pomodoro.py --work 25 --short-break 5 --long-break 15 --cycles 4
```

快速演示（每段 1 分钟、只跑 1 轮）：

```bash
python pomodoro.py --work 1 --short-break 1 --cycles 1
```

## 参数说明

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `--work` | 专注时长（分钟） | 25 |
| `--short-break` | 短休息时长（分钟） | 5 |
| `--long-break` | 长休息时长（分钟） | 15 |
| `--cycles` | 专注轮数 | 4 |

## 许可证

MIT 许可证。
