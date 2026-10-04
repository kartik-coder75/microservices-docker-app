import matplotlib.pyplot as plt

# Replace these lists with your actual measured values from load_test.py and docker stats
concurrency = [1, 2, 4, 8, 16]
avg_response_time = [15.2, 18.4, 25.1, 44.8, 82.3]  # in ms
throughput = [58.3, 102.1, 145.6, 168.4, 174.2]     # in req/s
cpu_order_service = [12.5, 24.0, 48.2, 79.5, 96.0]   # in %
mem_order_service = [42.1, 42.8, 43.5, 45.0, 47.2]   # in MB

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Graph 1: Response Time
axs[0, 0].plot(concurrency, avg_response_time, marker='o', color='b')
axs[0, 0].set_title('Concurrent Requests vs Average Response Time')
axs[0, 0].set_xlabel('Concurrency')
axs[0, 0].set_ylabel('Response Time (ms)')
axs[0, 0].grid(True)

# Graph 2: Throughput
axs[0, 1].plot(concurrency, throughput, marker='s', color='g')
axs[0, 1].set_title('Concurrent Requests vs Throughput')
axs[0, 1].set_xlabel('Concurrency')
axs[0, 1].set_ylabel('Throughput (req/s)')
axs[0, 1].grid(True)

# Graph 3: CPU Utilization
axs[1, 0].plot(concurrency, cpu_order_service, marker='^', color='r')
axs[1, 0].set_title('Concurrent Requests vs CPU Utilization (Order Service)')
axs[1, 0].set_xlabel('Concurrency')
axs[1, 0].set_ylabel('CPU (%)')
axs[1, 0].grid(True)

# Graph 4: Memory Utilization
axs[1, 1].plot(concurrency, mem_order_service, marker='d', color='purple')
axs[1, 1].set_title('Concurrent Requests vs Memory Utilization (Order Service)')
axs[1, 1].set_xlabel('Concurrency')
axs[1, 1].set_ylabel('Memory (MB)')
axs[1, 1].grid(True)

plt.tight_layout()
plt.savefig('performance_graphs.png')
print("Graphs saved as performance_graphs.png")
plt.show()