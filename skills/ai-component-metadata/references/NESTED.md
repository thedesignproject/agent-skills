# Nested Component Metadata

Guide for handling metadata in component composition hierarchies.

## Traversal Strategy

When components contain other components, metadata should reference the full tree:

```javascript
// Card → CardHeader → Text (h3)
//      → CardBody → Text (body2)
//      → CardFooter → Button → Button.Text

composition: {
  nestedComponents: ["CardHeader", "CardBody", "CardFooter"],
  // Each nested component has its own metadata
}
```

## Inheritance Patterns

### Props Inheritance
Child components may inherit certain metadata from parents:

```javascript
// Parent Card metadata
accessibility: {
  role: "article",
  landmark: true
}

// Child CardHeader inherits context
accessibility: {
  role: "heading",
  level: "derived from parent" // h2 if Card is top-level, h3 if nested
}
```

### Context Propagation
Semantic meaning flows down:

```javascript
// Form provides context
behavior: {
  context: "form-submission"
}

// Button inside Form understands its purpose
aiHints: {
  contextAware: true,
  inferredPurpose: "submit-action when inside Form"
}
```

## Composition Examples

### Simple Composition (Molecule)
```javascript
// Chip contains Text and optional Icon
composition: {
  slots: {
    "Text": { required: true, description: "Label content" },
    "Icon": { required: false, description: "Visual indicator" }
  },
  nestedComponents: ["Text", "Icon"]
}
```

### Complex Composition (Organism)
```javascript
// Table contains multiple levels
composition: {
  nestedComponents: [
    "TableHeader",
    "TableBody", 
    "TableFooter"
  ],
  deepStructure: {
    "TableHeader": ["TableRow", "TableHead"],
    "TableBody": ["TableRow", "TableCell"],
    "TableRow": ["TableCell", "Chip", "Button", "Text"]
  }
}
```

## AI Traversal Hints

Help AI understand component relationships:

```javascript
aiHints: {
  traversalRules: [
    "Always include TableRow when using Table",
    "TableCell can contain any atom or molecule",
    "Nested Tables should be avoided"
  ]
}
```
