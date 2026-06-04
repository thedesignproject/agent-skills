#!/usr/bin/env python3
"""
AI Component Metadata Generator
Analyzes React/TypeScript components and generates AI-ready metadata
"""

import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Any

def extract_component_info(content: str) -> Dict[str, Any]:
    """Extract component information from TypeScript/JSX content"""
    
    # Extract component name
    name_match = re.search(r'export (?:const|function) (\w+)', content)
    component_name = name_match.group(1) if name_match else 'Unknown'
    
    # Extract props
    props_match = re.search(r'type \w+Props = \{([^}]+)\}', content, re.DOTALL)
    props = []
    if props_match:
        prop_lines = props_match.group(1).strip().split('\n')
        for line in prop_lines:
            prop_match = re.match(r'\s*(\w+)(\?)?: (.+);?', line.strip())
            if prop_match:
                props.append({
                    'name': prop_match.group(1),
                    'required': prop_match.group(2) != '?',
                    'type': prop_match.group(3).strip()
                })
    
    # Extract variants
    variant_matches = re.findall(r'variant[s]?: \{([^}]+)\}', content, re.DOTALL)
    variants = []
    for match in variant_matches:
        variant_names = re.findall(r'(\w+):', match)
        variants.extend(variant_names)
    
    # Extract states
    state_matches = re.findall(r'state[s]?: \{([^}]+)\}', content, re.DOTALL)
    states = []
    for match in state_matches:
        state_names = re.findall(r'(\w+):', match)
        states.extend(state_names)
    
    # Detect component type
    component_type = 'display'
    if 'onClick' in content or 'onPress' in content:
        component_type = 'interactive'
    elif 'onChange' in content or 'onInput' in content:
        component_type = 'input'
    elif 'Container' in content or 'Layout' in content:
        component_type = 'container'
    
    # Detect category
    category = 'atoms'
    if 'withStaticProperties' in content or '.Text' in content or '.Icon' in content:
        category = 'molecules'
    elif 'Header' in component_name or 'Footer' in component_name or 'Form' in component_name:
        category = 'organisms'
    
    # Extract nested components
    nested_match = re.findall(r'(\w+): \w+(?:Text|Icon|Thumb|Header|Body|Footer)', content)
    nested_components = list(set(nested_match))
    
    return {
        'name': component_name,
        'type': component_type,
        'category': category,
        'props': props,
        'variants': list(set(variants)),
        'states': list(set(states)),
        'nested_components': nested_components
    }

def generate_metadata(component_info: Dict[str, Any]) -> Dict[str, Any]:
    """Generate AI-ready metadata from component information"""
    
    name = component_info['name']
    
    # Generate use cases based on component name and type
    use_cases = []
    name_lower = name.lower()
    
    if 'button' in name_lower:
        use_cases = ['primary-actions', 'form-submission', 'navigation-triggers']
    elif 'switch' in name_lower or 'toggle' in name_lower:
        use_cases = ['feature-toggles', 'settings-preferences', 'notification-controls']
    elif 'chip' in name_lower or 'tag' in name_lower:
        use_cases = ['status-indicators', 'category-labels', 'filter-tags']
    elif 'text' in name_lower:
        use_cases = ['body-text', 'headings', 'labels', 'captions']
    elif 'card' in name_lower:
        use_cases = ['content-containers', 'information-display', 'interactive-tiles']
    else:
        use_cases = ['general-purpose-component']
    
    # Generate keywords
    keywords = [name_lower]
    keywords.extend(name_lower.split('_'))
    keywords.extend(name_lower.split('-'))
    
    # Build metadata structure
    metadata = {
        'component': {
            'name': name,
            'category': component_info['category'],
            'description': f'{name} component for design system',
            'type': component_info['type']
        },
        'usage': {
            'useCases': use_cases,
            'requiredProps': [p['name'] for p in component_info['props'] if p.get('required')],
            'commonPatterns': [
                {
                    'name': 'basic-usage',
                    'description': f'Basic {name} usage',
                    'composition': f'<{name}></{name}>'
                }
            ],
            'antiPatterns': []
        },
        'composition': {
            'slots': {},
            'nestedComponents': component_info.get('nested_components', []),
            'commonPartners': [],
            'parentConstraints': []
        },
        'behavior': {
            'states': component_info.get('states', ['default']),
            'interactions': {},
            'responsive': {
                'mobile': 'Adapts to mobile viewport',
                'desktop': 'Standard desktop layout'
            }
        },
        'accessibility': {
            'role': 'generic',
            'keyboardSupport': 'Standard keyboard navigation',
            'screenReader': 'Properly announced',
            'focusManagement': 'Focus ring on interaction',
            'wcag': 'AA'
        },
        'aiHints': {
            'priority': 'medium',
            'keywords': list(set(keywords)),
            'context': f'Use for {", ".join(use_cases[:2])}'
        }
    }
    
    # Add variant-specific info
    if component_info.get('variants'):
        metadata['variants'] = {
            v: {'useCase': f'Use for {v} variant'} 
            for v in component_info['variants'][:5]  # Limit to first 5
        }
    
    # Adjust for specific component types
    if component_info['type'] == 'interactive':
        metadata['behavior']['interactions'] = {
            'click': 'Triggers action',
            'hover': 'Shows hover state'
        }
        metadata['accessibility']['role'] = 'button'
        metadata['accessibility']['keyboardSupport'] = 'Space/Enter to activate'
    
    elif component_info['type'] == 'input':
        metadata['accessibility']['role'] = 'textbox'
        metadata['behavior']['interactions'] = {
            'change': 'Updates value',
            'focus': 'Shows focus state'
        }
    
    return metadata

def format_metadata_for_tsx(metadata: Dict[str, Any]) -> str:
    """Format metadata as TypeScript export"""
    
    # Convert to JSON with proper indentation
    json_str = json.dumps(metadata, indent=2)
    
    # Format as TypeScript const export
    tsx_output = f"""// AI-ready component metadata
export const componentMetadata = {json_str} as const;
"""
    
    return tsx_output

def main():
    """Main entry point"""
    
    if len(sys.argv) < 2:
        print("Usage: python generate_metadata.py <component-file.tsx>")
        print("\nThis script analyzes React/TypeScript components and generates AI-ready metadata.")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found")
        sys.exit(1)
    
    # Read component file
    content = file_path.read_text()
    
    # Extract component information
    print(f"Analyzing {file_path.name}...")
    component_info = extract_component_info(content)
    
    # Generate metadata
    print(f"Generating metadata for {component_info['name']}...")
    metadata = generate_metadata(component_info)
    
    # Format as TypeScript
    tsx_output = format_metadata_for_tsx(metadata)
    
    # Save to file
    output_path = file_path.parent / f"{file_path.stem}-metadata.tsx"
    output_path.write_text(tsx_output)
    
    print(f"✅ Metadata generated: {output_path}")
    print(f"\nComponent: {component_info['name']}")
    print(f"Category: {component_info['category']}")
    print(f"Type: {component_info['type']}")
    print(f"Variants: {', '.join(component_info.get('variants', ['none']))}")
    print(f"States: {', '.join(component_info.get('states', ['default']))}")
    print(f"\nYou can now add this metadata to your component file.")

if __name__ == '__main__':
    main()
