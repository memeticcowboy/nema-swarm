#!/bin/bash
# Blog Image Management Script
# Usage: ./blog_image.sh add <path> [name] | list | embed <name> <alt> [caption] | remove <name>

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
IMAGES_DIR="$WORKSPACE_DIR/docs/blog/images"

mkdir -p "$IMAGES_DIR"

sanitize_filename() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9.-'
}

cmd_add() {
    local src_path="$1"
    local custom_name="$2"
    
    if [[ -z "$src_path" ]]; then
        echo "Error: No source path provided"
        exit 1
    fi
    
    if [[ ! -f "$src_path" ]]; then
        echo "Error: File not found: $src_path"
        exit 1
    fi
    
    # Get file extension
    ext="${src_path##*.}"
    ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
    
    # Validate extension
    if [[ ! "$ext_lower" =~ ^(png|jpg|jpeg|gif|svg|webp)$ ]]; then
        echo "Error: Unsupported format: $ext"
        echo "Supported: png, jpg, jpeg, gif, svg, webp"
        exit 1
    fi
    
    # Determine filename
    if [[ -n "$custom_name" ]]; then
        base_name="$(sanitize_filename "$custom_name")"
        filename="${base_name}.${ext_lower}"
    else
        filename="$(basename "$src_path" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')"
    fi
    
    dest_path="$IMAGES_DIR/$filename"
    
    # Check file size (5MB = 5242880 bytes)
    filesize=$(stat -f%z "$src_path" 2>/dev/null || stat -c%s "$src_path" 2>/dev/null)
    if [[ $filesize -gt 5242880 ]]; then
        echo "Error: File too large ($filesize bytes). Max: 5MB"
        exit 1
    fi
    
    cp "$src_path" "$dest_path"
    echo "Added: $filename → docs/blog/images/"
    echo "Embed markdown:"
    echo "![Alt text](images/$filename)"
}

cmd_list() {
    if [[ ! -d "$IMAGES_DIR" ]]; then
        echo "No images directory"
        exit 0
    fi
    
    echo "Blog images in docs/blog/images/:"
    ls -la "$IMAGES_DIR" | tail -n +2
}

cmd_embed() {
    local name="$1"
    local alt="$2"
    local caption="$3"
    
    if [[ -z "$name" ]]; then
        echo "Usage: embed <filename> <alt-text> [caption]"
        exit 1
    fi
    
    if [[ -z "$alt" ]]; then
        alt="Image"
    fi
    
    if [[ -n "$caption" ]]; then
        echo "<figure markdown=\"span\">"
        echo "  ![${alt}](images/${name}){ width=\"600\" }"
        echo "  <figcaption>${caption}</figcaption>"
        echo "</figure>"
    else
        echo "![${alt}](images/${name}){ width=\"600\" }"
    fi
}

cmd_remove() {
    local name="$1"
    if [[ -z "$name" ]]; then
        echo "Error: No filename provided"
        exit 1
    fi
    
    rm -f "$IMAGES_DIR/$name"
    echo "Removed: $name"
}

# Main command dispatch
case "${1:-}" in
    add)
        shift
        cmd_add "$@"
        ;;
    list)
        cmd_list
        ;;
    embed)
        shift
        cmd_embed "$@"
        ;;
    remove)
        shift
        cmd_remove "$@"
        ;;
    *)
        echo "Usage: $0 {add|list|embed|remove} [args...]"
        echo ""
        echo "Commands:"
        echo "  add <path> [name]     - Add an image to the blog"
        echo "  list                  - List all uploaded images"
        echo "  embed <name> <alt> [caption] - Generate embed markdown"
        echo "  remove <name>         - Remove an image"
        exit 1
        ;;
esac
