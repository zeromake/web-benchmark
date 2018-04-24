#!/bin/env python3
import subprocess
import json
import os
import time

BenchmarkArray = ("flask", "go", "fibjs", "sanic", "tornado", "asyncio")

def exec_shell(*args: str) -> int:
    popen_obj = subprocess.Popen(
        " ".join(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True
    )
    status = popen_obj.wait()
    return status

def split_ab(line: str):
    return line.split(":")[1].strip().split(" ")[0]

def benchmark_ab():
    data = {}
    exec_shell("ab -n 20000 -c 200 http://127.0.0.1:5000/echo > benchmark.log")
    try:
        with open("benchmark.log", 'r', encoding='utf8') as benchmark:
            for line in benchmark:
                if line.startswith("Concurrency Level"):
                    data['level'] = int(split_ab(line))
                elif line.startswith("Time taken for tests"):
                    data['time'] = float(split_ab(line)) * 1000
                elif line.startswith("Complete requests"):
                    data['request_count'] = int(split_ab(line))
                elif line.startswith("Requests per second"):
                    data['rps'] = float(split_ab(line))
                    break
    except Exception:
        return None
    return data

def benchmark_siege():
    data = {}
    exec_shell("siege -q -lbenchmark.log -c 200 -r 100 -b http://127.0.0.1:5000/echo")
    try:
        with open("benchmark.log", 'r', encoding='utf8') as benchmark:
            line = benchmark.readlines()[-1]
            temp = [x.strip() for x in line.split(",")]
            data['level'] = 200
            data['time'] = float(temp[2]) * 1000
            data['request_count'] = int(temp[1])
            data['rps'] = float(temp[5])
    except Exception:
        return None
    return data

def start_benchmark(name: str):
    ab = []
    siege = []
    if exec_shell("docker-compose", "up", "-d", name) == 0:
        time.sleep(1)
        print("start %s" % name)
        try:
            for _ in range(3):
                temp = benchmark_ab()
                if temp:
                    print("%s ab rps: %f" % (name, temp.get('rps', 0)))
                    ab.append(temp)
            for _ in range(3):
                temp = benchmark_siege()
                if temp:
                    print("%s siege rps: %f" % (name, temp.get('rps', 0)))
                    siege.append(temp)
        finally:
            print("stop %s" % name)
            exec_shell("docker-compose", "stop", name)
            return { "ab": ab, "siege": siege }

def main():
    BenchmarkData = {}
    for name in BenchmarkArray:
        BenchmarkData[name] = start_benchmark(name)
    with open("benchmark.json", 'w', encoding='utf8') as data:
        json.dump(BenchmarkData, data, ensure_ascii=False, indent='  ')
    os.remove("benchmark.log")

if __name__ == "__main__":
    main()
