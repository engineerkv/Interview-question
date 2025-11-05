# 🎬 6. Media Elements (Q76–85)

---

## 76) What are the different ways to embed media in HTML?

HTML provides multiple methods: `<img>`, `<video>`, `<audio>`, `<iframe>`, and `<object>` elements.

```html
<img src="image.jpg" alt="Description" width="300" height="200">
<video controls width="400" height="300">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
</video>
<audio controls><source src="audio.mp3" type="audio/mpeg"></audio>
```

- **Core Elements**: Each element serves specific media types (images, video, audio, iframes)
- **Real-World Use**: Use `<source>` for multiple format support, provide fallback content
- **Accessibility**: Consider accessibility with alt text, captions, and transcripts
- **Best Practice**: Choose appropriate element for content type, provide multiple formats
- **Interview Tip**: Explain that each element has specific use cases and attributes

---

## 77) How do you create responsive images?

Use `srcset` and `sizes` attributes to provide different image sizes for different screen densities and viewport widths.

```html
<img src="image-320w.jpg" 
     srcset="image-320w.jpg 320w, image-640w.jpg 640w, image-1280w.jpg 1280w"
     sizes="(max-width: 600px) 320px, (max-width: 1200px) 640px, 1280px"
     alt="Responsive image">
```

- **Core Attributes**: `srcset` provides multiple image sources, `sizes` tells browser which size to use
- **Real-World Use**: Reduces bandwidth on mobile devices, improves page load performance
- **Picture Element**: Enables art direction for different screen sizes
- **Performance**: Browser chooses appropriate size based on viewport and device pixel ratio
- **Interview Tip**: Explain that responsive images improve performance and user experience

---

## 78) What is the difference between `<img>` and `<picture>`?

`<img>` displays a single image. `<picture>` provides multiple image sources with media queries for different conditions.

```html
<img src="hero.jpg" alt="Hero image" srcset="hero-320w.jpg 320w, hero-640w.jpg 640w" sizes="(max-width: 600px) 320px, 640px">

<picture>
  <source media="(max-width: 600px)" srcset="hero-mobile.jpg">
  <source media="(min-width: 601px)" srcset="hero-desktop.jpg">
  <img src="hero.jpg" alt="Hero image">
</picture>
```

- **Core Difference**: `<img>` is simpler for basic responsive images, `<picture>` enables art direction
- **Real-World Use**: Use `<picture>` when you need different crops or formats for different screens
- **Format Selection**: `<picture>` can serve different formats (WebP, AVIF) based on browser support
- **Fallback**: Always include fallback `<img>` in `<picture>` for older browsers
- **Interview Tip**: Explain that `<picture>` is for art direction, `<img>` is for responsive sizing

---

## 79) How do you create accessible video content?

Use proper video structure with captions, transcripts, and controls for accessibility.

```html
<video controls width="800" height="450" poster="video-poster.jpg">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
  <track kind="subtitles" src="subtitles.vtt" srclang="es" label="Spanish">
</video>
```

- **Core Requirements**: Always provide captions for audio content, use `poster` attribute for thumbnail
- **Real-World Use**: Include multiple format sources, provide transcript for screen readers
- **Accessibility**: Test with keyboard navigation, ensure controls are accessible
- **Best Practice**: Use `<track>` elements with WebVTT files for captions and subtitles
- **Interview Tip**: Explain that accessible video is required by WCAG guidelines

---

## 80) What are the different video formats and codecs?

Different video formats offer varying compression, quality, and browser support trade-offs.

```html
<video controls>
  <source src="video.mp4" type="video/mp4; codecs=avc1.42E01E">
  <source src="video.webm" type="video/webm; codecs=vp9">
</video>
```

- **Core Formats**: MP4/H.264 (best browser support), WebM/VP9 (better compression), AV1 (next-gen)
- **Real-World Use**: Choose based on target audience, always provide MP4 fallback
- **Compression**: WebM/VP9 offers better compression, MP4 offers wider support
- **Quality Trade-offs**: Balance file size, quality, and browser support
- **Interview Tip**: Explain that multiple formats ensure cross-browser compatibility

---

## 81) How do you create audio players with controls?

Use `<audio>` element with controls and multiple source formats for cross-browser compatibility.

```html
<audio controls preload="metadata">
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <source src="audio.wav" type="audio/wav">
  <p>Your browser does not support the audio element.</p>
</audio>
```

- **Core Attributes**: `controls` shows default player, `preload` controls when audio loads
- **Real-World Use**: Provide multiple formats for compatibility, custom players offer more control
- **Accessibility**: Consider accessibility for custom controls, ensure keyboard navigation
- **Best Practice**: Provide fallback content for unsupported browsers
- **Interview Tip**: Explain that audio element is simpler than video, but similar principles apply

---

## 82) What is the purpose of the `<source>` element?

`<source>` provides alternative media sources for `<video>`, `<audio>`, and `<picture>` elements.

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <source src="video.ogv" type="video/ogg">
</video>
```

- **Core Purpose**: Provide fallback sources for unsupported formats, ensure cross-browser compatibility
- **Real-World Use**: Browser chooses first supported source, order sources by preference
- **Media Attribute**: Use `media` attribute for responsive sources based on screen size
- **Essential**: Essential for cross-browser compatibility, provides format fallbacks
- **Interview Tip**: Explain that browser tries sources in order until it finds one it supports

---

## 83) How do you create video subtitles and captions?

Use `<track>` elements with WebVTT files to provide subtitles and captions for video content.

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="subtitles" src="english.vtt" srclang="en" label="English" default>
  <track kind="captions" src="captions.vtt" srclang="en" label="English Captions">
  <track kind="chapters" src="chapters.vtt" srclang="en">
</video>
```

- **Core Format**: WebVTT is the standard format for captions and subtitles
- **Real-World Use**: Subtitles are translations, captions include audio descriptions
- **Track Types**: Use `kind="subtitles"`, `kind="captions"`, or `kind="chapters"`
- **Accessibility**: Essential for accessibility compliance, helps users with hearing impairments
- **Interview Tip**: Explain that WebVTT is the standard format, required for accessibility

---

## 84) What are the different image formats and when to use them?

Different image formats offer various compression, quality, and feature trade-offs for different use cases.

```html
<img src="photo.jpg" alt="Photograph">
<img src="logo.png" alt="Company logo">
<img src="image.webp" alt="Modern image" type="image/webp">
<img src="icon.svg" alt="Icon" width="24" height="24">
```

- **Core Formats**: JPEG (photos), PNG (transparency), WebP (better compression), SVG (scalable)
- **Real-World Use**: Choose based on content type, transparency needs, and browser support
- **JPEG**: Photos with many colors, no transparency, smaller file size
- **PNG**: Images with transparency, sharp edges, larger files
- **Interview Tip**: Explain that format choice affects file size, quality, and browser support

---

## 85) How do you optimize media for web performance?

Optimize media through proper sizing, compression, lazy loading, and modern formats to improve page performance.

```html
<img src="placeholder.jpg" data-src="actual-image.jpg" loading="lazy" alt="Description">
<img src="image-320w.jpg" srcset="image-320w.jpg 320w, image-640w.jpg 640w" sizes="(max-width: 600px) 320px, 640px" alt="Responsive">
<link rel="preload" as="image" href="hero-image.jpg">
```

- **Core Techniques**: Use `loading="lazy"` for below-fold images, provide appropriate sizes
- **Real-World Use**: Preload critical above-fold images, use `preload="metadata"` for videos
- **Modern Formats**: Consider WebP and AVIF for better compression
- **Compression**: Compress images without losing quality, balance file size and quality
- **Interview Tip**: Explain that media optimization significantly improves page load performance

---
