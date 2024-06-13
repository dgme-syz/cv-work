@echo off
REM 等待 30 分钟（1800 秒）
timeout /t 1800 /nobreak

REM 切换到指定目录
cd D:\projects\cv\cv-work\task3\SinSR

REM 激活 Conda 环境
call conda activate webui

REM 运行 Python 脚本
python inference.py -i .\testdata\RealSet65_sharp\ -o .\results\realset64_sharp --ckpt weights/SinSR_v1.pth --scale 4 --one_step --chop_size 256
