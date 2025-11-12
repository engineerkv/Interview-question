# 🔍 Duplicates and Overlaps Analysis - Frontend Section

## Critical Duplicates Found

### 1. Debounce/Throttle
- **JavaScript Q82**: Write a debounce function (implementation)
- **JavaScript Q85**: Write a throttle function (implementation)
- **JavaScript Q99**: debounce + immediate (advanced)
- **FE-System-Design Q60**: debouncing vs throttling (conceptual comparison)
- **Status**: ✅ ACCEPTABLE - Different perspectives (implementation vs concept)

### 2. Event Loop / Microtasks
- **JavaScript Q38**: microtasks vs macrotasks (detailed)
- **JavaScript Q39**: event loop handles Promises (detailed)
- **JavaScript Q108**: microtask queue concept (output question)
- **FE-System-Design Q58**: event loop in browsers vs Node.js (comparison)
- **Status**: ⚠️ OVERLAP - Q38 and Q108 are very similar

### 3. Service Workers
- **JavaScript Q173**: What are Service Workers?
- **JavaScript Q174**: Service Worker lifecycle events
- **JavaScript Q175**: Service Workers enable offline caching
- **JavaScript Q176**: Web Workers vs Service Workers
- **JavaScript Q177**: background sync or push notifications
- **FE-System-Design Q38**: service workers for offline caching
- **FE-System-Design Q61**: web workers vs service workers
- **FE-System-Design Q129**: service worker and caching
- **FE-System-Design Q130**: Service worker caching vs traditional browser caching
- **FE-System-Design Q131**: SW caching strategies
- **Status**: ⚠️ SIGNIFICANT OVERLAP - Multiple questions on same topic

### 4. Reflow/Repaint
- **FE-System-Design Q56**: reflow vs repaint, and how to minimize them
- **FE-System-Design Q63**: optimizations for paint and layout performance
- **JavaScript Q106**: techniques for reducing reflows and repaints
- **Status**: ✅ FIXED - Removed JavaScript Q106 (duplicate of FE-System-Design Q56), renumbered Q107-Q167 to Q106-Q166

### 5. Rendering Patterns (CSR, SSR, SSG, ISR)
- **FE-System-Design Q7**: difference between CSR, SSR, SSG, and ISR (basic intro, references Q64 for advanced)
- **FE-System-Design Q64**: rendering patterns (CSR, SSR, SSG, ISR, Streaming SSR, Partial Hydration, Islands Architecture)
- **Next.js Q11**: different rendering strategies in Next.js
- **Next.js Q2**: SSR, SSG, ISR core features
- **Status**: ✅ FIXED - Q7 now references Q64 for advanced patterns, Q64 remains comprehensive

### 6. Virtual DOM / Reconciliation
- **React Q4**: Virtual DOM and how it works
- **React Q5**: difference between real DOM and virtual DOM
- **React Q6**: Real DOM and why it's expensive
- **React Q11**: reconciliation in React and how React decides what to re-render (enhanced with Q61 content)
- **React Q61**: React Fiber and how it improves reconciliation (changed from duplicate reconciliation question)
- **Status**: ✅ FIXED - Q11 enhanced with Q61 content, Q61 changed to React Fiber topic

### 7. Flatten Array
- **JavaScript Q86**: Flatten a deeply nested array
- **JavaScript Q111**: Write a function to flatten a nested array
- **Status**: ✅ FIXED - Removed Q111, renumbered all subsequent questions

## Numbering Issues

### FE-System-Design
- **Section 7**: Shows Q65-Q84 (20 questions) - Header says Q65-84 ✓
- **Section 8**: Shows Q85-Q105 (21 questions) - Header says Q85-105 ✓
- **Section 9**: Shows Q106-Q120 (15 questions) - Header says Q106-120 ✓
- **Section 10**: Shows Q121-Q138 (18 questions) - Header says Q121-138 ✓
- **question.md**: Section 7 says Q66-85, Section 9 says Q106-111 ❌ MISMATCH

### JavaScript
- **Section 9**: All questions incorrectly numbered Q187 - ✅ FIXED (now Q169-Q188)
- **Section 8**: Removed duplicate Q111 (flatten array) - ✅ FIXED
- **Section 8**: Renumbered Q112-Q168 to Q111-Q167 - ✅ FIXED

## Recommendations

1. ✅ **Remove JavaScript Q111** (flatten array) - duplicate of Q86 - **FIXED**
2. ⚠️ **Merge or differentiate** JavaScript Q38 and Q108 (microtasks) - **PENDING**
3. ⚠️ **Consolidate Service Worker questions** - too many overlapping questions - **PENDING**
4. ✅ **Merge FE-System-Design Q7 and Q64** - Q7 now references Q64 for advanced patterns - **FIXED**
5. ✅ **Differentiate React Q11 and Q61** - Q11 enhanced, Q61 changed to React Fiber - **FIXED**
6. ✅ **Fix FE-System-Design question.md** numbering - **FIXED**
7. ✅ **Remove JavaScript Q106** (reflow/repaint) - duplicate of FE-System-Design Q56 - **FIXED**
8. ✅ **Fix FE-System-Design Q8 and Q10** - Q8 completed, Q10 changed to i18n - **FIXED**

