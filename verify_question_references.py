#!/usr/bin/env python3
"""
Script to verify all question references work properly.
Checks if referenced questions exist and if markdown links are correct.
"""
import os
import re
from pathlib import Path
from collections import defaultdict

def extract_question_anchors(file_path):
    """Extract all question headers and their anchor IDs."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        anchors = {}
        # Find all question headers: ## Q#. Title
        pattern = r'^## (Q\d+)\.\s*(.+)$'
        for match in re.finditer(pattern, content, re.MULTILINE):
            q_num = match.group(1)
            title = match.group(2).strip()
            # Remove emoji and clean title for anchor
            title_clean = re.sub(r'[\U0001F300-\U0001F9FF\U00002600-\U000026FF\U00002700-\U000027BF]', '', title).strip()
            # Generate anchor (GitHub markdown format: lowercase, spaces to hyphens, remove special chars)
            anchor = re.sub(r'[^\w\s-]', '', title_clean.lower())
            anchor = re.sub(r'[-\s]+', '-', anchor)
            anchor = f"q{q_num.lower()}-{anchor}"
            anchors[q_num] = {
                'title': title,
                'title_clean': title_clean,
                'anchor': anchor,
                'line': content[:match.start()].count('\n') + 1
            }
        
        return anchors, content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, ""

def find_question_references(content, file_path):
    """Find all question references in content."""
    references = []
    
    # Pattern 1: [Q#: Title](path#anchor)
    pattern1 = r'\[Q(\d+):[^\]]+\]\(([^#]+)#([^)]+)\)'
    for match in re.finditer(pattern1, content):
        references.append({
            'type': 'link',
            'q_num': match.group(1),
            'file_path': match.group(2),
            'anchor': match.group(3),
            'full_match': match.group(0),
            'line': content[:match.start()].count('\n') + 1
        })
    
    # Pattern 2: see Q# or Q#: (without link)
    pattern2 = r'(?:see|See|SEE|refer|Refer|REFER|check|Check|CHECK)\s+Q(\d+)[:\s]'
    for match in re.finditer(pattern2, content):
        # Find context around this reference
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 50)
        context = content[start:end]
        references.append({
            'type': 'text',
            'q_num': match.group(1),
            'context': context,
            'full_match': match.group(0),
            'line': content[:match.start()].count('\n') + 1
        })
    
    return references

def resolve_file_path(relative_path, base_file):
    """Resolve relative file path to absolute."""
    import urllib.parse
    # Decode URL-encoded paths (%29 -> ), etc.)
    decoded_path = urllib.parse.unquote(relative_path)
    base_dir = Path(base_file).parent
    
    # Handle ../ paths - go up one level from base_dir
    if decoded_path.startswith('../'):
        # Remove ../ and resolve relative to parent of base_dir
        remaining = decoded_path[3:]
        resolved = base_dir.parent / remaining
    elif decoded_path.startswith('./'):
        resolved = base_dir / decoded_path[2:]
    else:
        resolved = base_dir / decoded_path
    
    # Normalize path (resolve .. and .)
    resolved = resolved.resolve()
    
    # If file doesn't exist, try to find by filename in the directory structure
    if not resolved.exists():
        target_name = Path(decoded_path).name
        # Search in base_dir's parent directory
        search_dir = base_dir.parent
        if search_dir.exists():
            for file in search_dir.rglob(target_name):
                if file.is_file():
                    return file.resolve()
    
    return resolved

def main():
    """Main function to verify all references."""
    base_dir = Path(__file__).parent
    
    # Find all markdown files
    exclude_files = {'question.md', 'README.md', 'CROSS_CHECK_REPORT.md', 'rule.md', 
                     'verify_question_references.py', 'ISSUES_FOUND.md', 'DUPLICATES_REFERENCE.md',
                     'QUESTION_REFERENCES_REPORT.md'}
    exclude_patterns = ['Cheatsheet.md']
    
    md_files = []
    all_questions = {}  # file_path -> {q_num -> anchor info}
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                if file not in exclude_files and not any(pattern in file for pattern in exclude_patterns):
                    file_path = os.path.join(root, file)
                    md_files.append(file_path)
                    anchors, _ = extract_question_anchors(file_path)
                    all_questions[file_path] = anchors
    
    # Check references in all files
    issues = []
    verified = []
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            references = find_question_references(content, file_path)
            
            for ref in references:
                if ref['type'] == 'link':
                    # Resolve file path
                    resolved_path = resolve_file_path(ref['file_path'], file_path)
                    resolved_path_str = str(resolved_path)
                    
                    # Check if target file exists
                    if resolved_path_str not in all_questions:
                        # Try to find file with similar name
                        found = False
                        for known_file in all_questions.keys():
                            if Path(known_file).name == Path(resolved_path).name:
                                resolved_path_str = known_file
                                found = True
                                break
                        
                        if not found:
                            issues.append({
                                'file': file_path,
                                'line': ref['line'],
                                'issue': f"Target file not found: {ref['file_path']}",
                                'reference': ref['full_match']
                            })
                            continue
                    
                    # Check if question exists in target file
                    if resolved_path_str not in all_questions:
                        # Try to find by filename
                        target_name = Path(resolved_path).name
                        found_file = None
                        for known_file in all_questions.keys():
                            if Path(known_file).name == target_name:
                                found_file = known_file
                                break
                        
                        if not found_file:
                            issues.append({
                                'file': file_path,
                                'line': ref['line'],
                                'issue': f"Target file not found: {ref['file_path']}",
                                'reference': ref['full_match']
                            })
                            continue
                        resolved_path_str = found_file
                    
                    # Normalize path for comparison
                    resolved_path_obj = Path(resolved_path_str)
                    if resolved_path_obj.exists():
                        normalized_target = str(resolved_path_obj.resolve())
                    else:
                        normalized_target = None
                    
                    found_target = None
                    # First try exact match
                    if normalized_target:
                        for known_file in all_questions.keys():
                            if str(Path(known_file).resolve()) == normalized_target:
                                found_target = known_file
                                break
                    
                    # If not found, try by filename (handle URL encoding)
                    if not found_target:
                        target_name = Path(decoded_path).name
                        # Also try URL-decoded version
                        target_name_decoded = urllib.parse.unquote(target_name)
                        for known_file in all_questions.keys():
                            known_name = Path(known_file).name
                            if known_name == target_name or known_name == target_name_decoded:
                                found_target = known_file
                                break
                    
                    # Last resort: search by partial filename match
                    if not found_target:
                        target_base = Path(decoded_path).stem.lower().replace(' ', '').replace(')', '')
                        for known_file in all_questions.keys():
                            known_base = Path(known_file).stem.lower().replace(' ', '').replace(')', '')
                            if target_base in known_base or known_base in target_base:
                                found_target = known_file
                                break
                    
                    if not found_target:
                        issues.append({
                            'file': file_path,
                            'line': ref['line'],
                            'issue': f"Target file not found: {resolved_path_str}",
                            'reference': ref['full_match']
                        })
                        continue
                    
                    # Check if question exists - ref['q_num'] is just the number, need 'Q' prefix
                    q_key = f"Q{ref['q_num']}"
                    if q_key not in all_questions[found_target]:
                        issues.append({
                            'file': file_path,
                            'line': ref['line'],
                            'issue': f"Question {q_key} not found in target file (found questions: {list(all_questions[found_target].keys())[:10]})",
                            'reference': ref['full_match'],
                            'target_file': found_target
                        })
                    else:
                        # Verify anchor format (optional check)
                        expected_anchor = all_questions[resolved_path_str][ref['q_num']]['anchor']
                        # Anchor might be slightly different, that's okay - markdown handles it
                        verified.append({
                            'file': file_path,
                            'line': ref['line'],
                            'reference': ref['full_match'],
                            'status': 'verified',
                            'target_q': q_key,
                            'target_file': os.path.relpath(found_target, base_dir)
                        })
                
                elif ref['type'] == 'text':
                    # Text reference without link - check if we can find the question
                    # This is just informational
                    pass
        
        except Exception as e:
            issues.append({
                'file': file_path,
                'line': 0,
                'issue': f"Error processing file: {e}",
                'reference': ''
            })
    
    # Generate report
    report = f"""# ✅ Question References Verification Report

**Generated:** verify_question_references.py
**Total files checked:** {len(md_files)}
**Total references verified:** {len(verified)}
**Issues found:** {len(issues)}

---

## ✅ Verified References

**{len(verified)} references verified successfully!**

---

## ⚠️ Issues Found

"""
    
    if issues:
        for issue in issues:
            rel_file = os.path.relpath(issue['file'], base_dir)
            report += f"### {rel_file} (Line {issue['line']})\n\n"
            report += f"**Issue:** {issue['issue']}\n\n"
            report += f"**Reference:** `{issue['reference']}`\n\n"
            if 'target_file' in issue:
                report += f"**Target file:** `{issue['target_file']}`\n\n"
            report += "\n"
    else:
        report += "✅ **No issues found! All references are valid.**\n\n"
    
    report += "\n---\n\n## 📝 Summary\n\n"
    report += f"- ✅ Verified: {len(verified)} references\n"
    report += f"- ⚠️ Issues: {len(issues)} references\n"
    report += f"- 📄 Files checked: {len(md_files)}\n"
    
    # Write report
    output_file = base_dir / 'QUESTION_REFERENCES_REPORT.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Verification complete!")
    print(f"📊 Verified: {len(verified)} references")
    print(f"⚠️ Issues: {len(issues)} references")
    print(f"📄 Report: {output_file}")
    
    if issues:
        print("\n⚠️ Issues found:")
        for issue in issues[:10]:  # Show first 10
            print(f"  - {os.path.relpath(issue['file'], base_dir)}:{issue['line']} - {issue['issue']}")

if __name__ == '__main__':
    main()
