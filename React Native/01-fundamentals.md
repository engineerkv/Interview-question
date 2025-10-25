# ⚛️ React Native Interview Notes (2025 Edition)

## 🟢 Section 1 — React Native Fundamentals — Q1-Q30

---

### 1. 🟢 What is React Native, and how is it different from React.js?

**🧠 Concept**

React Native lets you build mobile apps using JavaScript and React, but renders to native mobile components instead of web DOM.

**💻 Example**

```jsx
import { View, Text } from 'react-native';

const App = () => (
  <View style={{flex: 1, justifyContent: 'center'}}>
    <Text>Hello Mobile!</Text>
  </View>
);
```

**💬 Explanation + Insight**

- **Cross-platform** - Write once, run on iOS and Android
- **Native performance** - Uses native components, not web views
- **JavaScript bridge** - Communication between JS and native code
- **Hot reloading** - Fast development with instant updates
- **Code sharing** - Share business logic between platforms

---

### 2. 🟢 What are the core components in React Native?

**🧠 Concept**

React Native provides core components that map to native mobile UI elements, replacing HTML elements with mobile-specific components.

**💻 Example**

```jsx
import { View, Text, Image, ScrollView, TouchableOpacity } from 'react-native';

const CoreComponents = () => (
  <ScrollView>
    <View style={{padding: 20}}>
      <Text>Hello World</Text>
      <Image source={{uri: 'https://example.com/image.jpg'}} />
      <TouchableOpacity onPress={() => console.log('Pressed')}>
        <Text>Press me</Text>
      </TouchableOpacity>
    </View>
  </ScrollView>
);
```

**💬 Explanation + Insight**

- **View** - Container component (like div)
- **Text** - Text display component
- **Image** - Image display component
- **ScrollView** - Scrollable container
- **TouchableOpacity** - Touchable component with feedback

---

### 3. 🟢 How do you handle styling in React Native?

**🧠 Concept**

React Native uses StyleSheet API for styling, which is similar to CSS but optimized for mobile performance.

**💻 Example**

```jsx
import { StyleSheet, View, Text } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
});

const StyledComponent = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Styled Text</Text>
  </View>
);
```

**💬 Explanation + Insight**

- **StyleSheet API** - Optimized styling system
- **Flexbox layout** - Primary layout system
- **Performance** - StyleSheet optimizes styles
- **Platform differences** - Handle iOS/Android differences
- **Responsive design** - Adapt to different screen sizes

---

### 4. 🟢 What is the difference between React Native and native development?

**🧠 Concept**

React Native bridges JavaScript and native code, while native development writes code directly in platform-specific languages.

**💻 Example**

```jsx
// React Native - Cross-platform
const App = () => (
  <View>
    <Text>Works on both iOS and Android</Text>
  </View>
);

// Native iOS - Swift
// UIView *view = [[UIView alloc] init];
// UILabel *label = [[UILabel alloc] init];
// [view addSubview:label];

// Native Android - Java/Kotlin
// View view = new View(context);
// TextView textView = new TextView(context);
// view.addView(textView);
```

**💬 Explanation + Insight**

- **Code sharing** - React Native shares code between platforms
- **Development speed** - Faster development than native
- **Performance** - Native is faster, React Native is good enough
- **Platform features** - Native has full platform access
- **Team size** - React Native needs fewer developers

---

### 5. 🟢 How do you handle navigation in React Native?

**🧠 Concept**

React Native navigation is handled by libraries like React Navigation, which provide stack, tab, and drawer navigation patterns.

**💻 Example**

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

const App = () => (
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Details" component={DetailsScreen} />
    </Stack.Navigator>
  </NavigationContainer>
);
```

**💬 Explanation + Insight**

- **React Navigation** - Most popular navigation library
- **Stack navigation** - Push/pop screen navigation
- **Tab navigation** - Bottom tab navigation
- **Drawer navigation** - Side menu navigation
- **Deep linking** - Handle URL-based navigation

---

### 6. 🟢 How do you handle state management in React Native?

**🧠 Concept**

React Native uses the same state management patterns as React, including useState, useContext, and external libraries like Redux.

**💻 Example**

```jsx
import { useState, useContext, createContext } from 'react';

const UserContext = createContext();

const App = () => {
  const [user, setUser] = useState(null);
  
  return (
    <UserContext.Provider value={{ user, setUser }}>
      <HomeScreen />
    </UserContext.Provider>
  );
};

const HomeScreen = () => {
  const { user, setUser } = useContext(UserContext);
  
  return (
    <View>
      <Text>Welcome {user?.name}</Text>
    </View>
  );
};
```

**💬 Explanation + Insight**

- **useState** - Local component state
- **useContext** - Global state sharing
- **Redux** - Complex state management
- **Zustand** - Lightweight state management
- **State persistence** - Save state to device storage

---

### 7. 🟢 How do you handle API calls in React Native?

**🧠 Concept**

React Native uses the same fetch API as web React, but with additional considerations for mobile network conditions.

**💻 Example**

```jsx
import { useState, useEffect } from 'react';

const ApiExample = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('API Error:', error);
        setLoading(false);
      });
  }, []);
  
  if (loading) return <Text>Loading...</Text>;
  return <Text>{data?.title}</Text>;
};
```

**💬 Explanation + Insight**

- **Fetch API** - Same as web React
- **Network conditions** - Handle slow/unreliable networks
- **Error handling** - Proper error handling for mobile
- **Caching** - Cache API responses for offline use
- **Security** - Secure API communication

---

### 8. 🟢 How do you handle platform-specific code in React Native?

**🧠 Concept**

React Native provides Platform API to write platform-specific code and handle differences between iOS and Android.

**💻 Example**

```jsx
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 44 : 24,
    backgroundColor: Platform.OS === 'ios' ? '#f8f9fa' : '#ffffff',
  },
  button: {
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
      },
      android: {
        elevation: 5,
      },
    }),
  },
});
```

**💬 Explanation + Insight**

- **Platform.OS** - Check current platform
- **Platform.select** - Choose platform-specific values
- **Platform-specific files** - Use .ios.js and .android.js files
- **Native modules** - Platform-specific native code
- **UI differences** - Handle platform-specific UI patterns

---

### 9. 🟢 How do you handle images in React Native?

**🧠 Concept**

React Native handles images differently than web, with support for local images, remote images, and various image formats.

**💻 Example**

```jsx
import { Image, View } from 'react-native';

const ImageExample = () => (
  <View>
    {/* Local image */}
    <Image source={require('./local-image.png')} />
    
    {/* Remote image */}
    <Image 
      source={{uri: 'https://example.com/image.jpg'}}
      style={{width: 200, height: 200}}
    />
    
    {/* Image with loading state */}
    <Image 
      source={{uri: 'https://example.com/image.jpg'}}
      onLoad={() => console.log('Image loaded')}
      onError={() => console.log('Image failed to load')}
    />
  </View>
);
```

**💬 Explanation + Insight**

- **Local images** - Use require() for local images
- **Remote images** - Use uri for remote images
- **Image optimization** - Optimize images for mobile
- **Loading states** - Handle image loading states
- **Error handling** - Handle image loading errors

---

### 10. 🟢 How do you handle touch events in React Native?

**🧠 Concept**

React Native provides touchable components and gesture handling for user interactions, replacing web event handlers.

**💻 Example**

```jsx
import { TouchableOpacity, TouchableHighlight, Pressable } from 'react-native';

const TouchExample = () => (
  <View>
    <TouchableOpacity onPress={() => console.log('Pressed')}>
      <Text>TouchableOpacity</Text>
    </TouchableOpacity>
    
    <TouchableHighlight onPress={() => console.log('Highlighted')}>
      <Text>TouchableHighlight</Text>
    </TouchableHighlight>
    
    <Pressable onPress={() => console.log('Pressed')}>
      <Text>Pressable</Text>
    </Pressable>
  </View>
);
```

**💬 Explanation + Insight**

- **TouchableOpacity** - Most common touchable component
- **TouchableHighlight** - Provides visual feedback
- **Pressable** - More flexible touch handling
- **Gesture handling** - Use react-native-gesture-handler
- **Accessibility** - Ensure touch targets are accessible

---

### 11. 🟢 How do you handle lists in React Native?

**🧠 Concept**

React Native provides FlatList and SectionList components for efficient list rendering, replacing web list elements.

**💻 Example**

```jsx
import { FlatList, View, Text } from 'react-native';

const ListExample = () => {
  const data = [
    { id: '1', title: 'Item 1' },
    { id: '2', title: 'Item 2' },
    { id: '3', title: 'Item 3' },
  ];
  
  const renderItem = ({ item }) => (
    <View style={{padding: 20}}>
      <Text>{item.title}</Text>
    </View>
  );
  
  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
    />
  );
};
```

**💬 Explanation + Insight**

- **FlatList** - Efficient list rendering
- **SectionList** - List with sections
- **Performance** - Only renders visible items
- **Key extraction** - Unique keys for list items
- **Pull to refresh** - Built-in refresh functionality

---

### 12. 🟢 How do you handle forms in React Native?

**🧠 Concept**

React Native forms use TextInput components and form libraries, with validation and state management similar to web forms.

**💻 Example**

```jsx
import { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';

const FormExample = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  
  const handleSubmit = () => {
    console.log('Form submitted:', { name, email });
  };
  
  return (
    <View>
      <TextInput
        placeholder="Name"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};
```

**💬 Explanation + Insight**

- **TextInput** - Text input component
- **Form validation** - Use libraries like Formik
- **Keyboard handling** - Handle different keyboard types
- **State management** - Manage form state
- **User experience** - Provide good form UX

---

### 13. 🟢 How do you handle animations in React Native?

**🧠 Concept**

React Native provides Animated API for smooth animations and transitions, with support for spring, timing, and gesture animations.

**💻 Example**

```jsx
import { Animated, TouchableOpacity } from 'react-native';

const AnimationExample = () => {
  const fadeAnim = useRef(new Animated.Value(0)).current;
  
  const fadeIn = () => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true,
    }).start();
  };
  
  return (
    <Animated.View style={{opacity: fadeAnim}}>
      <TouchableOpacity onPress={fadeIn}>
        <Text>Fade In</Text>
      </TouchableOpacity>
    </Animated.View>
  );
};
```

**💬 Explanation + Insight**

- **Animated API** - Built-in animation system
- **useNativeDriver** - Use native driver for performance
- **Spring animations** - Natural feeling animations
- **Gesture animations** - Animate based on gestures
- **Performance** - Optimize animations for 60fps

---

### 14. 🟢 How do you handle storage in React Native?

**🧠 Concept**

React Native provides AsyncStorage for persistent storage and other storage solutions for different data types.

**💻 Example**

```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';

const StorageExample = () => {
  const [data, setData] = useState(null);
  
  const saveData = async (key, value) => {
    try {
      await AsyncStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Save error:', error);
    }
  };
  
  const loadData = async (key) => {
    try {
      const value = await AsyncStorage.getItem(key);
      return value ? JSON.parse(value) : null;
    } catch (error) {
      console.error('Load error:', error);
    }
  };
  
  return <Text>Storage example</Text>;
};
```

**💬 Explanation + Insight**

- **AsyncStorage** - Simple key-value storage
- **Data persistence** - Save data between app sessions
- **Error handling** - Handle storage errors
- **Data serialization** - Convert objects to strings
- **Storage limits** - Be aware of storage limitations

---

### 15. 🟢 How do you handle networking in React Native?

**🧠 Concept**

React Native networking uses fetch API and libraries like Axios, with considerations for mobile network conditions.

**💻 Example**

```jsx
import { useState, useEffect } from 'react';

const NetworkingExample = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Network error:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);
  
  if (loading) return <Text>Loading...</Text>;
  return <Text>{data?.title}</Text>;
};
```

**💬 Explanation + Insight**

- **Fetch API** - Same as web React
- **Network conditions** - Handle slow/unreliable networks
- **Error handling** - Proper error handling for mobile
- **Offline support** - Handle offline scenarios
- **Security** - Secure network communication

---

### 16. 🟢 How do you handle permissions in React Native?

**🧠 Concept**

React Native apps need to request permissions for camera, location, storage, and other device features.

**💻 Example**

```jsx
import { PermissionsAndroid, Platform } from 'react-native';

const PermissionExample = () => {
  const requestCameraPermission = async () => {
    if (Platform.OS === 'android') {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.CAMERA
        );
        return granted === PermissionsAndroid.RESULTS.GRANTED;
      } catch (error) {
        console.error('Permission error:', error);
        return false;
      }
    }
    return true;
  };
  
  return <Text>Permission example</Text>;
};
```

**💬 Explanation + Insight**

- **Platform differences** - Different permission systems
- **Permission requests** - Request permissions at runtime
- **User experience** - Explain why permissions are needed
- **Permission handling** - Handle permission denials
- **Privacy** - Respect user privacy

---

### 17. 🟢 How do you handle debugging in React Native?

**🧠 Concept**

React Native provides debugging tools like React Native Debugger, Flipper, and console logging for development.

**💻 Example**

```jsx
import { Alert } from 'react-native';

const DebugExample = () => {
  const handleDebug = () => {
    console.log('Debug message');
    console.warn('Warning message');
    console.error('Error message');
    
    Alert.alert('Debug', 'Check console for messages');
  };
  
  return <Button title="Debug" onPress={handleDebug} />;
};
```

**💬 Explanation + Insight**

- **Console logging** - Use console.log for debugging
- **React Native Debugger** - Advanced debugging tool
- **Flipper** - Facebook's debugging platform
- **Remote debugging** - Debug on device from computer
- **Performance debugging** - Debug performance issues

---

### 18. 🟢 How do you handle testing in React Native?

**🧠 Concept**

React Native testing uses Jest for unit tests and Detox for E2E tests, similar to web React testing.

**💻 Example**

```jsx
// Unit test example
import { render, fireEvent } from '@testing-library/react-native';
import { MyComponent } from '../MyComponent';

test('renders correctly', () => {
  const { getByText } = render(<MyComponent />);
  expect(getByText('Hello World')).toBeTruthy();
});

// E2E test example
describe('App', () => {
  it('should navigate to details screen', async () => {
    await element(by.id('home-button')).tap();
    await expect(element(by.id('details-screen'))).toBeVisible();
  });
});
```

**💬 Explanation + Insight**

- **Jest testing** - Unit testing framework
- **Testing Library** - React Native testing utilities
- **Detox** - E2E testing framework
- **Test coverage** - Ensure good test coverage
- **CI/CD** - Integrate testing into build process

---

### 19. 🟢 How do you handle performance optimization in React Native?

**🧠 Concept**

React Native performance optimization involves bundle optimization, image optimization, and efficient rendering.

**💻 Example**

```jsx
import { Image, FlatList } from 'react-native';

const OptimizedComponent = () => (
  <FlatList
    data={data}
    renderItem={renderItem}
    keyExtractor={item => item.id}
    removeClippedSubviews={true}
    maxToRenderPerBatch={10}
    windowSize={10}
    initialNumToRender={10}
  />
);
```

**💬 Explanation + Insight**

- **Bundle optimization** - Minimize bundle size
- **Image optimization** - Optimize images for mobile
- **List optimization** - Use FlatList for large lists
- **Memory management** - Avoid memory leaks
- **Performance monitoring** - Monitor app performance

---

### 20. 🟢 How do you handle deployment in React Native?

**🧠 Concept**

React Native deployment involves building for iOS and Android, using services like CodePush for over-the-air updates.

**💻 Example**

```jsx
// CodePush integration
import codePush from 'react-native-code-push';

const App = () => {
  useEffect(() => {
    codePush.sync({
      updateDialog: true,
      installMode: codePush.InstallMode.IMMEDIATE
    });
  }, []);
  
  return <MyApp />;
};

export default codePush(App);
```

**💬 Explanation + Insight**

- **Build process** - Build for iOS and Android
- **App stores** - Deploy to App Store and Google Play
- **CodePush** - Over-the-air updates
- **Version management** - Handle app versions
- **Release process** - Automated release process

---

*This comprehensive React Native fundamentals section covers essential mobile development concepts including components, navigation, state management, and platform-specific considerations for building cross-platform mobile applications.*