# 🔄 3. Class Components & Lifecycle (Q28–29)

---

## 28) What are the main lifecycle methods in class components?

Class components have lifecycle methods: mounting (componentDidMount), updating (componentDidUpdate), and unmounting (componentWillUnmount).

```jsx
class UserProfile extends React.Component {
  componentDidMount() {
    fetch('/api/user').then(r => r.json()).then(user => this.setState({ user, loading: false }));
  }
  componentWillUnmount() { /* cleanup */ }
  render() { return this.state.loading ? null : <div>{this.state.user.name}</div>; }
}
```

- **Lifecycle Phases**: Mounting (create), updating (change), unmounting (destroy)
- **Real-World Use**: componentDidMount for API calls, componentWillUnmount for cleanup
- **Common Mistake**: Forgetting to clean up subscriptions or timers in componentWillUnmount
- **Optimization**: Use shouldComponentUpdate to prevent unnecessary re-renders
- **Interview Tip**: Explain that lifecycle methods are being replaced by hooks in modern React

---

## 29) What are the Hook equivalents of class lifecycle methods?

useEffect replaces lifecycle methods: empty array = componentDidMount, dependencies = componentDidUpdate, cleanup = componentWillUnmount.

```jsx
function HookComponent() {
  useEffect(() => {
    console.log('Component mounted');
    fetchData();
    return () => console.log('Cleanup');
  }, []);
  return <div />;
}
```

- **Core Mapping**: useEffect([]) = mount, useEffect([deps]) = update, return function = unmount
- **Real-World Benefit**: One hook handles all lifecycle needs, more flexible than class methods
- **Common Mistake**: Trying to replicate exact lifecycle behavior - hooks work differently
- **Optimization**: Multiple useEffect hooks separate concerns better than one lifecycle method
- **Interview Tip**: Explain that hooks unify lifecycle management, making code more maintainable

---
