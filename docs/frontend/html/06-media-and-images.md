---
sidebar_label: "Media & Images"
---
# 🎬 6. Media & Images (Q76–85)
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q76. 📄 Embedding videos in HTML

Use `<video>` element with controls and multiple source formats for cross-browser compatibility - each element has specific use cases and attributes. Each element serves specific media types (images, video, audio, iframes).

- **Trade-offs**: The catch is consider accessibility with alt text, captions, and transcripts - choose appropriate element for content type, provide multiple formats. Each element has specific use cases and attributes, but watch out - use `<source>` for multiple format support, provide fallback content.

Example:

```html
<img src="image.jpg" alt="Description" width="300" height="200">
<video controls width="400" height="300">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
</video>
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>

```

---

## Q77. 💡 Creating responsive images

Use `srcset` and `sizes` attributes to provide different image sizes for different screen densities and viewport widths - responsive images improve performance and user experience. `srcset` provides multiple image sources, `sizes` tells browser which size to use.

- **Trade-offs**: The catch is picture element enables art direction for different screen sizes - browser chooses appropriate size based on viewport and device pixel ratio. Responsive images improve performance and user experience, but watch out - reduces bandwidth on mobile devices, improves page load performance.

Example:

```html
<img src="image-320w.jpg"
     srcset="image-320w.jpg 320w, image-640w.jpg 640w, image-1280w.jpg 1280w"
     sizes="(max-width: 600px) 320px, (max-width: 1200px) 640px, 1280px"
     alt="Responsive image">

```

- **How the browser picks**: with `w` descriptors, the browser reads `sizes` (the image's rendered **CSS width** at each viewport condition), multiplies by the device pixel ratio, and picks the smallest candidate that's big enough. `sizes` should describe the layout — e.g. a full-bleed image is `100vw`, a 3-column grid card might be `(min-width: 1024px) 33vw, 100vw`. Getting `sizes` wrong (or omitting it — the default is `100vw`) is the most common reason phones download desktop-sized images.
- **Density descriptors** (`1x`, `2x`) are simpler for fixed-size images like logos and avatars: `srcset="avatar.png 1x, avatar@2x.png 2x"`.
- **Always set `width` and `height`** (or CSS `aspect-ratio`) so the browser reserves space and avoids layout shift (CLS).
- **Lazy images and `sizes="auto"`**: for `loading="lazy"` images, `sizes="auto"` lets the browser use the actual layout width — newer, Chromium-first; include a fallback value like `sizes="auto, 100vw"`.
- In practice, frameworks and image CDNs generate these (Next.js `<Image>`, Astro `<Image>`, Cloudinary/imgix URLs).

```html
<img src="card-640.avif"
     srcset="card-320.avif 320w, card-640.avif 640w, card-960.avif 960w"
     sizes="(min-width: 1024px) 33vw, 100vw"
     width="640" height="400"
     loading="lazy" decoding="async"
     alt="Product photo">
```

---

## Q78. 🤔 `<img>` vs `<picture>`

`<img>` displays a single image, while `<picture>` provides multiple image sources with media queries for different conditions - `<picture>` is for art direction, `<img>` is for responsive sizing. `<img>` is simpler for basic responsive images, `<picture>` enables art direction.

- **Trade-offs**: The catch is `<picture>` can serve different formats (WebP, AVIF) based on browser support - always include fallback `<img>` in `<picture>` for older browsers. `<picture>` is for art direction, `<img>` is for responsive sizing, but watch out - use `<picture>` when you need different crops or formats for different screens.

Example:

```html
<img src="hero.jpg" alt="Hero image"
     srcset="hero-320w.jpg 320w, hero-640w.jpg 640w"
     sizes="(max-width: 600px) 320px, 640px">

<picture>
  <source media="(max-width: 600px)" srcset="hero-mobile.jpg">
  <source media="(min-width: 601px)" srcset="hero-desktop.jpg">
  <img src="hero.jpg" alt="Hero image">
</picture>

<!-- Format fallback: first supported type wins; <img> carries alt, size, and loading attributes -->
<picture>
  <source type="image/avif" srcset="hero-800.avif 800w, hero-1600.avif 1600w" sizes="100vw">
  <source type="image/webp" srcset="hero-800.webp 800w, hero-1600.webp 1600w" sizes="100vw">
  <img src="hero-1600.jpg" srcset="hero-800.jpg 800w, hero-1600.jpg 1600w" sizes="100vw"
       width="1600" height="900" alt="Mountain lake at sunrise" fetchpriority="high">
</picture>

```

- **2026 note**: WebP is supported by all current browsers and AVIF by all major engines (Baseline since 2024), so a format `<picture>` is mostly about squeezing extra bytes with AVIF while keeping WebP/JPEG as fallbacks. If your image CDN does **content negotiation** via the `Accept` header, a plain `<img>` can get AVIF automatically — no `<picture>` needed. The `<img>` inside `<picture>` is required: it's what actually renders, and it's where `alt`, `width`/`height`, `loading`, and `fetchpriority` go.

---

## Q79. 🎥 Creating accessible videos

Use proper video structure with captions, transcripts, and controls for accessibility - accessible video is required by WCAG guidelines. Always provide captions for audio content, use `poster` attribute for thumbnail.

- **Trade-offs**: The catch is test with keyboard navigation, ensure controls are accessible - use `<track>` elements with WebVTT files for captions and subtitles. Accessible video is required by WCAG guidelines, but watch out - include multiple format sources, provide transcript for screen readers.

Example:

```html
<video controls width="800" height="450" poster="video-poster.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
  <track kind="subtitles" src="subtitles.vtt" srclang="es" label="Spanish">
</video>

```

---

## Q80. 📝 Different video formats

Different video formats offer varying compression, quality, and browser support trade-offs - multiple formats ensure cross-browser compatibility. MP4/H.264 (best browser support), WebM/VP9 (better compression), AV1 (next-gen; widely supported in current browsers, but hardware decoding varies on older devices, so keep an H.264 fallback). For long or large videos, use **adaptive streaming** (HLS or DASH, via Media Source Extensions and a player like hls.js/Shaka) or a video platform rather than a single progressive MP4.

- **Trade-offs**: The catch is WebM/VP9 offers better compression, MP4 offers wider support - balance file size, quality, and browser support. Multiple formats ensure cross-browser compatibility, but watch out - choose based on target audience, always provide MP4 fallback.

Example:

```html
<video controls>
  <source src="video.mp4" type="video/mp4; codecs=avc1.42E01E">
  <source src="video.webm" type="video/webm; codecs=vp9">
</video>

```

---

## Q81. 🔊 Creating audio players

Use `<audio>` element with controls and multiple source formats for cross-browser compatibility - audio element is simpler than video, but similar principles apply. `controls` shows default player, `preload` controls when audio loads.

- **Trade-offs**: The catch is consider accessibility for custom controls, ensure keyboard navigation - provide fallback content for unsupported browsers. Audio element is simpler than video, but similar principles apply, but watch out - provide multiple formats for compatibility, custom players offer more control.

Example:

```html
<audio controls preload="metadata">
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <source src="audio.wav" type="audio/wav">
  <p>Your browser does not support the audio element.</p>
</audio>

```

---

## Q82. 💡 Purpose of the `<source>` element

`<source>` provides alternative media sources for `<video>`, `<audio>`, and `<picture>` elements - browser tries sources in order until it finds one it supports. Provide fallback sources for unsupported formats, ensure cross-browser compatibility.

- **Trade-offs**: The catch is use `media` attribute for responsive sources based on screen size - essential for cross-browser compatibility, provides format fallbacks. Browser tries sources in order until it finds one it supports, but watch out - browser chooses first supported source, order sources by preference.

Example:

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogv" type="video/ogg">
</video>

```

> **Legacy note (2026):** Ogg Theora (`.ogv`) video is legacy — it's being removed from some browsers. Put the most efficient format first (AV1/VP9 WebM), with H.264 MP4 as the broad fallback.

---

## Q83. 🎥 Adding subtitles to videos

Use `<track>` elements with WebVTT files to provide subtitles and captions for video content - WebVTT is the standard format, required for accessibility. WebVTT is the standard format for captions and subtitles.

- **Trade-offs**: The catch is use `kind="subtitles"`, `kind="captions"`, or `kind="chapters"` - essential for accessibility compliance, helps users with hearing impairments. WebVTT is the standard format, required for accessibility, but watch out - subtitles are translations, captions include audio descriptions.

Example:

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="subtitles" src="english.vtt" srclang="en" label="English" default>
  <track kind="captions" src="captions.vtt" srclang="en" label="English Captions">
  <track kind="chapters" src="chapters.vtt" srclang="en">
</video>

```

---

## Q84. 📝 Different image formats

Different image formats offer various compression, quality, and feature trade-offs for different use cases - format choice affects file size, quality, and browser support. JPEG (photos), PNG (transparency), WebP (better compression, transparency, animation), AVIF (typically the smallest for photos at similar quality; slower to encode), SVG (scalable vector). JPEG XL has strong technical merits but limited browser support — not a safe default at the time of review. Replace animated GIFs with muted, looping `<video>` (or animated WebP/AVIF) — GIFs are very large.

- **Trade-offs**: The catch is JPEG for photos with many colors, no transparency, smaller file size - PNG for images with transparency, sharp edges, larger files. Format choice affects file size, quality, and browser support, but watch out - choose based on content type, transparency needs, and browser support.

Example:

```html
<img src="photo.jpg" alt="Photograph">
<img src="logo.png" alt="Company logo">
<img src="image.webp" alt="Modern image"> <!-- note: <img> has no type attribute; use <picture><source type> for format fallbacks -->
<video autoplay muted loop playsinline src="animation.mp4" aria-label="Loading animation"></video> <!-- instead of a large GIF -->
<img src="icon.svg" alt="Icon" width="24" height="24">

```

---

## Q85. 🎬 Optimizing media for web

Optimize media through proper sizing, compression, lazy loading, and modern formats to improve page performance - media optimization significantly improves page load performance. Use `loading="lazy"` for below-fold images, provide appropriate sizes.

- **Trade-offs**: The catch is consider WebP and AVIF for better compression - compress images without losing quality, balance file size and quality. Media optimization significantly improves page load performance, but watch out - preload critical above-fold images, use `preload="metadata"` for videos.

Example:

```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="Description">
<img src="image-320w.jpg"
     srcset="image-320w.jpg 320w, image-640w.jpg 640w"
     sizes="(max-width: 600px) 320px, 640px"
     alt="Responsive">
<link rel="preload" as="image" href="hero-image.jpg">

```

- **Modern checklist**:
  - `data-src` + JavaScript lazy loading is **legacy** — native `loading="lazy"` (Baseline) is enough for most cases. (The first line above mixes both patterns; don't do that in new code.)
  - **Never lazy-load the LCP image** (usually the hero). Give it `fetchpriority="high"` and leave `loading` at its default `eager`.
  - If the LCP image is discovered late (CSS background, JS-rendered), preload it — and for responsive images use `imagesrcset`/`imagesizes` on the preload so the right size is fetched.
  - Set `width`/`height` on every image and video to prevent CLS; use `decoding="async"` for non-critical images.
  - Videos: `preload="metadata"` or `preload="none"` plus a `poster`; `autoplay` requires `muted` (and `playsinline` on iOS).
  - Serve AVIF/WebP via `<picture>` or CDN negotiation, and compress at build time or with an image CDN.

```html
<link rel="preload" as="image" fetchpriority="high"
      imagesrcset="hero-800.avif 800w, hero-1600.avif 1600w" imagesizes="100vw" type="image/avif">
<img src="hero-1600.avif" srcset="hero-800.avif 800w, hero-1600.avif 1600w" sizes="100vw"
     width="1600" height="900" fetchpriority="high" alt="Hero">
```

---

