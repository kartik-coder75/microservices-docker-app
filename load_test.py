import concurrent.futures
import time
import requests

URL = "http://localhost:5001/order"
TOTAL_REQUESTS = 100
WORKLOADS = [1, 2, 4, 8, 16]

def send_request():
    start = time.time()
    try:
        response = requests.get(URL, timeout=10)
        duration = time.time() - start
        return response.status_code == 200, duration
    except Exception:
        return False, time.time() - start

print(f"{'Workload':<10} | {'Concurrency':<12} | {'Avg Latency (ms)':<18} | {'Throughput (req/s)':<20} | {'Failed':<8}")
print("-" * 75)

for idx, concurrency in enumerate(WORKLOADS, start=1):
    start_total = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        results = list(executor.map(lambda _: send_request(), range(TOTAL_REQUESTS)))
    total_time = time.time() - start_total

    successes = sum(1 for ok, _ in results if ok)
    latencies = [lat for _, lat in results]

    avg_latency = (sum(latencies) / len(latencies)) * 1000
    throughput = TOTAL_REQUESTS / total_time
    failed = TOTAL_REQUESTS - successes

    print(f"W{idx:<9} | {concurrency:<12} | {avg_latency:<18.2f} | {throughput:<20.2f} | {failed:<8}")
    
    # Short pause between test runs to view docker stats idle vs load
    time.sleep(2)