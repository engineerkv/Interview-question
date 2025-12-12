#!/usr/bin/env python3
"""
Script to improve examples in markdown files by adding helpful comments
"""

import os
import re
from pathlib import Path

def needs_comment(code_block, question_text):
    """Determine if a code block needs comments"""
    lines = code_block.split('\n')
    non_empty_lines = [l.strip() for l in lines if l.strip() and not l.strip().startswith('//')]
    
    # If already has comments, might be okay
    has_comments = any('//' in line for line in lines)
    
    # If very simple (1-3 lines), might not need comments
    if len(non_empty_lines) <= 3 and not has_comments:
        return False
    
    # If complex logic or multiple concepts, needs comments
    if len(non_empty_lines) > 5:
        return True
    
    # If has function definitions, conditionals, loops - might need comments
    complex_patterns = ['function', 'if', 'for', 'while', 'switch', '=>', 'class', 'interface', 'type']
    if any(pattern in code_block for pattern in complex_patterns):
        return True
    
    return False

def add_helpful_comments(code_block, question_text):
    """Add helpful comments to code block when needed"""
    lines = code_block.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip if already has comment
        if '//' in line:
            result.append(line)
            i += 1
            continue
        
        # Add comments for function definitions
        if re.match(r'^\s*(function|const|let|var|class|interface|type)\s+\w+', stripped):
            if 'function' in stripped or '=>' in stripped:
                # Check if next few lines are complex
                next_lines = ' '.join(lines[i+1:i+4])
                if any(keyword in next_lines for keyword in ['return', '{', 'if', 'for']):
                    result.append(line)
                    i += 1
                    continue
        
        # Add comments for complex expressions
        if '?' in stripped and ':' in stripped:  # Ternary
            if not any('//' in l for l in lines[max(0, i-1):i+2]):
                result.append(line)
                result.append('  // Ternary operator: condition ? valueIfTrue : valueIfFalse')
                i += 1
                continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if file is empty
        if not content.strip():
            return False
        
        # Pattern to find code blocks with their preceding question
        pattern = r'(## Q\d+\.\s+[^\n]+\n\n[^\n]+\n\n(?:- \*\*Trade-offs\*\*:[^\n]+\n\n)?Example:\n\n```\w+\n)(.*?)(\n```)'
        
        def replace_code_block(match):
            prefix = match.group(1)
            code = match.group(2)
            suffix = match.group(3)
            
            # Don't modify if code is very simple
            if len(code.strip().split('\n')) <= 3 and '//' not in code:
                return prefix + code + suffix
            
            # Add comments only where they add value
            # This is a conservative approach - we'll manually review complex cases
            return prefix + code + suffix
        
        new_content = re.sub(pattern, replace_code_block, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

if __name__ == '__main__':
    print("This script is a helper. Manual review and improvement is recommended.")
    print("Please review examples manually to add appropriate comments.")
