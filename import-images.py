import os
import re
import shutil
from pathlib import Path

# Define paths
attachments_dir = Path(os.getenv("ATTACHMENTS_DIR"))
static_images_dir = Path(os.getenv("STATIC_IMAGES_DIR"))
posts_dir = Path(os.getenv("OBSIDIAN_DIR"))

def verify_paths():
    """Verify all required paths exist."""
    if not attachments_dir.exists():
        print(f"Attachments directory not found: {attachments_dir}")
        return False
    if not posts_dir.exists():
        print(f"Posts directory not found: {posts_dir}")
        return False
    return True

def ensure_directories_exist():
    """Create destination directory if it doesn't exist."""
    static_images_dir.mkdir(parents=True, exist_ok=True)

def process_markdown_files():
    try:
        if not verify_paths():
            return
        ensure_directories_exist()
        # Match both Obsidian and standard markdown image patterns
        image_pattern = r'!?\[\[([^]]*\.(?:png|jpg|jpeg|gif))\]\]'
        for file_path in posts_dir.rglob("*.md"):
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read()
                    matches = re.finditer(image_pattern, content, re.IGNORECASE)
                    images = []
                    for match in matches:
                        img = match.group(1)
                        if img:
                            # URL encode spaces in filename
                            encoded_img = img.replace(' ', '%20')
                            images.append(encoded_img)
                            # Replace original image reference with URL encoded version
                            print(f"Processing {img.split(' ')[0]}")
                            description = img.split(' ')[0]
                            content = content.replace(f'![[{img}]]', f'![{description}](/images/{encoded_img})')
                    # Write updated content back
                    with open(file_path, "w", encoding='utf-8') as file:
                        file.write(content)
                    if images:
                        for image in images:
                            # For file operations, decode the URL encoding
                            decoded_img = image.replace('%20', ' ')
                            source_path = attachments_dir / decoded_img
                            dest_path = static_images_dir / decoded_img
                            if source_path.exists():
                                shutil.copy2(str(source_path), str(dest_path))
                                print(f"Copied {decoded_img}")
                            else:
                                print(f"Source image not found: {source_path}")
            except Exception as e:
                print(f"Error processing file: {str(e)}")
    except Exception as e:
        print(f"Process failed: {str(e)}")

if __name__ == "__main__":
    process_markdown_files()
