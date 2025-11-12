# 🎬 6. Media Elements (Q76–85)

---

## 🧩 Q76. How do you embed videos in HTML?

### 🧠 Concept

Use `<video>` element with controls and multiple source formats for cross-browser compatibility. Each element has specific use cases and attributes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Each element serves specific media types (images, video, audio, iframes).
* **Use Case:** Use `<source>` for multiple format support, provide fallback content.
* **Common Mistake:** Consider accessibility with alt text, captions, and transcripts.
* **Pro Tip:** Choose appropriate element for content type, provide multiple formats.

---

### ⭐ Senior Takeaway

Each element has specific use cases and attributes.

---

## 🧩 Q77. How do you create responsive images?

### 🧠 Concept

Use `srcset` and `sizes` attributes to provide different image sizes for different screen densities and viewport widths. Responsive images improve performance and user experience.

---

### 💡 Example

```html
<img src="image-320w.jpg" 
     srcset="image-320w.jpg 320w, image-640w.jpg 640w, image-1280w.jpg 1280w"
     sizes="(max-width: 600px) 320px, (max-width: 1200px) 640px, 1280px"
     alt="Responsive image">
```

---

### 🔍 Deep Insights

* **Rule:** `srcset` provides multiple image sources, `sizes` tells browser which size to use.
* **Use Case:** Reduces bandwidth on mobile devices, improves page load performance.
* **Common Mistake:** Picture element enables art direction for different screen sizes.
* **Pro Tip:** Browser chooses appropriate size based on viewport and device pixel ratio.

---

### ⭐ Senior Takeaway

Responsive images improve performance and user experience.

---

## 🧩 Q78. What is the difference between `<img>` and `<picture>`?

### 🧠 Concept

`<img>` displays a single image. `<picture>` provides multiple image sources with media queries for different conditions. `<picture>` is for art direction, `<img>` is for responsive sizing.

---

### 💡 Example

```html
<img src="hero.jpg" alt="Hero image" 
     srcset="hero-320w.jpg 320w, hero-640w.jpg 640w" 
     sizes="(max-width: 600px) 320px, 640px">

<picture>
  <source media="(max-width: 600px)" srcset="hero-mobile.jpg">
  <source media="(min-width: 601px)" srcset="hero-desktop.jpg">
  <img src="hero.jpg" alt="Hero image">
</picture>
```

---

### 🔍 Deep Insights

* **Rule:** `<img>` is simpler for basic responsive images, `<picture>` enables art direction.
* **Use Case:** Use `<picture>` when you need different crops or formats for different screens.
* **Common Mistake:** `<picture>` can serve different formats (WebP, AVIF) based on browser support.
* **Pro Tip:** Always include fallback `<img>` in `<picture>` for older browsers.

---

### ⭐ Senior Takeaway

`<picture>` is for art direction, `<img>` is for responsive sizing.

---

## 🧩 Q79. How do you create accessible videos?

### 🧠 Concept

Use proper video structure with captions, transcripts, and controls for accessibility. Accessible video is required by WCAG guidelines.

---

### 💡 Example

```html
<video controls width="800" height="450" poster="video-poster.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
  <track kind="subtitles" src="subtitles.vtt" srclang="es" label="Spanish">
</video>
```

---

### 🔍 Deep Insights

* **Rule:** Always provide captions for audio content, use `poster` attribute for thumbnail.
* **Use Case:** Include multiple format sources, provide transcript for screen readers.
* **Common Mistake:** Test with keyboard navigation, ensure controls are accessible.
* **Pro Tip:** Use `<track>` elements with WebVTT files for captions and subtitles.

---

### ⭐ Senior Takeaway

Accessible video is required by WCAG guidelines.

---

## 🧩 Q80. What are the different video formats?

### 🧠 Concept

Different video formats offer varying compression, quality, and browser support trade-offs. Multiple formats ensure cross-browser compatibility.

---

### 💡 Example

```html
<video controls>
  <source src="video.mp4" type="video/mp4; codecs=avc1.42E01E">
  <source src="video.webm" type="video/webm; codecs=vp9">
</video>
```

---

### 🔍 Deep Insights

* **Rule:** MP4/H.264 (best browser support), WebM/VP9 (better compression), AV1 (next-gen).
* **Use Case:** Choose based on target audience, always provide MP4 fallback.
* **Common Mistake:** WebM/VP9 offers better compression, MP4 offers wider support.
* **Pro Tip:** Balance file size, quality, and browser support.

---

### ⭐ Senior Takeaway

Multiple formats ensure cross-browser compatibility.

---

## 🧩 Q81. How do you create audio players?

### 🧠 Concept

Use `<audio>` element with controls and multiple source formats for cross-browser compatibility. Audio element is simpler than video, but similar principles apply.

---

### 💡 Example

```html
<audio controls preload="metadata">
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <source src="audio.wav" type="audio/wav">
  <p>Your browser does not support the audio element.</p>
</audio>
```

---

### 🔍 Deep Insights

* **Rule:** `controls` shows default player, `preload` controls when audio loads.
* **Use Case:** Provide multiple formats for compatibility, custom players offer more control.
* **Common Mistake:** Consider accessibility for custom controls, ensure keyboard navigation.
* **Pro Tip:** Provide fallback content for unsupported browsers.

---

### ⭐ Senior Takeaway

Audio element is simpler than video, but similar principles apply.

---

## 🧩 Q82. What is the purpose of the `<source>` element?

### 🧠 Concept

`<source>` provides alternative media sources for `<video>`, `<audio>`, and `<picture>` elements. Browser tries sources in order until it finds one it supports.

---

### 💡 Example

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogv" type="video/ogg">
</video>
```

---

### 🔍 Deep Insights

* **Rule:** Provide fallback sources for unsupported formats, ensure cross-browser compatibility.
* **Use Case:** Browser chooses first supported source, order sources by preference.
* **Common Mistake:** Use `media` attribute for responsive sources based on screen size.
* **Pro Tip:** Essential for cross-browser compatibility, provides format fallbacks.

---

### ⭐ Senior Takeaway

Browser tries sources in order until it finds one it supports.

---

## 🧩 Q83. How do you add subtitles to videos?

### 🧠 Concept

Use `<track>` elements with WebVTT files to provide subtitles and captions for video content. WebVTT is the standard format, required for accessibility.

---

### 💡 Example

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="subtitles" src="english.vtt" srclang="en" label="English" default>
  <track kind="captions" src="captions.vtt" srclang="en" label="English Captions">
  <track kind="chapters" src="chapters.vtt" srclang="en">
</video>
```

---

### 🔍 Deep Insights

* **Rule:** WebVTT is the standard format for captions and subtitles.
* **Use Case:** Subtitles are translations, captions include audio descriptions.
* **Common Mistake:** Use `kind="subtitles"`, `kind="captions"`, or `kind="chapters"`.
* **Pro Tip:** Essential for accessibility compliance, helps users with hearing impairments.

---

### ⭐ Senior Takeaway

WebVTT is the standard format, required for accessibility.

---

## 🧩 Q84. What are the different image formats?

### 🧠 Concept

Different image formats offer various compression, quality, and feature trade-offs for different use cases. Format choice affects file size, quality, and browser support.

---

### 💡 Example

```html
<img src="photo.jpg" alt="Photograph">
<img src="logo.png" alt="Company logo">
<img src="image.webp" alt="Modern image" type="image/webp">
<img src="icon.svg" alt="Icon" width="24" height="24">
```

---

### 🔍 Deep Insights

* **Rule:** JPEG (photos), PNG (transparency), WebP (better compression), SVG (scalable).
* **Use Case:** Choose based on content type, transparency needs, and browser support.
* **Common Mistake:** JPEG for photos with many colors, no transparency, smaller file size.
* **Pro Tip:** PNG for images with transparency, sharp edges, larger files.

---

### ⭐ Senior Takeaway

Format choice affects file size, quality, and browser support.

---

## 🧩 Q85. How do you optimize media for web?

### 🧠 Concept

Optimize media through proper sizing, compression, lazy loading, and modern formats to improve page performance. Media optimization significantly improves page load performance.

---

### 💡 Example

```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="Description">
<img src="image-320w.jpg" 
     srcset="image-320w.jpg 320w, image-640w.jpg 640w" 
     sizes="(max-width: 600px) 320px, 640px" 
     alt="Responsive">
<link rel="preload" as="image" href="hero-image.jpg">
```

---

### 🔍 Deep Insights

* **Rule:** Use `loading="lazy"` for below-fold images, provide appropriate sizes.
* **Use Case:** Preload critical above-fold images, use `preload="metadata"` for videos.
* **Common Mistake:** Consider WebP and AVIF for better compression.
* **Pro Tip:** Compress images without losing quality, balance file size and quality.

---

### ⭐ Senior Takeaway

Media optimization significantly improves page load performance.

---
