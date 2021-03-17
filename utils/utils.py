import platform
import signal

import os


def valid_port(port):
    while True:
        if get_platform() == "Windows":
            port_list = os.popen('NETSTAT -ano | findstr "' + str(port) + '"')
        else:  # sys == "Linux"
            # port_list = os.popen('netstat -ano | grep "%s" ' % port)
            port_list = os.popen('netstat -an | grep "%s" ' % port)
        port_used = port_list.read()
        if str(port) in port_used:
            port = port + 1
        else:
            break
    return port


def get_platform():
    return platform.system()


# 根据规则、匹配并杀死进程
def kill_process(pattern):
    sys = get_platform()
    if sys == "Windows":
        processes = os.popen('tasklist | findstr "' + pattern + '"')
    else:  # sys == "Linux"
        processes = os.popen('ps aux | grep ' + pattern)

    for process in processes.readlines():
        try:
            spilt = process.split()
            pid = spilt[1]
            os.kill(int(pid), signal.SIGKILL)
        except Exception as e:
            continue


# 获取 进程号 -> 进程命令 的字典
def get_process(pattern):
    processes = os.popen('ps aux | grep ' + pattern)
    result = {}
    for process in processes.readlines():
        try:
            spilt = process.split()
            result[str(spilt[1])] = " ".join(spilt[10:])
        except Exception as e:
            continue
    return result


def adb_devices():
    device_out = os.popen('adb devices')
    devices = []
    for device in device_out.readlines():
        if 'List of devices' in device or 'adb' in device or 'daemon' in device or 'offline' in device or 'unauthorized' in device or len(
                device) < 5:
            pass
        else:
            udid = device.split()
            devices.append(udid[0])
    device_out.close()
    return devices


def adb_reset():
    os.system("adb kill-server")
    os.system("adb server && adb devices")
