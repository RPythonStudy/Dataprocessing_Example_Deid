import re

def reorder_prompts(input_path, output_path):
    print(f"Reading {input_path}...")
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Blocks start with a '-' at the beginning of a line
        # We'll split the content into blocks
        # Using a regex that looks for '-' at the start of a line
        blocks = re.split(r'^(?=- )', content, flags=re.MULTILINE)
        
        # Remove any empty leading block (if the file starts with a '-' it might be empty)
        blocks = [b.strip() for b in blocks if b.strip()]
        
        # Reverse the order of blocks
        reversed_blocks = blocks[::-1]
        
        # Reconstruct content
        new_content = "\n\n".join(reversed_blocks)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Reordered prompts saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reorder_prompts("prompts.md", "prompts-1.md")
