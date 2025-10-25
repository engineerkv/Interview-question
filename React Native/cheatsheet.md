# 📱 React Native Cheatsheet - Interview Quick Reference

## 🚀 Quick Reference Guide

### 📱 React Native Fundamentals
- **Cross-platform**: Write once, run on iOS and Android
- **Native Performance**: Uses native components, not web views
- **JavaScript Bridge**: Communication between JS and native code
- **Hot Reloading**: Fast development with instant updates

### 🤖 Android & iOS Platform
- **Platform Differences**: iOS vs Android specific behaviors
- **Navigation**: React Navigation for cross-platform navigation
- **Platform APIs**: Camera, GPS, push notifications
- **App Store**: Deployment and distribution strategies

### 🔧 Native Modules & SDK
- **Native Modules**: Bridge between JS and native code
- **Third-party Libraries**: Expo, React Native CLI
- **Platform-specific Code**: iOS/Android specific implementations
- **SDK Integration**: Firebase, analytics, crash reporting

### ⚡ Performance Optimization
- **Bundle Size**: Code splitting, tree shaking, lazy loading
- **Memory Management**: Image optimization, list virtualization
- **Rendering**: FlatList, SectionList for large datasets
- **Native Performance**: Use native components when possible

### 🔒 Security & Stability
- **Code Obfuscation**: Protect JavaScript code
- **Certificate Pinning**: Secure API communications
- **Crash Reporting**: Sentry, Crashlytics integration
- **Error Boundaries**: Graceful error handling

### 🧪 Testing & Automation
- **Unit Testing**: Jest for JavaScript testing
- **Integration Testing**: Detox for E2E testing
- **CI/CD**: Automated testing and deployment
- **Device Testing**: Real device vs simulator testing

## 🎯 Common Patterns

### Navigation Setup
```javascript
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};
```

### State Management
```javascript
import { createContext, useContext, useReducer } from 'react';

const AppContext = createContext();

const appReducer = (state, action) => {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    default:
      return state;
  }
};

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, {
    user: null,
    loading: false,
  });

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};
```

### API Integration
```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

class ApiService {
  constructor() {
    this.baseURL = 'https://api.example.com';
  }

  async getAuthToken() {
    return await AsyncStorage.getItem('authToken');
  }

  async makeRequest(endpoint, options = {}) {
    const token = await this.getAuthToken();
    
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        ...options.headers,
      },
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`);
    }

    return response.json();
  }
}
```

### Platform-specific Code
```javascript
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

// Platform-specific components
const CustomButton = ({ children, onPress }) => {
  if (Platform.OS === 'ios') {
    return <IOSButton onPress={onPress}>{children}</IOSButton>;
  }
  return <AndroidButton onPress={onPress}>{children}</AndroidButton>;
};
```

### Performance Optimization
```javascript
import { FlatList, useMemo } from 'react-native';

const OptimizedList = ({ data, renderItem }) => {
  const memoizedData = useMemo(() => data, [data]);
  
  const keyExtractor = (item) => item.id.toString();
  
  const getItemLayout = (data, index) => ({
    length: 80,
    offset: 80 * index,
    index,
  });

  return (
    <FlatList
      data={memoizedData}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      getItemLayout={getItemLayout}
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      windowSize={10}
      initialNumToRender={10}
    />
  );
};
```

### Image Optimization
```javascript
import { Image } from 'react-native';

const OptimizedImage = ({ source, style, ...props }) => {
  return (
    <Image
      source={source}
      style={style}
      resizeMode="cover"
      loadingIndicatorSource={require('./placeholder.png')}
      {...props}
    />
  );
};

// Lazy loading images
const LazyImage = ({ uri, style }) => {
  const [loaded, setLoaded] = useState(false);
  
  return (
    <View style={style}>
      {!loaded && <ActivityIndicator />}
      <Image
        source={{ uri }}
        style={[style, { opacity: loaded ? 1 : 0 }]}
        onLoad={() => setLoaded(true)}
      />
    </View>
  );
};
```

## 📊 React Native Components

### Core Components
| Component | Description | Props |
|-----------|-------------|-------|
| `View` | Container component | style, children |
| `Text` | Text display | style, numberOfLines |
| `Image` | Image display | source, style, resizeMode |
| `ScrollView` | Scrollable container | contentContainerStyle |
| `FlatList` | Optimized list | data, renderItem, keyExtractor |
| `TouchableOpacity` | Touchable component | onPress, style |

### Navigation Components
| Component | Description | Usage |
|-----------|-------------|-------|
| `NavigationContainer` | Navigation wrapper | Root navigation |
| `Stack.Navigator` | Stack navigation | Screen navigation |
| `Tab.Navigator` | Tab navigation | Bottom tabs |
| `Drawer.Navigator` | Drawer navigation | Side menu |

### Platform APIs
| API | Description | Usage |
|-----|-------------|-------|
| `Camera` | Camera access | Photo/video capture |
| `Location` | GPS location | Maps, tracking |
| `PushNotification` | Push notifications | User engagement |
| `AsyncStorage` | Local storage | Data persistence |

## 🚀 Development Tools

### Debugging
```javascript
// React Native Debugger
import { Debugger } from 'react-native-debugger';

// Flipper integration
import { Flipper } from 'react-native-flipper';

// Console logging
console.log('Debug info:', data);
console.warn('Warning:', message);
console.error('Error:', error);
```

### Testing
```javascript
// Jest unit tests
import { render, fireEvent } from '@testing-library/react-native';
import { MyComponent } from '../MyComponent';

test('renders correctly', () => {
  const { getByText } = render(<MyComponent />);
  expect(getByText('Hello World')).toBeTruthy();
});

// Detox E2E tests
describe('App', () => {
  it('should navigate to details screen', async () => {
    await element(by.id('home-button')).tap();
    await expect(element(by.id('details-screen'))).toBeVisible();
  });
});
```

### Performance Monitoring
```javascript
// Performance monitoring
import { Performance } from 'react-native-performance';

const trackScreenTime = (screenName) => {
  const startTime = Performance.now();
  
  return () => {
    const endTime = Performance.now();
    console.log(`${screenName} took ${endTime - startTime}ms`);
  };
};

// Memory usage
import { getMemoryInfo } from 'react-native-memory-info';

const checkMemoryUsage = () => {
  const memoryInfo = getMemoryInfo();
  console.log('Memory usage:', memoryInfo);
};
```

## 🎨 Styling Patterns

### StyleSheet Usage
```javascript
import { StyleSheet } from 'react-native';

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
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#007bff',
    padding: 12,
    borderRadius: 6,
    alignItems: 'center',
  },
});
```

### Responsive Design
```javascript
import { Dimensions } from 'react-native';

const { width, height } = Dimensions.get('window');

const responsiveStyles = StyleSheet.create({
  container: {
    width: width * 0.9,
    height: height * 0.8,
  },
  text: {
    fontSize: width < 400 ? 14 : 16,
  },
});
```

## 🚀 Interview Tips

### Common Questions
1. **React Native vs React**: Differences in rendering and components
2. **Performance**: How to optimize React Native apps
3. **Navigation**: Different navigation patterns and libraries
4. **Platform Differences**: iOS vs Android specific considerations
5. **Testing**: Unit, integration, and E2E testing strategies

### Best Practices
1. **Component Architecture**: Keep components small and focused
2. **State Management**: Use appropriate state management solution
3. **Performance**: Optimize images, lists, and animations
4. **Error Handling**: Implement proper error boundaries
5. **Accessibility**: Ensure apps are accessible to all users

---

*This cheatsheet covers essential React Native concepts for interview preparation, including platform differences, performance optimization, and development best practices.*
