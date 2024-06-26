import re

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'

def markdown_to_blocks(markdown):
    pattern = '\n\n'
    split_list = markdown.split(pattern)
    filtered_list = []
    for block in split_list:
        if block == '':
            continue
        block = block.strip()
        filtered_list.append(block)
    return filtered_list

def is_ordered_list(text):
    lines = text.split('\n')
    current_number = 1
    for line in lines:
        if not re.match(r'^\d+\.\s', line):
            return False
        number = int(re.match(r'^(\d+)\.\s', line).group(1))
        if number != current_number:
            return False
        current_number += 1
    return True

def block_to_block_type(markdown_block):
    block_split_lines = markdown_block.splitlines()
    quote_start = all(line.startswith('>') for line in block_split_lines)
    unordered_list_start = all(line.startswith('* ') or line.startswith('- ') for line in block_split_lines)
    ordered_list_start = is_ordered_list(markdown_block)
    if markdown_block[0] == '#':
        return block_type_heading
    elif markdown_block[:3] == '```' and markdown_block[-3:] == '```':
        return block_type_code
    elif quote_start:
        return block_type_quote
    elif unordered_list_start:
        return block_type_unordered_list
    elif ordered_list_start:
        return block_type_ordered_list
    else:
        return block_type_paragraph

test = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""

test_func = markdown_to_blocks(test)
print(test_func)