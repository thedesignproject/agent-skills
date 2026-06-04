// Example: Button Component with AI Metadata

export const Button = withStaticProperties(ButtonFrame, {
  Text: ButtonText,
  Icon: ButtonIcon,
});

// AI-ready component metadata
export const componentMetadata = {
  component: {
    name: "Button",
    category: "atoms",
    description: "Interactive element for triggering user actions",
    type: "interactive"
  },
  
  usage: {
    useCases: [
      "primary-actions",
      "form-submission",
      "navigation-triggers",
      "dialog-confirmations",
      "state-changes"
    ],
    
    requiredProps: [],
    
    commonPatterns: [
      {
        name: "primary-action",
        description: "Main call-to-action button",
        composition: `
          <Button variant="solid_primary" size="md">
            <Button.Text>Take Action</Button.Text>
          </Button>
        `
      },
      {
        name: "secondary-action",
        description: "Secondary or cancel actions",
        composition: `
          <Button variant="outline_default" size="md">
            <Button.Text>Cancel</Button.Text>
          </Button>
        `
      },
      {
        name: "icon-button",
        description: "Button with icon and text",
        composition: `
          <Button variant="solid_primary">
            <Button.Icon><Plus /></Button.Icon>
            <Button.Text>Add Item</Button.Text>
          </Button>
        `
      },
      {
        name: "icon-only",
        description: "Icon-only button for compact interfaces",
        composition: `
          <Button variant="ghost_default" iconOnly>
            <Button.Icon><Settings /></Button.Icon>
          </Button>
        `
      }
    ],
    
    antiPatterns: [
      {
        scenario: "multiple-primary-buttons",
        reason: "Confuses user decision-making and visual hierarchy",
        alternative: "Use one primary button, others as secondary or tertiary"
      },
      {
        scenario: "button-as-link",
        reason: "Buttons trigger actions, links navigate",
        alternative: "Use Link component for navigation"
      }
    ]
  },
  
  composition: {
    slots: {
      "Text": {
        required: false,
        description: "Button label text"
      },
      "Icon": {
        required: false,
        description: "Icon element for visual enhancement"
      }
    },
    
    nestedComponents: ["Button.Text", "Button.Icon"],
    
    commonPartners: ["Form", "Card", "Modal", "Dialog", "Toolbar"],
    
    parentConstraints: []
  },
  
  behavior: {
    states: ["default", "hover", "pressed", "focused", "disabled", "loading"],
    
    interactions: {
      "click": "Executes primary action",
      "hover": "Shows interactive state",
      "focus": "Keyboard focus indicator",
      "space": "Activates when focused",
      "enter": "Activates when focused"
    },
    
    responsive: {
      "mobile": "Full width in narrow containers",
      "tablet": "Adapts to container width",
      "desktop": "Inline with auto width"
    }
  },
  
  accessibility: {
    role: "button",
    keyboardSupport: "Full keyboard navigation with Space/Enter activation",
    screenReader: "Announces button label and state",
    focusManagement: "Visible focus ring, follows focus order",
    wcag: "AA"
  },
  
  aiHints: {
    priority: "high",
    keywords: ["button", "action", "click", "submit", "cta", "trigger"],
    context: "Use for any interactive action that changes state or triggers behavior"
  }
} as const;
