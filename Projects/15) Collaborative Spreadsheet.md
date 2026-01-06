# Collaborative Spreadsheet System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Food Delivery System](14%29%20Food%20Delivery%20System.md) • [Next: Collaborative Word Processor →](16%29%20Collaborative%20Word%20Processor.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a collaborative spreadsheet application where multiple users can edit spreadsheets in real-time, similar to Google Sheets or Microsoft Excel Online. The system needs to handle formulas, cell formatting, and real-time synchronization.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Create, edit, and delete spreadsheets
- Real-time collaborative editing with multiple users (50+ concurrent editors)
- Formula engine supporting common functions (SUM, AVERAGE, IF, VLOOKUP, etc.)
- Cell formatting (bold, italic, colors, borders, alignment, number formats)
- Multiple sheets per workbook (tabs)
- Data import/export (CSV, Excel, JSON)
- Charts and graphs visualization
- Freeze panes and cell merging
- Undo/redo functionality
- Search and find/replace

**Collaboration Features:**
- Real-time cell updates visible to all users
- Presence indicators (who's viewing/editing)
- Cursor positions for active users
- Conflict resolution for simultaneous edits

### Non-Functional Requirements

**Performance:**
- Cell updates: < 100ms latency
- Formula recalculation: < 200ms
- Support spreadsheets with 10K+ rows and 1K+ columns
- Fast scrolling and rendering for large datasets

**Scalability:**
- Handle millions of spreadsheets
- Support 50+ concurrent editors per sheet
- Billions of cells in storage

**Reliability:**
- High availability (99.9% uptime)
- Auto-save functionality
- Version history

**User Experience:**
- Responsive design (mobile and desktop)
- Keyboard shortcuts
- Accessible interface (keyboard navigation, screen readers)

---

## 2) Component Hierarchy

The frontend is built as a React application with a clear component hierarchy. Here's how I'd structure it:

```
App
├── Layout
│   ├── Header
│   │   ├── SpreadsheetTitle (editable)
│   │   ├── CollaborationIndicator (shows active users)
│   │   └── UserMenu
│   ├── Toolbar
│   │   ├── FormatButtons (Bold, Italic, Underline, Colors)
│   │   ├── AlignmentButtons (Left, Center, Right)
│   │   ├── NumberFormatButtons (Currency, Percentage, Date)
│   │   ├── InsertButtons (Chart, Image, Link)
│   │   └── ActionButtons (Undo, Redo, Save)
│   ├── FormulaBar
│   │   ├── CellReference (shows active cell like "A1")
│   │   ├── FormulaInput (where user types formulas)
│   │   └── FunctionList (autocomplete for functions)
│   └── MainContent
│       ├── SheetTabs (multiple sheets in workbook)
│       └── SpreadsheetGrid
│           ├── RowHeaders (1, 2, 3...)
│           ├── ColumnHeaders (A, B, C...)
│           ├── Cell (Virtualized - only renders visible cells)
│           │   ├── CellValue (displays value or formula result)
│           │   ├── CellEditor (inline editing)
│           │   └── CellFormatting (applies styles)
│           ├── SelectionOverlay (highlights selected cells)
│           └── CursorIndicators (other users' cursors)
└── Sidebar (optional)
    ├── FormatPanel (detailed formatting options)
    ├── ChartPanel (chart creation/editing)
    └── CollaborationPanel (list of active users)
```

### Key Components Explained

**1. SpreadsheetGrid Component**
- Uses virtualization (react-window) to render only visible cells
- Handles cell selection (single cell or range)
- Manages keyboard navigation (arrow keys, Tab, Enter)
- Optimized with React.memo to prevent unnecessary re-renders

**2. Cell Component**
- Displays cell value or formula result
- Handles inline editing (double-click to edit)
- Applies formatting (styles, colors, borders)
- Shows formula errors if any

**3. FormulaBar Component**
- Shows active cell reference (e.g., "A1")
- Displays cell value or formula
- Allows formula editing with syntax highlighting
- Provides function autocomplete

**4. FormulaEngine (Business Logic)**
- Parses formulas into Abstract Syntax Tree (AST)
- Evaluates formulas with dependency tracking
- Detects circular references
- Recalculates dependent cells when dependencies change

**5. CollaborationManager**
- WebSocket connection for real-time updates
- Operational transformation for conflict resolution
- Presence tracking (who's viewing, cursor positions)
- Broadcasts cell changes to all connected clients

---

## 3) Data Models

Here are the key data structures I'd use:

```typescript
// Main spreadsheet structure
interface Spreadsheet {
  id: string;
  name: string;
  sheets: Sheet[];  // Multiple sheets in one workbook
  createdAt: string;
  updatedAt: string;
  ownerId: string;
  collaborators: Collaborator[];
}

// Individual sheet within a workbook
interface Sheet {
  id: string;
  name: string;  // "Sheet1", "Sheet2", etc.
  rows: number;
  columns: number;
  cells: Map<string, Cell>;  // Key: "A1", "B2", etc.
  frozenRows: number;  // Freeze panes feature
  frozenColumns: number;
}

// Individual cell
interface Cell {
  id: string;  // "A1", "B2", etc.
  row: number;
  column: number;
  value: string | number | null;  // Displayed value
  formula: string | null;  // Formula if any (e.g., "=SUM(A1:A10)")
  format: CellFormat;
  type: 'text' | 'number' | 'formula' | 'date';
  dependencies: string[];  // Cell IDs this cell depends on (for formulas)
  dependents: string[];  // Cell IDs that depend on this cell
}

// Cell formatting
interface CellFormat {
  bold: boolean;
  italic: boolean;
  underline: boolean;
  fontSize: number;
  fontFamily: string;
  textColor: string;
  backgroundColor: string;
  alignment: 'left' | 'center' | 'right';
  border: BorderStyle;
  numberFormat: 'general' | 'number' | 'currency' | 'percentage' | 'date';
}

// Formula representation
interface Formula {
  id: string;
  cellId: string;
  expression: string;  // "=SUM(A1:A10)"
  ast: ASTNode;  // Parsed Abstract Syntax Tree
  dependencies: string[];  // ["A1", "A2", ..., "A10"]
  result: any;  // Calculated result
  error: string | null;  // Error message if formula is invalid
}

// AST node for formula parsing
interface ASTNode {
  type: 'function' | 'reference' | 'literal' | 'operator';
  value: string;
  children: ASTNode[];
}

// Collaboration
interface Collaborator {
  userId: string;
  email: string;
  role: 'owner' | 'editor' | 'viewer';
  cursorPosition: CursorPosition | null;
}

interface CursorPosition {
  cellId: string;
  row: number;
  column: number;
  color: string;  // User's cursor color
}

// Update operation for real-time sync
interface SpreadsheetUpdate {
  type: 'cell_update' | 'cell_format' | 'formula_change' | 'sheet_add';
  cellId?: string;
  sheetId: string;
  data: any;
  timestamp: string;
  userId: string;
  version: number;  // For conflict resolution
}
```

### Data Flow Explanation

**When a user edits a cell:**
1. Cell value/formula is updated in the `Cell` object
2. If it's a formula, dependencies are calculated and stored
3. Dependent cells are identified and queued for recalculation
4. Update is broadcasted via WebSocket to other users
5. All clients update their local state

**Formula Dependency Graph:**
- If cell B1 has formula `=A1*2`, then B1 depends on A1
- When A1 changes, B1 needs to recalculate
- We maintain a dependency graph to track these relationships
- Circular references are detected using graph traversal

---

## 4) API Design

### REST Endpoints

**GET /api/v1/spreadsheets/:id**
- Fetch spreadsheet data
- Returns spreadsheet with all sheets and cells
- Response includes metadata (owner, collaborators, timestamps)

**PATCH /api/v1/spreadsheets/:id/cells**
- Update one or more cells
- Request body contains array of cell updates
- Returns updated cells and list of cells that need recalculation

**POST /api/v1/spreadsheets/:id/formulas/evaluate**
- Evaluate a formula (useful for validation)
- Takes formula string and cell context
- Returns result and dependencies

**POST /api/v1/spreadsheets/:id/export**
- Export spreadsheet to CSV/Excel
- Request specifies format and optional range
- Returns file download

**POST /api/v1/spreadsheets/:id/import**
- Import data from CSV/Excel file
- Uploads file via FormData
- Returns import summary (rows/columns imported)

### API Request/Response Examples

**Update Cell:**
```json
// PATCH /api/v1/spreadsheets/:id/cells
{
  "sheetId": "sheet_1",
  "updates": [
    {
      "cellId": "A1",
      "value": "Hello",
      "formula": null
    },
    {
      "cellId": "B1",
      "value": null,
      "formula": "=A1*2"
    }
  ]
}

// Response
{
  "success": true,
  "data": {
    "updatedCells": ["A1", "B1"],
    "recalculatedCells": ["B1"]  // B1 recalculated because it depends on A1
  }
}
```

**Get Spreadsheet:**
```json
// GET /api/v1/spreadsheets/:id
// Response
{
  "success": true,
  "data": {
    "id": "spreadsheet_123",
    "name": "My Spreadsheet",
    "sheets": [
      {
        "id": "sheet_1",
        "name": "Sheet1",
        "cells": {
          "A1": {
            "id": "A1",
            "row": 1,
            "column": 1,
            "value": "Hello",
            "formula": null,
            "format": { "bold": true, "fontSize": 12 }
          },
          "B1": {
            "id": "B1",
            "row": 1,
            "column": 2,
            "value": 20,
            "formula": "=A1*2",
            "format": {}
          }
        }
      }
    ]
  }
}
```

### WebSocket Protocol

**Connection:** `wss://api.example.com/spreadsheets/:id`

**Events:**
- `cell_update` - Cell value or formula changed
- `cell_format` - Cell formatting changed
- `presence_update` - User joined/left or cursor moved
- `conflict` - Conflict detected, requires resolution

**Message Format:**
```json
{
  "type": "cell_update",
  "data": {
    "cellId": "A1",
    "sheetId": "sheet_1",
    "value": "New Value",
    "userId": "user_123",
    "timestamp": "2024-01-15T12:00:00Z",
    "version": 5
  }
}
```

### Conflict Resolution Strategy

**Version-based approach:**
- Each update includes a version number
- Server maintains current version
- If client sends update with outdated version, server returns 409 Conflict
- Client must fetch latest version and retry

**Operational Transformation (OT):**
- For real-time collaboration, use OT to transform concurrent operations
- When two users edit simultaneously, operations are transformed to maintain consistency
- Example: User A inserts at position 5, User B inserts at position 3
  - Operations are transformed so both insertions are preserved correctly

---

## Key Design Decisions

**1. Virtualization for Performance**
- Only render visible cells (react-window)
- For 10K rows, we don't render all 10K cells at once
- Only render what's visible in viewport + small buffer

**2. Formula Dependency Graph**
- Maintain a graph of formula dependencies
- When a cell changes, only recalculate dependent cells
- Prevents unnecessary recalculations

**3. Optimistic Updates**
- Apply changes locally immediately (optimistic)
- Send to server in background
- If server rejects, rollback and show error

**4. WebSocket for Real-time**
- WebSocket connection per spreadsheet
- Broadcast changes to all connected clients
- Use operational transformation for conflict resolution

**5. Cell Storage Strategy**
- Store only non-empty cells (sparse storage)
- Don't store empty cells to save space
- Use Map data structure: key is cell ID ("A1"), value is Cell object

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with what the system needs to do - real-time collaboration, formulas, formatting

2. **Component Structure**: Explain the React component hierarchy - how the grid, cells, and formula bar work together

3. **Data Models**: Walk through the key data structures - Spreadsheet, Sheet, Cell, Formula - and how they relate

4. **API Design**: Show the REST endpoints and WebSocket protocol for real-time updates

5. **Key Challenges**: 
   - Formula dependency tracking and recalculation
   - Real-time conflict resolution
   - Performance with large spreadsheets (virtualization)
   - Circular reference detection

**Example explanation flow:**
> "So for a collaborative spreadsheet, I'd start with the requirements: we need real-time editing, formulas, and formatting. The frontend would be a React app with a virtualized grid component that only renders visible cells for performance. Each cell is a component that can display values or formula results. The data model centers around a Spreadsheet containing Sheets, which contain Cells. Cells can have formulas that depend on other cells, so we maintain a dependency graph. For real-time collaboration, we use WebSockets to broadcast changes, and operational transformation to resolve conflicts when multiple users edit simultaneously."

---

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Food Delivery System](14%29%20Food%20Delivery%20System.md) • [Next: Collaborative Word Processor →](16%29%20Collaborative%20Word%20Processor.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
