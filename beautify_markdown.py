#!/usr/bin/env python3
"""
Markdown Beautifier - Beautifies all markdown files while preserving emojis
"""

import os
import re
from pathlib import Path

def beautify_markdown(content):
    """Beautify markdown content while preserving emojis"""
    if not content.strip():
        return content
    
    lines = content.split('\n')
    beautified = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        is_empty = not stripped
        
        # Handle empty lines - ensure max 2 consecutive empty lines
        if is_empty:
            # Count consecutive empty lines
            empty_count = 0
            j = i
            while j < len(lines) and not lines[j].strip():
                empty_count += 1
                j += 1
            
            # Add appropriate number of empty lines
            if empty_count > 0:
                # Check context to decide how many empty lines
                prev_non_empty = None
                for k in range(i - 1, -1, -1):
                    if lines[k].strip():
                        prev_non_empty = lines[k].strip()
                        break
                
                # If previous was a horizontal rule or header, keep 1 empty line
                if prev_non_empty and (prev_non_empty == '---' or prev_non_empty.startswith('#')):
                    beautified.append('')
                # Otherwise, keep max 2 empty lines
                elif empty_count > 2:
                    beautified.append('')
                    beautified.append('')
                else:
                    for _ in range(empty_count):
                        beautified.append('')
            
            i = j
            continue
        
        # Handle headers
        if stripped.startswith('#'):
            # Add blank line before header if needed
            if beautified and beautified[-1].strip() and not beautified[-1].strip().startswith('#'):
                beautified.append('')
            beautified.append(line)
            # Add blank line after header if next line is not empty and not code block
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith('```') and not next_line.startswith('<'):
                    beautified.append('')
        
        # Handle horizontal rules
        elif stripped == '---':
            # Add blank line before if previous line is not empty
            if beautified and beautified[-1].strip() and beautified[-1].strip() != '---':
                beautified.append('')
            beautified.append(line)
            # Add blank line after if next line is not empty
            if i + 1 < len(lines) and lines[i + 1].strip() and lines[i + 1].strip() != '---':
                beautified.append('')
        
        # Handle code blocks
        elif stripped.startswith('```'):
            # Add blank line before code block if previous line is not empty
            if beautified and beautified[-1].strip() and not beautified[-1].strip().startswith('```'):
                beautified.append('')
            beautified.append(line)
            i += 1
            # Copy code block content
            while i < len(lines) and not lines[i].strip().startswith('```'):
                beautified.append(lines[i])
                i += 1
            # Add closing ```
            if i < len(lines):
                beautified.append(lines[i])
                # Add blank line after code block if next line is not empty
                if i + 1 < len(lines) and lines[i + 1].strip():
                    beautified.append('')
        
        # Handle HTML blocks (like navigation divs)
        elif stripped.startswith('<div') or stripped.startswith('</div>'):
            beautified.append(line)
            # Add blank line after closing div if next line is not empty
            if stripped.startswith('</div>') and i + 1 < len(lines) and lines[i + 1].strip():
                beautified.append('')
        
        # Handle list items
        elif stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.', stripped):
            # Add blank line before list if previous line is not empty and not a list
            if beautified and beautified[-1].strip():
                prev_stripped = beautified[-1].strip()
                if not (prev_stripped.startswith('- ') or prev_stripped.startswith('* ') or re.match(r'^\d+\.', prev_stripped)):
                    beautified.append('')
            beautified.append(line)
        
        # Handle blockquotes
        elif stripped.startswith('>'):
            # Add blank line before blockquote if previous line is not empty
            if beautified and beautified[-1].strip() and not beautified[-1].strip().startswith('>'):
                beautified.append('')
            beautified.append(line)
            # Add blank line after blockquote if next line is not empty and not blockquote
            if i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].strip().startswith('>'):
                beautified.append('')
        
        # Regular line
        else:
            beautified.append(line)
        
        i += 1
    
    # Join lines
    result = '\n'.join(beautified)
    
    # Remove trailing whitespace from each line
    result = '\n'.join(line.rstrip() for line in result.split('\n'))
    
    # Fix multiple consecutive blank lines (max 2 consecutive)
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    # Ensure file ends with single newline
    result = result.rstrip() + '\n'
    
    return result

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if file is empty
        if not content.strip():
            return False
        
        beautified = beautify_markdown(content)
        
        # Only write if content changed
        if beautified != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(beautified)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all markdown files"""
    root_dir = Path(__file__).parent
    
    # Find all markdown files
    md_files = list(root_dir.rglob('*.md'))
    
    # Exclude certain directories/files if needed
    excluded = {'.git', 'node_modules', '__pycache__'}
    md_files = [f for f in md_files if not any(excluded_dir in str(f) for excluded_dir in excluded)]
    
    print(f"Found {len(md_files)} markdown files")
    print("Processing files...\n")
    
    processed = 0
    for md_file in sorted(md_files):
        if process_file(md_file):
            processed += 1
            print(f"✓ Beautified: {md_file.relative_to(root_dir)}")
    
    print(f"\n{'='*60}")
    print(f"✓ Beautification complete!")
    print(f"  - Total files: {len(md_files)}")
    print(f"  - Files beautified: {processed}")
    print(f"  - Files already formatted: {len(md_files) - processed}")

if __name__ == '__main__':
    main()
