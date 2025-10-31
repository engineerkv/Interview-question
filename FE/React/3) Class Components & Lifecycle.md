# 🔄 3. Class Components & Lifecycle (Q28–29)

---

## 28) What are the main lifecycle methods in class components?

Concept:
Class lifecycles include: constructor, render, componentDidMount, shouldComponentUpdate, getSnapshotBeforeUpdate, componentDidUpdate, componentWillUnmount, static getDerivedStateFromProps, static getDerivedStateFromError, and componentDidCatch.

Example:
```jsx
class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null, loading: true };
  }
  componentDidMount() {
    fetch('/api/user').then(r => r.json()).then(user => this.setState({ user, loading: false }));
  }
  shouldComponentUpdate(nextProps, nextState) { return nextState.user !== this.state.user; }
  getSnapshotBeforeUpdate(prevProps, prevState) { return window.scrollY; }
  componentDidUpdate(prevProps, prevState, snapshot) { if (snapshot > 0) window.scrollTo(0, snapshot); }
  componentWillUnmount() { /* cleanup */ }
  render() { return this.state.loading ? null : <div>{this.state.user.name}</div>; }
}
```

Deep Insight:
- **Mounting**: constructor → render → componentDidMount (fetch/subscribe)
- **Updating**: shouldComponentUpdate → render → getSnapshotBeforeUpdate → componentDidUpdate
- **Unmounting**: componentWillUnmount (cleanup timers, events, abort requests)
- **Derivations**: static getDerivedStateFromProps, static getDerivedStateFromError
- **Errors**: componentDidCatch for boundaries (log and show fallback)

---

## 29) What are the Hook equivalents of class lifecycle methods?

Concept:
useEffect with empty dependency array replaces componentDidMount, useEffect with dependencies replaces componentDidUpdate, and cleanup functions replace componentWillUnmount.

Example:
```jsx
// Class Component Lifecycle
class ClassComponent extends React.Component {
  componentDidMount() {
    console.log('Component mounted');
    this.fetchData();
  }
  componentWillUnmount() { console.log('Cleanup'); }
  render() { return <div />; }
}

// Hook Equivalents
function HookComponent() {
  useEffect(() => {
    console.log('Component mounted');
    fetchData();
    return () => console.log('Cleanup');
  }, []);
  return <div />;
}
```

Deep Insight:
- **useEffect**: Single hook replaces multiple lifecycle methods
- **Dependency Array**: Controls when effect runs (mount, update, unmount)
- **Cleanup Function**: Return function from useEffect for cleanup
- **Multiple Effects**: Can have multiple useEffect hooks for different concerns
- **Simpler Logic**: Hooks provide cleaner, more composable lifecycle management

---
