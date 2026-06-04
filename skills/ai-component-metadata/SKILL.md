---
name: ai-component-metadata
version: 1.0.0
description: Generate AI-ready metadata for design system components to enable intelligent UI generation. Analyzes component structure and generates structured metadata that helps AI understand when and how to use components correctly. Useful for teams building AI-consumable design systems.
---

# AI Component Metadata Generator

Generate structured, AI-consumable metadata for design system components to enable intelligent UI generation and component usage.

## Quick Start

When analyzing a component, use the metadata schema template in `scripts/generate_metadata.py` or follow the manual process below:

```bash
# Automatic generation (reads component file)
python scripts/generate_metadata.py path/to/Component.tsx

# Or use the template directly
cp assets/metadata-template.tsx your-component-metadata.tsx
```

## Core Workflow

### 1. Analyze Component Structure
Identify:
- Component composition (slots, children)
- Available variants and states
- Props and their types
- Accessibility attributes

### 2. Generate Metadata
Create metadata following this schema:

```javascript
export const componentMetadata = {
  component: {
    name: "ComponentName",
    category: "atoms|molecules|organisms",
    description: "Brief description",
    type: "interactive|display|container|input|navigation"
  },
  
  usage: {
    useCases: ["primary-use", "secondary-use"],
    requiredProps: [],
    commonPatterns: [
      {
        name: "pattern-name",
        description: "When to use",
        composition: "JSX example"
      }
    ],
    antiPatterns: [
      {
        scenario: "what-not-to-do",
        reason: "why",
        alternative: "what-instead"
      }
    ]
  },
  
  composition: {
    slots: {},
    nestedComponents: [],
    commonPartners: [],
    parentConstraints: []
  },
  
  behavior: {
    states: [],
    interactions: {},
    responsive: {}
  },
  
  accessibility: {
    role: "ARIA role",
    keyboardSupport: "description",
    screenReader: "behavior",
    focusManagement: "strategy",
    wcag: "AA"
  },
  
  aiHints: {
    priority: "high|medium|low",
    keywords: [],
    context: "when to use"
  }
}
```

### 3. Validate Metadata
- Test with AI generation tasks
- Verify in Storybook
- Ensure examples are runnable

## Component Categories

- **atoms**: Basic building blocks (Button, Text, Input)
- **molecules**: Simple combinations (Card, Chip, FormField)
- **organisms**: Complex components (Header, Table, Form)

## Advanced Features

For complex scenarios, see:
- **Nested components**: [NESTED.md](references/NESTED.md)
- **Integration patterns**: [INTEGRATION.md](references/INTEGRATION.md)
- **Testing strategies**: [TESTING.md](references/TESTING.md)

## Working with Figma

When combining with Figma MCP:

```javascript
// Figma provides visual context
const figmaContext = await Figma.get_design_context();

// Your metadata provides behavioral context
const componentMetadata = components.Button.metadata;

// AI combines both for complete understanding
```

## Best Practices

1. **Keep examples real** - Use actual, runnable code
2. **Focus on patterns** - Document common usage patterns
3. **Include anti-patterns** - Help AI avoid mistakes
4. **Validate through usage** - Test with actual AI generation

## Success Metrics

Your metadata is effective when:
- AI uses existing components instead of recreating
- Correct variants are selected based on context
- Accessibility is maintained in generated code
- Patterns are consistent across AI outputs
