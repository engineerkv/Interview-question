# 🎬 6. Media Elements (Q76–85)

---

## 76) What are the different ways to embed media in HTML?

Concept:
HTML provides multiple methods for embedding media: `<img>`, `<video>`, `<audio>`, `<iframe>`, and `<object>` elements.

Example:
```html
<!-- Images -->
<img src="image.jpg" alt="Description" width="300" height="200">

<!-- Video -->
<video controls width="400" height="300">
  <source src="video.mp4" type="video/mp4">
```

Deep Insight:
- Each element serves specific media types
- Use `<source>` for multiple format support
- Provide fallback content for unsupported browsers
- Consider accessibility with alt text and captions
- Choose appropriate element for content type

---

## 77) How do you create responsive images?

Concept:
Use `srcset` and `sizes` attributes to provide different image sizes for different screen densities and viewport widths.

Example:
```html
<!-- Basic responsive image -->
<img src="image-320w.jpg" 
     srcset="image-320w.jpg 320w, 
             image-640w.jpg 640w, 
             image-1280w.jpg 1280w"
     sizes="(max-width: 600px) 320px, 
```

Deep Insight:
- `srcset` provides multiple image sources
- `sizes` tells browser which size to use
- Picture element enables art direction
- Reduces bandwidth on mobile devices
- Improves page load performance

---

## 78) What is the difference between `<img>` and `<picture>`?

Concept:
`<img>` displays a single image; `<picture>` provides multiple image sources with media queries for different conditions.

Example:
```html
<!-- img: single image -->
<img src="hero.jpg" alt="Hero image" 
     srcset="hero-320w.jpg 320w, hero-640w.jpg 640w"
     sizes="(max-width: 600px) 320px, 640px">

<!-- picture: multiple sources with conditions -->
```

Deep Insight:
- `<img>` is simpler for basic responsive images
- `<picture>` enables art direction and format selection
- `<picture>` can serve different formats (WebP, AVIF)
- Use `<picture>` when you need different crops
- Always include fallback `<img>` in `<picture>`

---

## 79) How do you create accessible video content?

Concept:
Use proper video structure with captions, transcripts, and controls for accessibility.

Example:
```html
<video controls width="800" height="450" 
       poster="video-poster.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  
  <!-- Captions and subtitles -->
```

Deep Insight:
- Always provide captions for audio content
- Use `poster` attribute for video thumbnail
- Include multiple format sources
- Provide transcript for screen readers
- Test with keyboard navigation

---

## 80) What are the different video formats and codecs?

Concept:
Different video formats offer varying compression, quality, and browser support trade-offs.

Example:
```html
<video controls>
  <!-- MP4 with H.264 (widest support) -->
  <source src="video.mp4" type="video/mp4; codecs=avc1.42E01E">
  
  <!-- WebM with VP9 (better compression) -->
  <source src="video.webm" type="video/webm; codecs=vp9">
```

Deep Insight:
- MP4/H.264: Best browser support, larger files
- WebM/VP9: Better compression, good support
- AV1: Next-gen codec, limited support
- Choose based on target audience
- Always provide MP4 fallback

---

## 81) How do you create audio players with controls?

Concept:
Use `<audio>` element with controls and multiple source formats for cross-browser compatibility.

Example:
```html
<audio controls preload="metadata">
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <source src="audio.wav" type="audio/wav">
  
  <!-- Fallback for older browsers -->
```

Deep Insight:
- `controls` attribute shows default player
- `preload` controls when audio loads
- Provide multiple formats for compatibility
- Custom players offer more control
- Consider accessibility for custom controls

---

## 82) What is the purpose of the `<source>` element?

Concept:
`<source>` provides alternative media sources for `<video>`, `<audio>`, and `<picture>` elements.

Example:
```html
<!-- Video with multiple sources -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogv" type="video/ogg">
</video>
```

Deep Insight:
- Browser chooses first supported source
- Order sources by preference
- Use `media` attribute for responsive sources
- Provides fallback for unsupported formats
- Essential for cross-browser compatibility

---

## 83) How do you create video subtitles and captions?

Concept:
Use `<track>` elements with WebVTT files to provide subtitles and captions for video content.

Example:
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  
  <!-- Subtitles (translation) -->
  <track kind="subtitles" src="english.vtt" 
         srclang="en" label="English" default>
```

Deep Insight:
- WebVTT is the standard format for captions
- Subtitles are translations, captions include descriptions
- `default` attribute selects initial track
- Chapters help with navigation
- Essential for accessibility compliance

---

## 84) What are the different image formats and when to use them?

Concept:
Different image formats offer various compression, quality, and feature trade-offs for different use cases.

Example:
```html
<!-- JPEG: Photos with many colors -->
<img src="photo.jpg" alt="Photograph">

<!-- PNG: Images with transparency -->
<img src="logo.png" alt="Company logo">

```

Deep Insight:
- JPEG: Photos, many colors, no transparency
- PNG: Transparency, sharp edges, larger files
- WebP: Better compression, limited support
- SVG: Scalable, small file size, sharp at any size
- Choose based on content type and browser support

---

## 85) How do you optimize media for web performance?

Concept:
Optimize media through proper sizing, compression, lazy loading, and modern formats to improve page performance.

Example:
```html
<!-- Lazy loading images -->
<img src="placeholder.jpg" 
     data-src="actual-image.jpg" 
     loading="lazy" 
     alt="Description">

```

Deep Insight:
- Use `loading="lazy"` for below-fold images
- Provide appropriate image sizes for different screens
- Preload critical above-fold images
- Use `preload="metadata"` for videos
- Consider modern formats like WebP and AVIF
- Compress images without losing quality
