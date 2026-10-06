# Build, Deploy and Analyze a Containerized Microservice Application Under Varying Workloads

> **Lab Evaluation Experiment** — Microservices, Docker, Docker Compose and Performance Analysis

---

## Table of Contents

1. [Aim](#aim)
2. [Project Overview](#project-overview)
3. [General Instructions Followed](#general-instructions-followed)
4. [Architecture](#architecture)
5. [Repository Structure](#repository-structure)
6. [Technology Stack](#technology-stack)
7. [Checkpoint 1 — Design and Develop the Microservices](#checkpoint-1--design-and-develop-the-microservices)
8. [Checkpoint 2 — Containerize and Deploy the Application](#checkpoint-2--containerize-and-deploy-the-application)
9. [Checkpoint 3 — Establish and Demonstrate Microservice Communication](#checkpoint-3--establish-and-demonstrate-microservice-communication)
10. [Checkpoint 4 — Generate Varying Workloads and Monitor Performance](#checkpoint-4--generate-varying-workloads-and-monitor-performance)
11. [Checkpoint 5 — Analyze and Present the Results](#checkpoint-5--analyze-and-present-the-results)
12. [How to Run the Project](#how-to-run-the-project)
13. [Final Deliverables Checklist](#final-deliverables-checklist)
14. [Conclusion](#conclusion)


---

## Aim

To develop a microservice-based application containing three independent services, containerize and deploy the services using Docker, establish inter-service communication, generate varying workloads, monitor resource utilization, and analyze application performance.

---

## Project Overview

| Item | Details |
|------|---------|
| **Application Domain** | Order Management |
| **Number of Microservices** | 3 |
| **Programming Language / Framework** | Python Flask |
| **Containerization** | Docker |
| **Orchestration / Deployment** | Docker Compose |
| **Load Testing Tool** | Custom Python script |
| **Monitoring Tool** | docker stats |

**Short description of the application:**

A 3-tier microservice application simulating an e-commerce order workflow. The order-service acts as an entry API gateway that orchestrates end-to-end order processing by synchronously querying user-service for customer profile verification and triggering notification-service to deliver status alerts over an isolated Docker bridge network.

---

## General Instructions Followed

- The application contains **exactly three independent microservices**.
- Each microservice has a **clear responsibility** and **at least one working REST API endpoint**.
- **Docker** is used to containerize every service, and **Docker Compose** is used for deployment.
- Workload testing was performed and **actual measured values** were used for the analysis.
- Each checkpoint was demonstrated to the evaluator before proceeding to the next one.

---

## Architecture

### Minimum Required Architecture

```
Client → Service 1 → Service 2 / Service 3
```

### Architecture of This Project

```
                      ┌──────────────────────────┐
                      │          Client          │
                      │          (curl)          │
                      └────────────┬─────────────┘
                                   │  HTTP
                                   ▼
                      ┌──────────────────────────┐
                      │ Service 1: order-service │
                      │ Port: 5001               │
                      └─────┬──────────────┬─────┘
                            │              │
              (user-service)│              │(notification-service)
                            ▼              ▼
          ┌────────────────────────┐   ┌─────────────────────────────────┐
          │ Service 2: user-service│   │ Service 3: notification-service │
          │ Port: 5002             │   │ Port: 5003                      │
          └────────────────────────┘   └─────────────────────────────────┘

            All services run on the same Docker Compose network
```


### Communication Flow

Client calls order-service at http://localhost:5001/order → order-service calls user-service (http://user-service:5000/user) for user profile details → order-service calls notification-service (http://notification-service:5000/notify) to trigger order notifications → combined aggregated response is returned to the client.

---

## Repository Structure

```
.
├── notification-service/
│   ├── app.py 
│   ├── requirements.txt 
│   └── Dockerfile
├── order-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── load_test.py
|── performance_graphs.png
|── plot_graphs.py
├── .gitignore
└── README.md
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language / Framework | Python 3.12.8 / Flask |
| Containerization | Docker 29.8.0 |
| Deployment | Docker Compose v5.5.1 |
| Load Testing | Custom Python Script |
| Monitoring | docker stats |
| Graph Plotting | Matplotlib |

---

## Checkpoint 1 — Design and Develop the Microservices

### Tasks

1. Select an application domain.
2. Identify three independent microservices.
3. Define the responsibility of each service.
4. Implement the three services using a suitable programming language/framework.
5. Create REST API endpoints for each service.
6. Run and test each service independently.
7. Verify that the APIs return the expected responses.

> **Completion condition:** All three microservices are independently working and their APIs can be demonstrated.

### Selected Domain

##### Order Management: 
Justification: E-commerce applications require decoupled components where ordering, user authentication/profile management, and asynchronous customer notifications operate independently to ensure fault isolation and scalable workload handling.

### Microservices and Their Responsibilities

| Service | Name | Responsibility | Port |
|---------|------|----------------|------|
| Service 1 | order-service | Acts as the primary API gateway; aggregates customer data and triggers notifications upon order processing. | 5001 (Host) / 5000 (Container) |
| Service 2 | user-service | Manages user accounts, retrieves active profile data, and validates user status. | 5002 (Host) / 5000 (Container) |
| Service 3 | notification-service | Handles dispatching email/SMS notifications and confirmation alerts. | 5003 (Host) / 5000 (Container) |

### REST API Endpoints

**Service 1 — order-service**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| GET | /order | Orchestrates the order flow by querying User and Notification services and returning the consolidated result. | {"status": "Order Processed", "user_info": {"user_id": 101, "name": "Student", "status": "Active"}, "notification": {"status": "Notification sent successfully via Email"}} |

**Service 2 — user-service**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| GET | /user | `Fetches details and active status for a given user profile. | {"user_id": 101, "name": "Student", "status": "Active"} |

**Service 3 — notification-service**

| Method | Endpoint | Description | Sample Response |
|--------|----------|-------------|-----------------|
| GET |/notify | Simulates sending an order confirmation notification. | {"status": "Notification sent successfully via Email"} |

### Independent Testing of Each Service

```bash
curl http://localhost:5001/
curl http://localhost:5002/user
curl http://localhost:5003/notify
```

---
## Checkpoint 2 — Containerize and Deploy the Application

### Tasks

1. Create a separate Dockerfile for each microservice.
2. Create the required dependency/configuration files.
3. Build a Docker image for each microservice.
4. Verify that all three images are available using Docker commands.
5. Create a `docker-compose.yml` file.
6. Configure all three services in Docker Compose.
7. Deploy the complete application using Docker Compose.
8. Verify that all three containers are running.

> **Completion condition:** Three Docker images are built successfully and all three microservices are running as containers.

### Dockerfiles

A separate Dockerfile is provided for each service:

- [`order-service/Dockerfile`](order-service/Dockerfile)
- [`user-service/Dockerfile`](user-service/Dockerfile)
- [`notification-service/Dockerfile`](notification-service/Dockerfile)

### Dependency / Configuration Files

order-service/requirements.txt: flask, requests

user-service/requirements.txt: flask

notification-service/requirements.txt: flask

### Build Docker Images

```bash
docker build -t order-service ./order-service
docker build -t user-service ./user-service
docker build -t notification-service ./notification-service
```

### Verify Images

```bash
docker images
```

### docker-compose.yml

See [`docker-compose.yml`](docker-compose.yml).

```yaml
services:
  order-service:
    build: ./order-service
    ports:
      - "5001:5000"
    environment:
      - USER_SERVICE_URL=http://user-service:5000
      - NOTIFICATION_SERVICE_URL=http://notification-service:5000
    depends_on:
      - user-service
      - notification-service
    networks:
      - lab-network

  user-service:
    build: ./user-service
    ports:
      - "5002:5000"
    networks:
      - lab-network

  notification-service:
    build: ./notification-service
    ports:
      - "5003:5000"
    networks:
      - lab-network

networks:
  lab-network:
    driver: bridge
```

### Deploy Using Docker Compose

```bash
docker compose up --build -d
```

### Verify Running Containers

```bash
docker ps
docker compose ps
```

---

## Checkpoint 3 — Establish and Demonstrate Microservice Communication

### Tasks

1. Create/configure the Docker network through Docker Compose.
2. Connect all three services to the same application network.
3. Configure service-to-service communication using Docker service names.
4. Test communication between the microservices.
5. Perform an end-to-end request involving multiple services.
6. Verify that the final response is successfully returned to the client.

> **Completion condition:** Students demonstrate successful communication between the three microservices and an end-to-end request.

### Docker Network Configuration

- **Network name:** microservice-lab_lab-network
- **Network driver:**  bridge
- All three services are attached to the same network through `docker-compose.yml`.

```bash
docker network ls
docker network inspect microservice-lab_lab-network
```


### Service-to-Service Communication (Using Docker Service Names)

| Caller | Callee | URL Used (Docker Service Name) | Purpose |
|--------|--------|--------------------------------|---------|
| order-service | user-service | http://user-service:5000/user | Retrieve customer account and active status details |
| order-service | notification-service | http://notification-service:5000/notify | Trigger dispatch of order confirmation alerts |

### End-to-End Request

```bash
curl http://localhost:5001/order
```

**Sample Response:**

```json
{
  "notification": {
    "status": "Notification sent successfully via Email"
  },
  "status": "Order Processed",
  "user_info": {
    "name": "Student",
    "status": "Active",
    "user_id": 101
  }
}
```

---

## Checkpoint 4 — Generate Varying Workloads and Monitor Performance

### Tasks

1. Select an API suitable for workload testing.
2. Use a load-testing tool or create a suitable workload generator.
3. Test the application using at least five workload levels.
4. A suggested workload is 1, 2, 4, 8, and 16 concurrent requests.
5. Record response time and throughput for every workload.
6. Monitor all three containers using `docker stats` or another suitable monitoring method.
7. Record CPU and memory utilization.
8. Record successful and failed requests, if applicable.

> **Completion condition:** Performance measurements are collected for all workload levels.

### API Selected for Workload Testing

- **Endpoint:** GET http://localhost:5001/order
- **Reason for selection:** It acts as the primary end-to-end composite endpoint that triggers synchronous inter-service communication across all three microservices (order-service calling both user-service and notification-service), ensuring the measured resource metrics reflect full system load.

### Load-Testing Tool / Workload Generator

- **Tool:** Custom Python script using concurrent futures.ThreadPoolExecutor and requests
- **Total requests per workload:** 100
- **Test duration (if applicable):** Variable / Request-bounded (runs until all 100 requests complete per concurrency level)

### Suggested Workload Levels

| Test | Concurrent Requests |
|------|---------------------|
| W1 | 1 |
| W2 | 2 |
| W3 | 4 |
| W4 | 8 |
| W5 | 16 |

### Commands Used

```bash
# Load test
python load_test.py

# Container monitoring
docker stats
```

### Monitoring Method

All three containers were monitored using `docker stats` CLI live stream while each workload was running. The peak/average CPU and memory utilization of each container was recorded. 


### Raw Measurements — Per-Container Resource Utilization

**Service 1 — order-service**

| Workload | Concurrency | CPU (%) | Memory (MiB) |
|----------|-------------|---------|------------------|
| W1 | 1 | 29.14 | 29.39 |
| W2 | 2 | 55.09 | 28.07 |
| W3 | 4 | 50.1 | 30.87 |
| W4 | 8 | 81.77 | 30.17 |
| W5 | 16 | 90.49 | 29.37 |

**Service 2 — user-service**

| Workload | Concurrency | CPU (%) | Memory (MiB / %) |
|----------|-------------|---------|------------------|
| W1 | 1 | 9.18 | 22.19 |
| W2 | 2 | 17.99 | 22.28 |
| W3 | 4 | 14.06 | 22.14 |
| W4 | 8 | 16.66 | 22.31 |
| W5 | 16 | 15.73 | 21.91 |

**Service 3 — notification-service**

| Workload | Concurrency | CPU (%) | Memory (MiB / %) |
|----------|-------------|---------|------------------|
| W1 | 1 | 8.71 | 22.73 |
| W2 | 2 | 16.80 | 23.31 |
| W3 | 4 | 20.02 | 23.5 |
| W4 | 8 | 11.85 | 22.98 |
| W5 | 16 | 19.88 | 23.86 |

---

## Checkpoint 5 — Analyze and Present the Results

### Tasks

1. Prepare an observation table containing workload, concurrency, response time, throughput, failed requests, CPU utilization, and memory utilization.
2. Create suitable graphs from the measured results.
3. Compare application performance at different workload levels.
4. Identify how increasing workload affects the application.
5. Identify which microservice consumes more resources.
6. Explain any performance degradation or failures observed.
7. Demonstrate the complete application to the evaluator.
8. Explain the architecture, containerization, communication, workload testing, and performance results.

> **Completion condition:** Students demonstrate the complete experiment and explain their measured results.

### Performance Observation Table

| Workload | Concurrency | Avg. Response Time (ms) | Throughput (req/s) | Failed Requests |
|----------|-------------|-------------------------|--------------------|-----------------|
| W1 | 1 | 30.90 | 32.14 | 0 |
| W2 | 2 | 32.07 | 61.91 | 0 | 
| W3 | 4 | 34.63 | 114.05 | 0 |
| W4 | 8 | 62.27 | 124.44 | 0 |
| W5 | 16 | 122.70 | 120.19 | 0 |


### Performance Graphs

**1. Concurrent Requests vs Average Response Time**

**2. Concurrent Requests vs Throughput**

**3. Concurrent Requests vs CPU Utilization**

**4. Concurrent Requests vs Memory Utilization**

<img width="1919" height="954" alt="Screenshot 2026-10-04 121638" src="https://github.com/user-attachments/assets/cdbeeaba-3924-47be-8da7-d57be4668fd1" />


### Analysis

**Comparison of performance at different workload levels:**

From Concurrency 1 (W1) to Concurrency 4 (W3), throughput scaled almost linearly from 32.14 req/s to 114.05 req/s while average response time remained stable (increasing marginally from 30.90 ms to 34.63 ms). As workload increased to Concurrency 8 (W4) and Concurrency 16 (W5), throughput saturated near ~120–124 req/s, and average response time escalated sharply to 62.27 ms and 122.70 ms. Zero request failures occurred across all tested workloads.

**Effect of increasing workload on the application:**

- Response time: Increased moderately from 30.90 ms (W1) to 34.63 ms (W3), then spiked sharply to 62.27 ms (W4) and 122.70 ms (W5) due to queueing delays under higher concurrency.
- Throughput: Increased significantly from 32.14 req/s to a peak of 124.44 req/s at Concurrency 8, then plateaued/slightly dropped to 120.19 req/s at Concurrency 16 as CPU capacity saturated.
- CPU utilization: Scaled dramatically on order-service from 29.14% (W1) up to 90.49% (W5), whereas user-service and notification-service remained comparatively low (peaking around 17.99% and 20.02%).
- Memory utilization: Remained nearly constant across all workloads for all services (order-service ~28–30 MiB, user-service ~22 MiB, notification-service ~22–23 MiB), indicating stateless request handling with no memory leaks.
- Failed requests: 0 failed requests across all workload tiers (100% success rate up to Concurrency 16).

**Microservice consuming the most resources:**

order-service consumed the most resources by a significant margin. While user-service and notification-service peaked at only 17.99% and 20.02% CPU respectively, order-service reached a peak CPU utilization of 90.49% at W5 and maintained higher memory usage (~29.39–30.87 MiB vs. ~22–23 MiB). This occurs because order-service serves as the primary ingress gateway, managing incoming client network connections, issuing separate outgoing HTTP calls to both backend microservices, and aggregating their JSON payloads.

**Performance degradation / failures observed and their explanation:**

Performance degradation began at Concurrency 8 (W4) and was prominently evident at Concurrency 16 (W5), where response times doubled from 62.27 ms to 122.70 ms while throughput plateaued around ~120 req/s. This saturation occurred because order-service reached 90.49% CPU utilization, creating a processing bottleneck. Because order-service makes synchronous sequential requests over HTTP to user-service and notification-service, the single-threaded/blocking nature of default Flask development server workers caused worker starvation and request queuing under 16 concurrent clients. No HTTP error failures or timeouts occurred, confirming stability under load.
### Architecture, Containerization, Communication and Workload Testing — Summary

| Area | Summary |
|------|---------|
| Architecture | 3-tier decoupled microservice application composed of order-service (acting as the entry API Gateway on port 5001), user-service (port 5002), and notification-service (port 5003) built with Python Flask. |
| Containerization | Each microservice is packaged using standalone Dockerfile builds based on Python images, managing service-specific dependencies via isolated requirements.txt files. |
| Communication | Microservices run inside a dedicated user-defined Docker bridge network (microservice-lab_lab-network), communicating synchronously via HTTP REST using internal Docker DNS service names (http://user-service:5000 and http://notification-service:5000). |
| Workload Testing | Automated benchmarking executed against the end-to-end composite /order endpoint using a custom Python multi-threaded script across 5 concurrency tiers ($1, 2, 4, 8, 16$) with 100 requests each, monitored live using docker stats. |
| Performance Results | Peak throughput reached $124.44\text{ req/s}$ at concurrency 8 before plateauing. Average response time escalated from $30.90\text{ ms}$ to $122.70\text{ ms}$ at concurrency 16 as gateway CPU peaked at $90.49\%$, with zero failed requests across all workloads. |

---

## How to Run the Project

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed
- Python 3.x installed with requests library (for running load_test.py)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/kartik-coder75/microservices-docker-app
cd C:\Users\karti\OneDrive\Documents\KLETech\FifthSem\CloudComputing\Lab\LabExperiments\microservice-lab

# 2. Build and start all three services
docker compose up --build -d

# 3. Verify that all three containers are running
docker compose ps

# 4. Test the end-to-end API
curl http://localhost:5001/order

# 5. Run the load test
python load_test.py

# 6. Monitor resource usage in another terminal
docker stats

# 7. Stop and remove the containers
docker compose down
```


---

## Workflow

```
DEVELOP → CONTAINERIZE → DEPLOY → CONNECT → LOAD TEST → MONITOR → ANALYZE → DEMONSTRATE
```

---

## Conclusion

A 3-tier Flask microservice application was containerized and deployed using Docker Compose over an isolated bridge network. As concurrency increased from 1 to 16, throughput peaked at 124.44 req/s while response time increased to 122.70 ms without any failed requests. The order-service acted as the primary bottleneck reaching 90.49% CPU utilization, demonstrating container resource isolation and highlighting the necessity of asynchronous handling under heavy loads.

---

