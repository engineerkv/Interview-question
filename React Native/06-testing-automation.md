# ⚛️ React Native Interview Notes (2025 Edition)

## 🧪 Section 6 — Testing, Automation & CI/CD — Q126-Q140

---

## **Q126. What are the different types of testing in React Native?**

**🧠 Concept**

React Native testing includes unit tests, integration tests, and end-to-end tests to ensure app quality and reliability.

**💻 Example**
```javascript
// Unit test
describe('MyComponent', () => {
  test('renders correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });
});

// Integration test
test('user can login', async () => {
  render(<LoginScreen />);
  fireEvent.changeText(screen.getByPlaceholderText('Email'), 'user@test.com');
  fireEvent.press(screen.getByText('Login'));
  await waitFor(() => expect(screen.getByText('Welcome')).toBeInTheDocument());
});
```

**💬 Explanation + Insight**

- Unit tests: Test individual components and functions
- Integration tests: Test component interactions
- E2E tests: Test complete user workflows
- Coverage: Aim for high test coverage
- Quality: Ensures app quality and reliability

---

## **Q127. How do you set up Jest for React Native testing?**

**🧠 Concept**

Jest is set up by configuring the test environment, adding test scripts, and configuring mocks for React Native components.

**💻 Example**
```javascript
// jest.config.js
module.exports = {
  preset: 'react-native',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  transformIgnorePatterns: [
    'node_modules/(?!(react-native|@react-native|react-native-.*)/)',
  ],
  testMatch: ['**/__tests__/**/*.(js|jsx|ts|tsx)'],
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
  ],
};
```

**💬 Explanation + Insight**

- Configuration: Configure Jest for React Native
- Setup files: Use setup files for global configuration
- Transform: Configure file transformations
- Coverage: Set up test coverage reporting
- Performance: Optimize test performance

---

## **Q128. How do you use React Native Testing Library?**

**🧠 Concept**

React Native Testing Library provides utilities for testing React Native components with a focus on user behavior and accessibility.

**💻 Example**
```javascript
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

test('user can interact with component', async () => {
  const { getByText, getByPlaceholderText } = render(<MyComponent />);
  
  fireEvent.changeText(getByPlaceholderText('Enter text'), 'Hello');
  fireEvent.press(getByText('Submit'));
  
  await waitFor(() => {
    expect(getByText('Success')).toBeInTheDocument();
  });
});
```

**💬 Explanation + Insight**

- User-focused: Tests from user perspective
- Accessibility: Tests accessibility features
- Queries: Use semantic queries
- Events: Simulate user interactions
- Async: Handle async operations

---

## **Q129. How do you mock native modules in React Native tests?**

**🧠 Concept**

Native modules are mocked by creating mock implementations that simulate native functionality in JavaScript tests.

**💻 Example**
```javascript
// __mocks__/react-native-keychain.js
export default {
  setInternetCredentials: jest.fn(() => Promise.resolve()),
  getInternetCredentials: jest.fn(() => Promise.resolve({ username: 'test', password: 'test' })),
  resetInternetCredentials: jest.fn(() => Promise.resolve()),
};

// In test file
jest.mock('react-native-keychain', () => require('../__mocks__/react-native-keychain'));
```

**💬 Explanation + Insight**

- Mock files: Create mock files for native modules
- Jest mocks: Use Jest mocking capabilities
- Promises: Mock async operations
- Functionality: Simulate native functionality
- Testing: Test JavaScript logic without native dependencies

---

## **Q130. How do you set up Detox for E2E testing?**

**🧠 Concept**

Detox is set up by configuring the test environment, creating test files, and running tests on simulators or devices.

**💻 Example**
```javascript
// .detoxrc.js
module.exports = {
  testRunner: 'jest',
  runnerConfig: 'e2e/config.json',
  configurations: {
    'ios.sim.debug': {
      binaryPath: 'ios/build/Build/Products/Debug-iphonesimulator/MyApp.app',
      build: 'xcodebuild -workspace ios/MyApp.xcworkspace -scheme MyApp -configuration Debug -sdk iphonesimulator -derivedDataPath ios/build',
      type: 'ios.simulator',
      device: {
        type: 'iPhone 14',
      },
    },
  },
};
```

**💬 Explanation + Insight**

- Configuration: Configure Detox for your app
- Test files: Create E2E test files
- Simulators: Test on iOS and Android simulators
- Devices: Test on real devices
- CI/CD: Integrate with CI/CD pipelines

---

## **Q131. How do you write Detox E2E tests?**

**🧠 Concept**

Detox E2E tests are written using Detox's API to simulate user interactions and verify app behavior.

**💻 Example**
```javascript
describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  beforeEach(async () => {
    await device.reloadReactNative();
  });

  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@test.com');
    await element(by.id('password-input')).typeText('password123');
    await element(by.id('login-button')).tap();
    
    await expect(element(by.text('Welcome'))).toBeVisible();
  });
});
```

**💬 Explanation + Insight**

- User interactions: Simulate real user interactions
- Element selection: Use element selectors
- Assertions: Verify expected behavior
- Setup: Proper test setup and teardown
- Reliability: Write reliable E2E tests

---

## **Q132. How do you implement snapshot testing in React Native?**

**🧠 Concept**

Snapshot testing captures component output and compares it with stored snapshots to detect unexpected changes.

**💻 Example**
```javascript
import React from 'react';
import { render } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

test('renders correctly', () => {
  const tree = render(<MyComponent />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

**💬 Explanation + Insight**

- Component output: Capture component rendering output
- Change detection: Detect unexpected changes
- Maintenance: Update snapshots when needed
- Coverage: Test component rendering
- Regression: Prevent regression bugs

---

## **Q133. How do you measure test coverage in React Native?**

**🧠 Concept**

Test coverage is measured using Jest's coverage reporting to identify untested code and improve test quality.

**💻 Example**
```javascript
// package.json
{
  "scripts": {
    "test": "jest",
    "test:coverage": "jest --coverage"
  }
}

// jest.config.js
module.exports = {
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.stories.{js,jsx,ts,tsx}',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

**💬 Explanation + Insight**

- Coverage reporting: Generate coverage reports
- Thresholds: Set coverage thresholds
- Quality: Improve test quality
- Gaps: Identify untested code
- Metrics: Track coverage metrics

---

## **Q134. How do you set up GitHub Actions for React Native CI/CD?**

**🧠 Concept**

GitHub Actions are set up by creating workflow files that automate building, testing, and deploying React Native apps.

**💻 Example**
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test
      - run: npm run test:coverage
```

**💬 Explanation + Insight**

- Workflow files: Create GitHub Actions workflows
- Triggers: Set up workflow triggers
- Steps: Define workflow steps
- Testing: Automate testing
- Deployment: Automate deployment

---

## **Q135. How do you set up CircleCI for React Native CI/CD?**

**🧠 Concept**

CircleCI is set up by creating configuration files that define build, test, and deployment pipelines for React Native apps.

**💻 Example**
```yaml
# .circleci/config.yml
version: 2.1

jobs:
  test:
    docker:
      - image: cimg/node:18.0
    steps:
      - checkout
      - run: npm install
      - run: npm test
      - run: npm run test:coverage

  build:
    docker:
      - image: cimg/android:2023.09.1
    steps:
      - checkout
      - run: npm install
      - run: cd android && ./gradlew assembleRelease
```

**💬 Explanation + Insight**

- Configuration: Create CircleCI configuration
- Jobs: Define build and test jobs
- Docker: Use Docker for consistent environments
- Automation: Automate build and test processes
- Deployment: Set up deployment pipelines

---

## **Q136. How do you set up Bitrise for React Native CI/CD?**

**🧠 Concept**

Bitrise is set up by creating workflow configurations that automate building, testing, and deploying React Native apps.

**💻 Example**
```yaml
# bitrise.yml
format_version: '11'
default_step_lib_source: https://github.com/bitrise-io/bitrise-steplib.git

workflows:
  test:
    steps:
      - activate-ssh-key@4:
          run_if: '{{getenv "SSH_RSA_PRIVATE_KEY" | ne ""}}'
      - git-clone@6: {}
      - npm@3:
          inputs:
            - command: install
      - npm@3:
          inputs:
            - command: test
```

**💬 Explanation + Insight**

- Workflow configuration: Create Bitrise workflows
- Steps: Define workflow steps
- Automation: Automate build processes
- Testing: Integrate testing
- Deployment: Set up deployment

---

## **Q137. How do you use EAS Build for React Native?**

**🧠 Concept**

EAS Build is used to build React Native apps in the cloud with proper configuration and build profiles.

**💻 Example**
```json
// eas.json
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {
      "distribution": "store"
    }
  }
}
```

**💬 Explanation + Insight**

- Cloud building: Build apps in the cloud
- Configuration: Configure build profiles
- Distribution: Set up distribution methods
- Automation: Automate build processes
- Scaling: Scale build processes

---

## **Q138. How do you configure build variants in React Native?**

**🧠 Concept**

Build variants are configured by setting up different build configurations for development, staging, and production environments.

**💻 Example**
```javascript
// android/app/build.gradle
android {
    buildTypes {
        debug {
            applicationIdSuffix ".debug"
            versionNameSuffix "-debug"
            buildConfigField "String", "API_URL", '"https://api-dev.example.com"'
        }
        release {
            buildConfigField "String", "API_URL", '"https://api.example.com"'
        }
    }
}
```

**💬 Explanation + Insight**

- Build types: Configure different build types
- Environment variables: Set environment-specific variables
- Configuration: Configure build settings
- Automation: Automate build processes
- Deployment: Set up deployment strategies

---

## **Q139. How do you automate signing in React Native?**

**🧠 Concept**

Signing is automated by configuring certificates, provisioning profiles, and using CI/CD tools to handle the signing process.

**💻 Example**
```yaml
# GitHub Actions workflow
- name: Setup iOS signing
  uses: apple-actions/setup-xcode@v1
  with:
    xcode-version: '14.0'

- name: Import certificates
  run: |
    echo "${{ secrets.CERTIFICATE_BASE64 }}" | base64 --decode > certificate.p12
    security create-keychain -p "" build.keychain
    security default-keychain -s build.keychain
    security unlock-keychain -p "" build.keychain
    security import certificate.p12 -k build.keychain -P "${{ secrets.CERTIFICATE_PASSWORD }}" -T /usr/bin/codesign
```

**💬 Explanation + Insight**

- Certificates: Configure certificates
- Provisioning: Set up provisioning profiles
- Automation: Automate signing process
- Security: Secure certificate handling
- CI/CD: Integrate with CI/CD pipelines

---

## **Q140. How do you configure environment configs in React Native?**

**🧠 Concept**

Environment configs are configured by using different configuration files and environment variables for different environments.

**💻 Example**
```javascript
// config/development.js
export default {
  API_URL: 'https://api-dev.example.com',
  DEBUG: true,
  LOG_LEVEL: 'debug',
};

// config/production.js
export default {
  API_URL: 'https://api.example.com',
  DEBUG: false,
  LOG_LEVEL: 'error',
};
```

**💬 Explanation + Insight**

- Environment files: Create environment-specific files
- Configuration: Configure environment settings
- Variables: Use environment variables
- Security: Secure configuration data
- Deployment: Deploy with correct configurations

---

*This section covers testing types (unit, integration, E2E), Jest and RN Testing Library, native module mocking, Detox E2E testing, snapshot testing, test coverage, GitHub Actions/CircleCI/Bitrise automation, EAS Build, build variants, signing automation, environment configs, phased rollouts, OTA updates, and performance benchmarks.*
