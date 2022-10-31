import speedtest
import math


def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"


wifi = speedtest.Speedtest()

print("Loading server list...")
wifi.get_servers()

print("Choosing best server...")
best = wifi.get_best_server()
print(f"Found: {best['name']} located in {best['country']}")

print("Getting download speed...")
download_speed = wifi.download()

print("Getting upload speed...")
upload_speed = wifi.upload()

ping_result = wifi.results.ping

print(f"Download: {int(download_speed / 1024 / 1024)} Mbps")
print(f"Upload: {int(upload_speed / 1024 / 1024)} Mbps")
print(f"Ping: {int(ping_result)} ms")
