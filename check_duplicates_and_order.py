#!/usr/bin/env python3
"""
Script to check for duplicate question numbers, overlapping content, and verify logical order.
Creates a reference document for duplicates/overlaps.
"""
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_question_numbers(file_path):
    """Extract all question numbers from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all Q# patterns
        questions = re.findall(r'^## (Q\d+)\.', content, re.MULTILINE)
        return questions, content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return [], ""

def find_overlapping_topics(content1, content2, file1, file2):
    """Find overlapping topics between two files."""
    # Extract keywords from content (simplified approach)
    keywords1 = set(re.findall(r'\b(?:HTTP|REST|GraphQL|WebSocket|TCP|UDP|DNS|TLS|API|Database|Cache|Redis|MongoDB|SQL|Node\.js|React|JavaScript|TypeScript|Performance|Security|Testing|Authentication|Authorization|Scaling|Sharding|Replication|Load\s+balancing|CDN|Microservices|Event\s+loop|Promise|Async|Await|Closure|Prototype|Hoisting|State|Props|Hooks|Component|Rendering|SSR|SSG|ISR|CSR)\b', content1, re.IGNORECASE))
    keywords2 = set(re.findall(r'\b(?:HTTP|REST|GraphQL|WebSocket|TCP|UDP|DNS|TLS|API|Database|Cache|Redis|MongoDB|SQL|Node\.js|React|JavaScript|TypeScript|Performance|Security|Testing|Authentication|Authorization|Scaling|Sharding|Replication|Load\s+balancing|CDN|Microservices|Event\s+loop|Promise|Async|Await|Closure|Prototype|Hoisting|State|Props|Hooks|Component|Rendering|SSR|SSG|ISR|CSR)\b', content2, re.IGNORECASE))
    
    overlap = keywords1.intersection(keywords2)
    return overlap if len(overlap) > 3 else set()  # Only report if significant overlap

def check_logical_order():
    """Check logical order of folders and sections."""
    # Expected order based on learning path
    expected_order = {
        'FE': ['HTML', 'CSS', 'Javascript', 'Typescript', 'React', 'Next', 'React-Native', 'FE-System-Design'],
        'BE': ['Node-Express', 'Sql', 'No-Sql', 'BE-System-Design'],
        'DSA': ['Arrays', 'Strings', 'Linked List', 'Stacks & Queues', 'Binary Trees', 'Binary Search Tree', 
                'Heaps & Priority Queue', 'Graphs', 'Dynamic Programming', 'Recursion & Backtracking',
                'Matrix', 'Trie', 'Binary Search', 'Bit Manipulation', 'Math']
    }
    return expected_order

def main():
    """Main function to check duplicates and overlaps."""
    base_dir = Path(__file__).parent
    
    # Find all markdown files
    exclude_files = {'question.md', 'README.md', 'CROSS_CHECK_REPORT.md', 'rule.md', 
                     'check_duplicates_and_order.py', 'ISSUES_FOUND.md', 'DUPLICATES_REFERENCE.md'}
    exclude_patterns = ['Cheatsheet.md']
    
    md_files = []
    question_map = defaultdict(list)  # question_number -> list of files
    file_contents = {}  # file_path -> content
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                if file not in exclude_files and not any(pattern in file for pattern in exclude_patterns):
                    file_path = os.path.join(root, file)
                    md_files.append(file_path)
                    questions, content = extract_question_numbers(file_path)
                    file_contents[file_path] = content
                    for q in questions:
                        question_map[q].append(file_path)
    
    # Find duplicates within same tech stack
    duplicates = defaultdict(list)
    for q_num, files in question_map.items():
        if len(files) > 1:
            # Group by tech stack
            tech_stacks = defaultdict(list)
            for file_path in files:
                if 'FE/' in file_path:
                    tech_stacks['FE'].append(file_path)
                elif 'BE/' in file_path:
                    tech_stacks['BE'].append(file_path)
                elif 'DSA/' in file_path:
                    tech_stacks['DSA'].append(file_path)
                else:
                    tech_stacks['OTHER'].append(file_path)
            
            # Only report if duplicate within same tech stack
            for stack, stack_files in tech_stacks.items():
                if len(stack_files) > 1:
                    duplicates[q_num].extend(stack_files)
    
    # Find overlaps - only between related files
    overlaps = []
    file_list = list(md_files)
    for i in range(len(file_list)):
        for j in range(i + 1, len(file_list)):
            file1, file2 = file_list[i], file_list[j]
            # Check overlaps between:
            # 1. FE System Design and BE System Design
            # 2. Node.js in FE and Node.js in BE
            # 3. JavaScript in FE and Node.js in BE
            should_check = False
            if ('FE-System-Design' in file1 and 'BE-System-Design' in file2) or \
               ('FE-System-Design' in file2 and 'BE-System-Design' in file1):
                should_check = True
            elif ('FE/' in file1 and 'Node.js' in file1 and 'BE/' in file2 and 'Node' in file2) or \
                 ('FE/' in file2 and 'Node.js' in file2 and 'BE/' in file1 and 'Node' in file1):
                should_check = True
            elif ('FE/Javascript' in file1 and 'BE/Node-Express' in file2) or \
                 ('FE/Javascript' in file2 and 'BE/Node-Express' in file1):
                should_check = True
            
            if should_check:
                overlap = find_overlapping_topics(
                    file_contents[file1], 
                    file_contents[file2], 
                    file1, 
                    file2
                )
                if overlap:
                    overlaps.append({
                        'file1': file1,
                        'file2': file2,
                        'topics': overlap
                    })
    
    # Generate reference document
    reference_content = f"""# 📋 Duplicates & Overlaps Reference Guide

**Generated:** {Path(__file__).name}
**Purpose:** Reference guide for duplicate question numbers and overlapping content across folders

---

## 🔍 Duplicate Question Numbers

"""
    
    if duplicates:
        reference_content += f"**Found {len(duplicates)} duplicate question numbers:**\n\n"
        for q_num, files in sorted(duplicates.items()):
            reference_content += f"### {q_num}\n\n"
            for file_path in files:
                rel_path = os.path.relpath(file_path, base_dir)
                reference_content += f"- [{rel_path}]({rel_path})\n"
            reference_content += "\n**Action:** Check these files and ensure questions are unique or add cross-references.\n\n"
    else:
        reference_content += "✅ **No duplicate question numbers found!**\n\n"
    
    reference_content += "\n---\n\n## 🔗 Overlapping Content Topics\n\n"
    
    if overlaps:
        reference_content += f"**Found {len(overlaps)} potential content overlaps:**\n\n"
        for overlap in overlaps[:20]:  # Limit to first 20
            file1_rel = os.path.relpath(overlap['file1'], base_dir)
            file2_rel = os.path.relpath(overlap['file2'], base_dir)
            topics = ', '.join(sorted(list(overlap['topics']))[:10])
            reference_content += f"### Overlap between:\n"
            reference_content += f"- [{file1_rel}]({file1_rel})\n"
            reference_content += f"- [{file2_rel}]({file2_rel})\n\n"
            reference_content += f"**Common topics:** {topics}\n\n"
            reference_content += f"**Action:** Review both files - if content overlaps significantly, add cross-references.\n\n"
    else:
        reference_content += "✅ **No significant content overlaps found!**\n\n"
    
    reference_content += "\n---\n\n## 📚 Logical Order Reference\n\n"
    
    expected_order = check_logical_order()
    reference_content += "### Recommended Learning Path:\n\n"
    
    reference_content += "#### Frontend (FE)\n"
    reference_content += "1. HTML (Fundamentals)\n"
    reference_content += "2. CSS (Styling)\n"
    reference_content += "3. JavaScript (Core language)\n"
    reference_content += "4. TypeScript (Type safety)\n"
    reference_content += "5. React (UI library)\n"
    reference_content += "6. Next.js (React framework)\n"
    reference_content += "7. React Native (Mobile)\n"
    reference_content += "8. FE System Design (Advanced)\n\n"
    
    reference_content += "#### Backend (BE)\n"
    reference_content += "1. Node.js & Express (Server fundamentals)\n"
    reference_content += "2. SQL (Relational databases)\n"
    reference_content += "3. NoSQL/MongoDB (Document databases)\n"
    reference_content += "4. BE System Design (Advanced)\n\n"
    
    reference_content += "#### DSA\n"
    reference_content += "1. Arrays (Foundation)\n"
    reference_content += "2. Strings (Text manipulation)\n"
    reference_content += "3. Linked List (Linear structures)\n"
    reference_content += "4. Stacks & Queues (Linear structures)\n"
    reference_content += "5. Binary Trees (Tree structures)\n"
    reference_content += "6. Binary Search Tree (Tree structures)\n"
    reference_content += "7. Heaps & Priority Queue (Tree structures)\n"
    reference_content += "8. Graphs (Advanced structures)\n"
    reference_content += "9. Dynamic Programming (Advanced algorithms)\n"
    reference_content += "10. Recursion & Backtracking (Advanced algorithms)\n"
    reference_content += "11. Matrix (Specialized)\n"
    reference_content += "12. Trie (Specialized)\n"
    reference_content += "13. Binary Search (Search algorithms)\n"
    reference_content += "14. Bit Manipulation (Specialized)\n"
    reference_content += "15. Math (Specialized)\n\n"
    
    reference_content += "\n---\n\n## 📝 How to Use This Reference\n\n"
    reference_content += "1. **For Duplicates:** If you find a duplicate question number, check both files and either:\n"
    reference_content += "   - Remove the duplicate if it's truly the same question\n"
    reference_content += "   - Add a cross-reference: `See also: [Q# in File Name](path/to/file.md)`\n\n"
    reference_content += "2. **For Overlaps:** If content overlaps significantly:\n"
    reference_content += "   - Add cross-references at the beginning of overlapping sections\n"
    reference_content += "   - Example: `📌 Related: See [Topic Name](path/to/file.md#section)`\n\n"
    reference_content += "3. **For Logical Order:** Follow the recommended learning path for interview preparation.\n\n"
    
    # Write reference document
    output_file = base_dir / 'DUPLICATES_REFERENCE.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reference_content)
    
    print(f"✅ Analysis complete!")
    print(f"📊 Found {len(duplicates)} duplicate question numbers")
    print(f"📊 Found {len(overlaps)} potential content overlaps")
    print(f"📄 Reference document created: {output_file}")

if __name__ == '__main__':
    main()
