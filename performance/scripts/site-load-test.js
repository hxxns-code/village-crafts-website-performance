import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'http://127.0.0.1:8000';

export const options = {
  vus: 5,
  duration: '30s',
};

export default function () {
  const pages = [
    { name: 'homepage', path: '/index.html' },
    { name: 'new-pieces', path: '/new-pieces.html' },
  ];

  for (const page of pages) {
    const response = http.get(`${BASE_URL}${page.path}`, {
      tags: { page: page.name },
    });

    check(response, {
      [`${page.name}: status is 200`]: (r) => r.status === 200,
      [`${page.name}: response has a body`]: (r) => r.body !== null && r.body.length > 0,
    });
  }

  sleep(1);
}
