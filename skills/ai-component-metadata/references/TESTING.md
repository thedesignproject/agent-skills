# Testing Strategies

How to validate AI metadata and enable AI-driven testing.

## Metadata Validation

### Completeness Checks
Ensure all required fields are present:

```javascript
function validateMetadata(metadata) {
  const required = [
    'component.name',
    'component.category', 
    'component.description',
    'usage.useCases',
    'accessibility.role'
  ];
  
  return required.every(path => 
    getNestedValue(metadata, path) !== undefined
  );
}
```

### Pattern Validation
Verify examples are runnable:

```javascript
// Test each commonPattern
metadata.usage.commonPatterns.forEach(pattern => {
  test(`Pattern "${pattern.name}" renders`, () => {
    const component = render(pattern.composition);
    expect(component).toBeTruthy();
  });
});
```

## AI Generation Testing

### Component Selection
Test if AI chooses correct component:

```javascript
// Test prompt
const prompt = "Create a toggle for notifications";

// Expected: AI selects Switch, not Button
expect(aiResponse).toContain('Switch');
expect(aiResponse).not.toContain('Button');
```

### Variant Selection
Test if AI applies correct variants:

```javascript
// Test prompt
const prompt = "Show an error message chip";

// Expected: AI uses danger variant
expect(aiResponse).toContain('variant="solid_danger"');
```

## Accessibility Testing

### WCAG Compliance
Validate accessibility claims:

```javascript
testingHints: {
  accessibility: [
    {
      test: "color-contrast",
      expected: "4.5:1 minimum",
      tools: ["axe-core", "pa11y"]
    },
    {
      test: "keyboard-navigation", 
      expected: "Full support",
      validate: "Tab, Space, Enter, Escape"
    }
  ]
}
```

### Screen Reader Testing
Verify announcements:

```javascript
accessibility: {
  screenReader: "Announces label and state",
  testCases: [
    {
      state: "checked",
      announcement: "Notifications, switch, checked"
    },
    {
      state: "unchecked",
      announcement: "Notifications, switch, unchecked"
    }
  ]
}
```

## Visual Regression

### Component States
Test all visual states:

```javascript
const states = metadata.behavior.states;
// ["default", "hover", "active", "focus", "disabled"]

states.forEach(state => {
  test(`Visual regression - ${state}`, async () => {
    const screenshot = await captureComponent(Component, { state });
    expect(screenshot).toMatchSnapshot();
  });
});
```

### Responsive Behavior
Test across breakpoints:

```javascript
const breakpoints = ["mobile", "tablet", "desktop"];

breakpoints.forEach(breakpoint => {
  test(`Responsive - ${breakpoint}`, () => {
    const behavior = metadata.behavior.responsive[breakpoint];
    // Verify behavior matches description
  });
});
```

## Integration Testing

### Component Combinations
Test common partnerships:

```javascript
metadata.composition.commonPartners.forEach(partner => {
  test(`Works with ${partner}`, () => {
    const combo = render(
      <Partner>
        <Component />
      </Partner>
    );
    expect(combo).toRenderWithoutErrors();
  });
});
```

### Anti-Pattern Detection
Ensure anti-patterns fail appropriately:

```javascript
metadata.usage.antiPatterns.forEach(antiPattern => {
  test(`Prevents: ${antiPattern.scenario}`, () => {
    // Verify linter/build warns about antiPattern
    expect(lintWarnings).toContain(antiPattern.reason);
  });
});
```

## AI Behavior Validation

### Prompt Testing Suite
Create test prompts for each use case:

```javascript
const testPrompts = {
  "status-indicators": [
    "Show user is online",
    "Display error state",
    "Mark as completed"
  ],
  "category-labels": [
    "Tag as technology",
    "Label with department"
  ]
};

// Test each prompt generates appropriate component
```

### Success Metrics

Track AI performance:

```javascript
metrics: {
  componentReuseRate: "85%", // Uses existing vs creating new
  variantAccuracy: "90%",    // Correct variant selection
  accessibilityScore: "100%", // Maintains a11y standards
  patternConsistency: "95%"   // Follows documented patterns
}
```

## Continuous Validation

### Automated Checks
Run on every commit:

```bash
npm run validate:metadata    # Structure validation
npm run test:ai-generation   # AI usage tests
npm run test:accessibility   # WCAG compliance
npm run test:visual          # Visual regression
```

### Manual Review
Periodic human validation:

1. Review Storybook examples
2. Test with real AI tools
3. Validate against design specs
4. Check documentation sync

## Test Data Examples

### Sample Test Cases

```javascript
export const testCases = [
  {
    prompt: "Create a primary action button",
    expected: {
      component: "Button",
      variant: "solid_primary",
      hasText: true
    }
  },
  {
    prompt: "Show loading state",
    expected: {
      component: "Spinner|Skeleton|Button",
      state: "loading"
    }
  },
  {
    prompt: "Display user role",
    expected: {
      component: "Chip|Badge",
      variant: "outline_default"
    }
  }
];
```
