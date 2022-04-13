import argparse
import inotify.adapters
import os
import sys
import signal
import shlex
import subprocess as sp
import time

args = None
podlist = {}

def launch_scheduler():
    # cfg_h, cfg_t = os.path.split(args.pod_list)
    # if cfg_h == '':
    #     cfg_h = os.getcwd()

    cmd = "{} -p {} -f {} -q {} -m {} -w {}".format(
        args.schd, args.ipc_dir, args.pod_list, args.base_quota, args.min_quota, args.window
    )
      
    proc = sp.Popen(shlex.split(cmd), universal_newlines=True, bufsize=1)
    return proc

def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('schd', help='path to scheduler executable')
    parser.add_argument('gpu_uuid', help='scheduling system GPU UUID')
    parser.add_argument('pod_list', help='path to pod list file')
    parser.add_argument('ipc_dir', help='path to pod ipc dir')
    parser.add_argument('--base_quota', type=float, default=300, help='base quota (ms)')
    parser.add_argument('--min_quota', type=float, default=20, help='minimum quota (ms)')
    parser.add_argument('--window', type=float, default=10000, help='time window (ms)')
    args = parser.parse_args()

    launch_scheduler()
    sys.stderr.write(f"[launcher] scheduler started on 0.0.0.0:\n")
    sys.stderr.flush()


if __name__ == '__main__':
    os.setpgrp()
    try:
        main()
    except:
        sys.stderr.write("Catch exception: {}\n".format(sys.exc_info()))
        sys.stderr.flush()
    finally:
        for _, val in podlist.items():
            os.killpg(os.getpgid(val[1].pid), signal.SIGKILL)
        os.killpg(0, signal.SIGKILL)
