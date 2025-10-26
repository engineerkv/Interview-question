# 🎨 HTML & CSS Interview Notes (2025 Edition)

## 🔵 Section 6 — UI Libraries: Material UI & Styled Components — Q111-Q125

---

### 111. 🔵 What is Material UI (MUI), and how is it structured?

**🧠 Concept**

Material UI is a React component library that implements Google's Material Design system, providing pre-built components with consistent styling and behavior.

**💻 Example**


```jsx
import { Button, Card, CardContent, Typography } from '@mui/material';

function App() {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" component="h2">
          Material UI Card
        </Typography>
        <Button variant="contained" color="primary">
          Click me
        </Button>
      </CardContent>
    </Card>
  );
}
```

**📝 Deeper Insight**

MUI provides a comprehensive set of components following Material Design principles, with built-in accessibility, theming, and responsive behavior. It's structured around components, theming, and styling systems.

---

## 112. How does the sx prop work in MUI?

**🧠 Concept**

The `sx` prop allows inline styling with access to the theme, providing a powerful way to style components with theme-aware values.

**💻 Example**


```jsx
import { Box, Button } from '@mui/material';

function Component() {
  return (
    <Box
      sx={{
        width: 300,
        height: 200,
        bgcolor: 'primary.main',
        color: 'white',
        p: 2,
        borderRadius: 1,
        '&:hover': {
          bgcolor: 'primary.dark',
        }
      }}
    >
      <Button
        sx={{
          mt: 2,
          px: 3,
          py: 1,
          fontSize: '1.2rem',
          textTransform: 'none',
        }}
      >
        Custom Button
      </Button>
    </Box>
  );
}
```

**📝 Deeper Insight**

The `sx` prop provides theme access, responsive values, and pseudo-selectors. It's more powerful than regular CSS-in-JS because it integrates with MUI's design system and theme.

---

## 113. How do you customize the MUI theme using createTheme()?

**🧠 Concept**

MUI themes are customized using `createTheme()` to override default values for colors, typography, spacing, and component styles.

**💻 Example**


```jsx
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
      light: '#42a5f5',
      dark: '#1565c0',
    },
    secondary: {
      main: '#dc004e',
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
    h1: {
      fontSize: '2.5rem',
      fontWeight: 600,
    },
  },
  spacing: 8, // 8px base unit
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      {/* Your app components */}
    </ThemeProvider>
  );
}
```

**📝 Deeper Insight**

Theme customization allows consistent branding across your application. The theme object can override any design token, and changes propagate to all components automatically.

---

## 114. What is ThemeProvider, and why is it required?

**🧠 Concept**

`ThemeProvider` makes the theme available to all MUI components in the component tree, enabling consistent styling and theme access.

**💻 Example**


```jsx
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { Button, Typography } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: { main: '#1976d2' },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Typography color="primary">
        This text uses the theme's primary color
      </Typography>
      <Button color="primary">
        This button uses the theme
      </Button>
    </ThemeProvider>
  );
}
```

**📝 Deeper Insight**

`ThemeProvider` is required because MUI components need access to the theme object for styling. Without it, components fall back to default values and lose theme integration.

---

## 115. How do you switch between light and dark themes in MUI?

**🧠 Concept**

MUI supports theme switching by creating separate light and dark themes and using state to toggle between them.

**💻 Example**


```jsx
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { CssBaseline, Switch, FormControlLabel } from '@mui/material';
import { useState } from 'react';

const lightTheme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#1976d2' },
  },
});

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: { main: '#90caf9' },
  },
});

function App() {
  const [darkMode, setDarkMode] = useState(false);
  
  return (
    <ThemeProvider theme={darkMode ? darkTheme : lightTheme}>
      <CssBaseline />
      <FormControlLabel
        control={
          <Switch
            checked={darkMode}
            onChange={(e) => setDarkMode(e.target.checked)}
          />
        }
        label="Dark Mode"
      />
    </ThemeProvider>
  );
}
```

**📝 Deeper Insight**

Theme switching requires creating separate theme objects and managing state. The `CssBaseline` component ensures consistent baseline styles across themes.

---

## 116. What are global overrides and CSS Baseline in MUI?

**🧠 Concept**

Global overrides customize component styles globally, while CSS Baseline provides consistent cross-browser styling and resets.

**💻 Example**


```jsx
import { createTheme } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';

const theme = createTheme({
  components: {
    // Global component overrides
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          borderRadius: 8,
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
        },
      },
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {/* All buttons will have no text transform and rounded corners */}
    </ThemeProvider>
  );
}
```

**📝 Deeper Insight**

Global overrides affect all instances of a component, while CSS Baseline ensures consistent styling across browsers. Use overrides sparingly to maintain component consistency.

---

## 117. How does MUI handle responsiveness and breakpoints?

**🧠 Concept**

MUI provides a responsive system with predefined breakpoints and utilities for creating responsive layouts and components.

**💻 Example**


```jsx
import { Box, Grid, useMediaQuery, useTheme } from '@mui/material';

function ResponsiveComponent() {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  
  return (
    <Box
      sx={{
        display: { xs: 'block', sm: 'flex' },
        flexDirection: { xs: 'column', md: 'row' },
        gap: { xs: 2, md: 4 },
      }}
    >
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6} md={4}>
          <Box>Responsive Grid Item</Box>
        </Grid>
      </Grid>
    </Box>
  );
}
```

**📝 Deeper Insight**

MUI's responsive system uses breakpoints (xs, sm, md, lg, xl) and provides utilities like `useMediaQuery` and responsive props in the `sx` prop for flexible layouts.

---

## 118. How does Styled Components work under the hood?

**🧠 Concept**

Styled Components uses tagged template literals to create styled React components, generating unique class names and injecting CSS dynamically.

**💻 Example**


```jsx
import styled from 'styled-components';

const StyledButton = styled.button`
  background-color: ${props => props.primary ? '#007bff' : '#6c757d'};
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  
  &:hover {
    opacity: 0.8;
  }
`;

// Usage
<StyledButton primary>Primary Button</StyledButton>
<StyledButton>Secondary Button</StyledButton>
```

**📝 Deeper Insight**

Styled Components generates unique class names, injects CSS into the DOM, and provides props-based styling. It uses CSS-in-JS with template literals for component styling.

---

## 119. What are the pros and cons of Styled Components vs CSS Modules?

**🧠 Concept**

Styled Components offers dynamic styling and component co-location, while CSS Modules provides better performance and simpler mental model.

**💻 Example**


```jsx
// Styled Components
const Button = styled.button`
  background: ${props => props.variant === 'primary' ? 'blue' : 'gray'};
  padding: 10px 20px;
`;

// CSS Modules
import styles from './Button.module.css';

function Button({ variant }) {
  return (
    <button className={`${styles.button} ${styles[variant]}`}>
      Click me
    </button>
  );
}
```

```css
/* Button.module.css */
.button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
}

.primary {
  background: blue;
  color: white;
}

.secondary {
  background: gray;
  color: white;
}
```

**📝 Deeper Insight**

Styled Components excel at dynamic styling and component co-location, while CSS Modules offer better performance, simpler debugging, and easier migration from existing CSS.

---

## 120. How do props work inside styled components?

**🧠 Concept**

Props are passed to styled components and can be used in template literals to create dynamic styles based on component state or props.

**💻 Example**


```jsx
const StyledCard = styled.div`
  background-color: ${props => props.bgColor || '#ffffff'};
  padding: ${props => props.padding || '16px'};
  border-radius: ${props => props.rounded ? '8px' : '0'};
  box-shadow: ${props => props.shadow ? '0 2px 4px rgba(0,0,0,0.1)' : 'none'};
  
  ${props => props.hover && `
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
  `}
`;

// Usage with different props
<StyledCard bgColor="#f0f0f0" padding="24px" rounded hover>
  Card content
</StyledCard>
```

**📝 Deeper Insight**

Props enable dynamic styling in styled components. Use conditional logic, default values, and complex expressions to create flexible, reusable styled components.

---

## 121. How do you create global styles in Styled Components?

**🧠 Concept**

Global styles in Styled Components are created using `createGlobalStyle` to inject CSS that affects the entire application.

**💻 Example**


```jsx
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    color: #333;
  }
  
  h1, h2, h3 {
    font-weight: 600;
    margin-bottom: 1rem;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }
`;

function App() {
  return (
    <>
      <GlobalStyle />
      {/* Your app components */}
    </>
  );
}
```

**📝 Deeper Insight**

`createGlobalStyle` is used for CSS resets, typography, and global layout styles. It's rendered once and affects the entire application.

---

## 122. How do you use attrs() in Styled Components?

**🧠 Concept**

`attrs()` allows setting default HTML attributes or props for styled components, providing a way to configure the underlying element.

**💻 Example**


```jsx
const StyledInput = styled.input.attrs(props => ({
  type: props.type || 'text',
  placeholder: props.placeholder || 'Enter text',
  disabled: props.disabled || false,
}))`
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  
  &:focus {
    outline: none;
    border-color: #007bff;
  }
  
  &:disabled {
    background-color: #f5f5f5;
    cursor: not-allowed;
  }
`;

// Usage
<StyledInput type="email" placeholder="Enter email" />
<StyledInput type="password" placeholder="Enter password" />
<StyledInput disabled />
```

**📝 Deeper Insight**

`attrs()` is useful for setting default attributes, handling different input types, and configuring the underlying HTML element without cluttering the component usage.

---

## 123. What are keyframes in Styled Components?

**🧠 Concept**

Keyframes in Styled Components are created using the `keyframes` helper to define CSS animations that can be used in styled components.

**💻 Example**


```jsx
import styled, { keyframes } from 'styled-components';

const fadeIn = keyframes`
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
`;

const bounce = keyframes`
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
`;

const AnimatedDiv = styled.div`
  animation: ${fadeIn} 0.5s ease-in-out;
`;

const BouncingButton = styled.button`
  animation: ${bounce} 2s infinite;
  padding: 10px 20px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
`;
```

**📝 Deeper Insight**

Keyframes in Styled Components work like regular CSS keyframes but are JavaScript functions. They can be reused across multiple styled components and accept props for dynamic animations.

---

## 124. How do you combine Styled Components with Tailwind or MUI?

**🧠 Concept**

Styled Components can be combined with other styling solutions by using them selectively for specific components while maintaining the overall design system.

**💻 Example**


```jsx
// Combining with Tailwind
import styled from 'styled-components';

const CustomCard = styled.div`
  /* Tailwind classes for base styling */
  @apply bg-white rounded-lg shadow-md p-6;
  
  /* Custom styled-components logic */
  background-color: ${props => props.theme.colors.primary};
  transform: ${props => props.hover ? 'translateY(-2px)' : 'translateY(0)'};
  transition: transform 0.2s ease;
`;

// Combining with MUI
import { styled } from '@mui/material/styles';
import { Button } from '@mui/material';

const StyledButton = styled(Button)`
  background: linear-gradient(45deg, #fe6b8b 30%, #ff8e53 90%);
  border: 0;
  border-radius: 3;
  box-shadow: 0 3px 5px 2px rgba(255, 105, 135, .3);
  color: white;
  height: 48;
  padding: 0 30px;
`;
```

**📝 Deeper Insight**

Combining styling solutions requires careful planning to avoid conflicts. Use each tool for its strengths: design systems for consistency, styled-components for dynamic styling.

---

## 125. What are the performance implications of CSS-in-JS?

**🧠 Concept**

CSS-in-JS has runtime overhead due to style generation, but modern solutions like Styled Components v5+ and Emotion provide optimizations to minimize performance impact.

**💻 Example**


```jsx
// Performance considerations
const OptimizedComponent = styled.div`
  /* Avoid complex calculations in render */
  background-color: ${props => props.theme.colors.primary};
  
  /* Use CSS custom properties for dynamic values */
  --dynamic-color: ${props => props.color};
  color: var(--dynamic-color);
`;

// Better performance with static styles
const StaticComponent = styled.div`
  background-color: #007bff;
  color: white;
  padding: 16px;
`;

// Use shouldForwardProp to prevent unnecessary re-renders
const FilteredComponent = styled.div.withConfig({
  shouldForwardProp: (prop) => !['color', 'size'].includes(prop),
})`
  background-color: ${props => props.color};
  font-size: ${props => props.size}px;
`;
```

**📝 Deeper Insight**

CSS-in-JS performance depends on implementation. Modern solutions use CSS custom properties, avoid runtime calculations, and provide optimizations like style caching and prop filtering.
