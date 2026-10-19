# Local Website Load Test Report

## Test setup
- Tool: k6 v2.2.0
- Python: 3.14.6
- Target: Experimental optimized website running locally
- Virtual users: 5
- Duration: 30 seconds
- Routes tested: /index.html and /new-pieces.html

## Recorded results

| Metric | Result |
|---|---:|
| HTTP requests | 300 |
| Completed iterations | 150 |
| Checks passed | 600 / 600 |
| Failed HTTP requests | 0 |
| Average response time | 9.11 ms |
| Median response time | 6.81 ms |
| p90 response time | 18.44 ms |
| p95 response time | 24.87 ms |
| Maximum response time | 49.86 ms |

## Limitations

These figures represent one local test run, not production performance. They do not prove an equivalent improvement in real-world page-load speed. Only two routes were tested, and browser rendering and Core Web Vitals were not measured.
