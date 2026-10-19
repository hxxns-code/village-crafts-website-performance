# Village Crafts — Website Development & Performance Study

*A story-driven digital showroom connecting handcrafted furniture from Jodhpur and fine mussars from Srinagar with homes in Oman.*

**Live website:** https://villagecrafts.shop/

## Overview

Village Crafts is a local business in Qurum, Muscat, Oman, founded by Ahmed Hilal. It offers handmade furniture from Jodhpur, India, and fine pashmina mussars from Srinagar, Kashmir.

The website was designed as an immersive, story-driven experience rather than a conventional online shop. It guides visitors from the origins of the products through craftsmanship and collection discovery to a personal introduction to the founder and a direct enquiry.

The central idea is: **Bring home a piece of its story.**

There is no online checkout. Customers enquire directly through WhatsApp.

## Part 1 — Website Development

### Concept and storytelling

The homepage follows a deliberate narrative:

1. **Hero:** A skippable introduction leads into a full-screen opening.
2. **The Journey:** An animated route traces the products' journey from Srinagar and Jodhpur to Muscat.
3. **The Craft:** Four visual stages explore wood grain, hand carving, brass inlay and the finished piece.
4. **New Pieces:** Selected furniture is presented with individual enquiry actions.
5. **Why Village Crafts:** Communicates the shop's qualities and values.
6. **Gallery:** A visual grid with a full-screen lightbox.
7. **A Note from the Owner:** A personal letter-style card from Ahmed Hilal.
8. **Contact:** WhatsApp, Instagram and showroom location details.

The story moves from origin to craftsmanship, then to the object, the person and finally an invitation to enquire.

### Design language: Wood and mussar

**Wood-inspired design**
- Dark walnut palette with warm brass and gold accents.
- Oxblood red highlights and parchment-cream reading surfaces.
- Subtle CSS wood-grain textures.
- Plaque-inspired image frames and brass-outline product-card hover effects.

**Woven-inspired design**
- Fine diagonal twill textures across selected sections.
- Drifting paisley (boteh) border strips used as section dividers.
- A brass-and-red progress bar that fills as the visitor scrolls, inspired by a thread being woven.

**Motion and interaction**
- Scroll-triggered reveal animations.
- Soft image fades.
- Full-screen gallery lightbox.
- Floating WhatsApp enquiry button.
- Responsive layouts for desktop and mobile.

### Website pages

| File | Description |
|---|---|
| `index.html` | Main story experience, from the hero to the final contact section. |
| `our-story.html` | Introduces the Srinagar and Jodhpur product origins. |
| `collection.html` | Horizontally scrolling featured collection with WhatsApp enquiries. |
| `new-pieces.html` | Presents 25 new pieces with individual enquiry messages. |
| `gallery.html` | Image gallery with a full-screen lightbox. |
| `contact.html` | WhatsApp, Instagram, showroom location and directions. |

### Enquiry workflow

The site uses WhatsApp deep links with prefilled messages identifying the selected product, for example:

> Hello Village Crafts, I'd like to enquire about the [piece name]

This connects product discovery to a direct conversation without requiring a custom backend, shopping cart or payment gateway.

## Part 2 — Performance Analysis

### Investigation

The original HTML files contained large Base64-encoded image payloads. I investigated their document sizes and created a separate experimental copy that extracted images into local asset files and reused identical image files where possible.

The live website and original source files were not modified by this experiment.

### HTML size comparison

| Page | Original HTML (KB) | Experimental HTML (KB) | Reduction |
|---|---:|---:|---:|
| Home | 3938.7 | 66.8 | 98.3% |
| Collection | 1859.3 | 44.7 | 97.6% |
| Contact | 616.2 | 73.2 | 88.1% |
| Gallery | 3115.2 | 69.5 | 97.8% |
| New Pieces | 6266.8 | 91.8 | 98.5% |
| Our Story | 1079.1 | 43.0 | 96.0% |

These reductions refer to HTML file sizes only. They do not establish the same reduction in total page downloads or prove improved real-world loading speed.

### Validation and limitations

- Confirmed all six experimental HTML pages were present.
- Checked 70 detected local asset references; no missing files were reported.
- Inspected the experimental pages in a browser.
- Some embedded image data remained and requires further investigation.
- Used HTTP requests and k6 for exploratory performance measurements.
- Localhost timings are not directly comparable with production measurements.

A controlled browser-based test and a review of total transfer size would be needed to establish the user-perceived performance impact.

## Tech stack

- HTML5
- CSS3
- Vanilla JavaScript
- GSAP and ScrollTrigger
- Google Fonts
- WhatsApp deep links
- Google Maps links
- Python for the optimization experiment
- PowerShell for validation and file operations
- Git and GitHub
- Cloudflare hosting and DNS

The website uses no frontend framework or build step. Images in the original website are embedded directly in the HTML.

## Repository structure

```text
village-crafts-performance-study/
├── README.md
├── .gitignore
├── performance/
│   ├── scripts/
│   │   └── optimize_village_site.py
│   └── results/
│       └── html-size-comparison.csv
├── screenshots/
└── website/                 # Local only; excluded from Git
    ├── index.html
    ├── our-story.html
    ├── collection.html
    ├── new-pieces.html
    └── ...
```

The `website/` folder contains the local source copy and is excluded from Git until permission to publish the client source and imagery is confirmed.

## Run locally

The website is static and has no build step.

1. Obtain the website source files with appropriate permission.
2. Open `index.html` in a browser.

Alternatively, run a simple local server from the website directory:

```bash
python -m http.server 8000
```

Open `http://localhost:8000` in your browser.

## Deployment

The live site is hosted on Cloudflare using the custom domain:

**https://villagecrafts.shop/**

The domain was configured through NameSilo and connected to Cloudflare. The current enquiry workflow relies on WhatsApp links rather than a custom backend.

## Roadmap

- [ ] Replace generated imagery with professional photography of the actual stock.
- [ ] Investigate and remove remaining embedded image data where appropriate.
- [ ] Measure total page transfer size and browser-based loading performance under controlled conditions.
- [ ] Review accessibility, keyboard navigation, image descriptions and reduced-motion support.
- [ ] Continue refining responsive layouts and animation behaviour.
- [ ] Consider a maintainable product content workflow as the collection grows.

## Credits and transparency

- **Business:** Village Crafts, founded by Ahmed Hilal, Muscat, Oman.
- **Imagery:** Images are AI-generated visualisations created with Google Gemini to represent the shop's real products. They are not photographs taken in the shop, a workshop or the artisans' studios.
- **Implementation:** AI-assisted coding was used alongside human direction, content and design decisions, asset selection, configuration, review and testing.
- **Libraries and services:** GSAP, GSAP ScrollTrigger, Google Fonts, WhatsApp, Google Maps and Cloudflare.

## Screenshot

Add a representative homepage screenshot here.

`[Homepage screenshot placeholder]`

---

*Village Crafts — Bring home a piece of its story.*
