### Local Load Testing

I used k6 v2.2.0 to test two routes on the experimental optimised website, served locally using Python.

**Test configuration**
- Virtual users: 5
- Duration: 30 seconds
- Routes: `/index.html` and `/new-pieces.html`

**Recorded results**

| Metric | Result |
|---|---:|
| HTTP requests | 300 |
| Completed iterations | 150 |
| Checks passed | 600 / 600 |
| Failed HTTP requests | 0 |
| Average response time | 9.11 ms |
| Median response time | 6.81 ms |
| 95th percentile response time | 24.87 ms |
| Maximum response time | 49.86 ms |

These measurements represent a local test run, not production performance. The test checks HTTP status codes and non-empty response bodies; it does not measure browser rendering or Core Web Vitals.

- [View the detailed performance report](performance/results/performance-test-report.md)
- [Inspect the k6 test script](performance/scripts/site-load-test.js)
- [View the HTML size comparison](performance/results/html-size-comparison.csv)

