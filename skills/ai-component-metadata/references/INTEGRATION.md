# Integration Patterns

Common patterns for integrating components with AI metadata.

## With Figma MCP

Combine visual and behavioral context:

```javascript
// Step 1: Get visual specs from Figma
const figmaContext = await Figma.get_design_context();
// Returns: layout, spacing, colors, typography

// Step 2: Get behavioral specs from metadata
const behaviorContext = componentMetadata.behavior;
// Returns: states, interactions, accessibility

// Step 3: AI combines both
const fullContext = {
  visual: figmaContext,
  behavioral: behaviorContext,
  implementation: componentCode
};
```

## With Code Generation

### Direct Component Usage
AI should prefer existing components:

```javascript
// User: "Create a status indicator"

// ❌ Bad: AI creates new element
<div style={{background: 'green'}}>Active</div>

// ✅ Good: AI uses existing Chip
<Chip variant="solid_success" size="sm">
  <Chip.Text>Active</Chip.Text>
</Chip>
```

### Pattern Recognition
AI learns from commonPatterns:

```javascript
// Metadata defines pattern
commonPatterns: [{
  name: "form-actions",
  composition: `
    <Stack direction="horizontal" gap="$2">
      <Button variant="solid_primary">Submit</Button>
      <Button variant="outline_default">Cancel</Button>
    </Stack>
  `
}]

// AI recognizes and applies pattern
// User: "Add form buttons"
// AI generates the exact pattern from metadata
```

## With Documentation

### Sync Strategies

1. **Manual Sync**
   - Developer updates both docs and metadata
   - Good for small teams

2. **Semi-Automated**
   - Metadata generates from JSDoc comments
   - Script updates both sources

3. **Fully Automated**
   - Single source of truth (code)
   - Build process generates metadata
   - Webhooks sync documentation

### Documentation Integration

```javascript
// Component file
/**
 * @metadata
 * @category atoms
 * @type interactive
 * @useCases ["primary-actions", "form-submission"]
 */
export const Button = ...

// Build process extracts to metadata
componentMetadata = extractMetadata(Button);
```

## With Testing

### AI-Driven Test Generation

```javascript
// Metadata informs test cases
accessibility: {
  keyboardSupport: "Space/Enter activates",
  focusManagement: "Visible ring on focus"
}

// AI generates tests
describe('Button Accessibility', () => {
  test('responds to Space key', () => {
    // Test implementation
  });
  
  test('shows focus ring', () => {
    // Test implementation
  });
});
```

### Visual Regression Hints

```javascript
testingHints: {
  visualRegression: [
    "All color variants render correctly",
    "Hover states are visible",
    "Focus rings appear on keyboard nav"
  ]
}
```

## With Design Tokens

```javascript
// Tokens provide values
tokens: {
  colors: { primary: "#007AFF" },
  spacing: { md: "16px" }
}

// Metadata provides meaning
aiHints: {
  tokenUsage: {
    "primary": "Use for main CTAs",
    "spacing.md": "Default component spacing"
  }
}
```

## Framework-Specific Patterns

### React/Tamagui
```javascript
// Metadata for styled components
composition: {
  styling: "tamagui",
  styledProps: ["size", "variant", "state"],
  tokenPrefix: "$"
}
```

### Vue
```javascript
// Metadata for Vue components
composition: {
  framework: "vue",
  slots: { default: true, icon: false },
  emits: ["click", "change"]
}
```

### Web Components
```javascript
// Metadata for custom elements
composition: {
  framework: "web-components",
  tagName: "ds-button",
  attributes: ["variant", "size", "disabled"]
}
```
