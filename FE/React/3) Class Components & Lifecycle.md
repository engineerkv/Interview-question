# 🔄 3. Class Components & Lifecycle (Q29–30)

---

## 🧩 Q29. What are the main lifecycle methods in class components?

### 🧠 Concept

Class components have lifecycle methods for mounting (componentDidMount), updating (componentDidUpdate), and unmounting (componentWillUnmount). These methods let you run code at specific points in a component's life.

---

### 💡 Example

```jsx
class UserProfile extends React.Component {
  componentDidMount() {
    fetch('/api/user')
      .then(r => r.json())
      .then(user => this.setState({ user, loading: false }));
  }
  componentWillUnmount() {
    // cleanup
  }
  render() {
    return this.state.loading ? null : <div>{this.state.user.name}</div>;
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Lifecycle phases are mounting (create), updating (change), unmounting (destroy).
* **Use Case:** componentDidMount for API calls, componentWillUnmount for cleanup.
* **Common Mistake:** Forgetting to clean up subscriptions or timers in componentWillUnmount.
* **Pro Tip:** Use shouldComponentUpdate to prevent unnecessary re-renders.

---

### ⭐ Senior Takeaway

Lifecycle methods are being replaced by hooks in modern React—prefer functional components.

---

## 🧩 Q30. How do you convert class components to functional components with hooks?

### 🧠 Concept

useEffect replaces lifecycle methods: empty array equals componentDidMount, dependencies equal componentDidUpdate, cleanup return equals componentWillUnmount. One hook handles all lifecycle needs.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** useEffect([]) equals mount, useEffect([deps]) equals update, return function equals unmount.
* **Use Case:** One hook handles all lifecycle needs, more flexible than class methods.
* **Common Mistake:** Trying to replicate exact lifecycle behavior—hooks work differently.
* **Pro Tip:** Multiple useEffect hooks separate concerns better than one lifecycle method.

---

### ⭐ Senior Takeaway

Hooks unify lifecycle management, making code more maintainable and testable.

---
