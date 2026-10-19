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

## Lighthouse experiment: hero visibility CSS

**Date:** 19 October 2026  
**Environment:** Local optimized copy, Chrome Lighthouse 13.4.1, emulated Moto G Power, Slow 4G.

The hero eyebrow, heading, subtitle and call-to-action elements originally started with `opacity: 0` and `translateY(36px)`. In the experimental copy, their initial CSS was changed to `opacity: 1` and `transform: none`, so the hero content could render without waiting for its entrance animation. The intro overlay was retained.

| Metric | Earlier optimized runs | After CSS change |
|---|---:|---:|
| Performance score | 70–77 | 82–86 |
| Largest Contentful Paint | 6.3–6.4 s | 4.1–4.7 s |
| First Contentful Paint | 1.7–2.7 s | 1.7 s |
| Total Blocking Time | 0–310 ms | 0 ms |
| Cumulative Layout Shift | 0 | 0 |

The two post-change Lighthouse runs showed LCP values of 4.1 s and 4.7 s. This is a promising improvement, but Lighthouse scores and timings vary between runs. The experiment suggests that the CSS visibility/animation behavior may contribute to LCP; it does not establish causation by itself.

These measurements were taken against a local development server under simulated mobile conditions. They are not production measurements and do not guarantee equivalent improvements for visitors to the live website. The change has only been tested in the experimental copy; the live website remains unchanged.

Remaining opportunities include image delivery, browser cache lifetimes and render-blocking resources.
