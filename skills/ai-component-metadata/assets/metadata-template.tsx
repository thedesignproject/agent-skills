import React from 'react';

/**
 * AI Component Metadata Template
 * 
 * Instructions:
 * 1. Replace COMPONENT_NAME with your actual component name
 * 2. Fill in all metadata fields based on your component
 * 3. Remove any sections that don't apply
 * 4. Add to your component file as an export
 */

// ============================================
// AI-READY METADATA
// ============================================

export const componentMetadata = {
  component: {
    name: "COMPONENT_NAME",
    category: "atoms", // atoms | molecules | organisms
    description: "One-line description of component purpose",
    type: "interactive" // interactive | display | container | input | navigation
  },
  
  usage: {
    useCases: [
      // List specific, semantic use cases
      "primary-use-case",
      "secondary-use-case"
    ],
    
    requiredProps: [
      // Props that must always be provided
    ],
    
    commonPatterns: [
      {
        name: "basic-usage",
        description: "Most common usage pattern",
        composition: `
          <COMPONENT_NAME>
            Content
          </COMPONENT_NAME>
        `
      }
    ],
    
    antiPatterns: [
      {
        scenario: "what-not-to-do",
        reason: "Why this is problematic",
        alternative: "What to do instead"
      }
    ]
  },
  
  composition: {
    slots: {
      // Define slots/subcomponents
      "SlotName": {
        required: false,
        description: "Purpose of this slot"
      }
    },
    
    nestedComponents: [
      // Child components used
    ],
    
    commonPartners: [
      // Components often used together
    ],
    
    parentConstraints: [
      // Placement restrictions
    ]
  },
  
  behavior: {
    states: ["default", "hover", "active", "disabled"],
    
    interactions: {
      "click": "Action triggered",
      "focus": "Focus behavior"
    },
    
    responsive: {
      "mobile": "Mobile behavior",
      "desktop": "Desktop behavior"
    }
  },
  
  accessibility: {
    role: "button", // ARIA role
    keyboardSupport: "Space/Enter to activate",
    screenReader: "Announces label and state",
    focusManagement: "Visible focus ring",
    wcag: "AA"
  },
  
  aiHints: {
    priority: "medium", // high | medium | low
    keywords: ["trigger", "words"],
    context: "When AI should use this component"
  }
} as const;
