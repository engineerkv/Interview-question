# Duplicate and Overlapping Questions Analysis

## Found Duplicates

### 1. Controlled vs Uncontrolled Components
- **Q9** in `1) React Fundamentals.md`
- **Q68** (should be Q66) in `7) React Architecture & Core Concepts.md`
- **Recommendation**: Keep in Fundamentals, remove from Architecture or merge into comprehensive answer

### 2. Reconciliation
- **Q11** in `1) React Fundamentals.md` - Basic explanation
- **Q68** (should be Q59) in `7) React Architecture & Core Concepts.md` - More detailed with Fiber
- **Recommendation**: Keep both but differentiate - Fundamentals covers basics, Architecture covers Fiber implementation

### 3. Strict Mode
- **Q54** in `6) React Latest Features.md`
- **Q68** (should be Q63) in `7) React Architecture & Core Concepts.md`
- **Recommendation**: Keep in Latest Features, remove from Architecture or reference it

### 4. Refs and Ref Forwarding
- **Q15, Q16** in `2) React Hooks.md` - useRef and refs vs state
- **Q68** (should be Q65) in `7) React Architecture & Core Concepts.md` - Ref forwarding
- **Recommendation**: Keep both - Hooks covers basics, Architecture covers advanced forwarding

### 5. React Profiler
- **Q82** (multiple) in `8) Performance Optimization.md`
- **Q68** (should be Q66) in `7) React Architecture & Core Concepts.md`
- **Recommendation**: Keep in Performance Optimization, remove from Architecture or make it a reference

## Numbering Issues in Architecture File

The file `7) React Architecture & Core Concepts.md` has:
- Q57: Fiber architecture ✓
- Q68: Multiple questions incorrectly numbered (should be Q58-Q66)

**Fixed numbering should be:**
- Q57: Fiber architecture
- Q58: How Fiber improves reconciliation
- Q59: Reconciliation details
- Q60: React Portals
- Q61: Error Boundaries
- Q62: HOCs and Render Props
- Q63: Strict Mode (DUPLICATE - remove or reference)
- Q64: Refs and ref forwarding
- Q65: Controlled vs uncontrolled (DUPLICATE - remove or reference)
- Q66: React Profiler (DUPLICATE - remove or reference)

