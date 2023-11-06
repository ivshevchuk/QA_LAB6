import subprocess
import json
import sys

def client(server_ip):
    return subprocess.run(["iperf3", "-c", server_ip, "--json"], capture_output=True, text=True)

def parser(iperf_result):
    jsonResult = json.loads(iperf_result.stdout)
    return list(map(lambda interval: parse_interval(interval), jsonResult["intervals"]))

def parse_interval(interval):
    intervalSum = interval["sum"]
    return {
        "Interval": f'{intervalSum["start"]:.1f}-{intervalSum["end"]:.1f}',
        "Transfer": float(f'{intervalSum["bytes"]:.1f}'),
        "Transfer_unit": "Bytes",
        "Bandwidth": float(f'{intervalSum["bits_per_second"]:.1f}'),
        "Bandwidth_unit": "Bits/sec"
    }

if name == "main":
    for value in parser(client("192.168.56.101")):
        print(value)
