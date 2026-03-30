#!/usr/bin/env bash
# blog_image.sh — Upload and manage images for NEMA SWARM blog posts
#
# Usage:
#   ./scripts/blog_image.sh add <image_file> [optional_name]
#   ./scripts/blog_image.sh list
#   ./scripts/blog_image.sh remove <image_name>
#   ./scripts/blog_image.sh embed <image_name> [alt_text] [caption]
#
# Examples:
#   ./scripts/blog_image.sh add ~/Downloads/ego-dev-theory.png
#   ./scripts/blog_image.sh add ~/Downloads/photo.jpg daemon-dialogue
#   ./scripts/blog_image.sh list
#   ./scripts/blog_image.sh embed ego-dev-theory.png "Ego Development Theory diagram"
#   ./scripts/blog_image.sh embed ego-dev-theory.png "EDT diagram" "Source: Cook-Greuter"

set -euo pipefail

BLOG_IMAGES_DIR="$(cd "$(dirname "$0")/../docs/blog/images" && pwd)"
SUPPORTED_EXTENSIONS="png jpg jpeg gif svg webp"
MAX_SIZE_MB=5

usage() {
    cat <<'USAGE'
blog_image.sh — Upload and manage images for NEMA SWARM blog posts

Commands:
  add <image_file> [name]    Copy image to blog/images/ (optional rename)
  list                       List all images in blog/images/
  remove <image_name>        Remove an image from blog/images/
  embed <image_name> [alt] [caption]  Print markdown to embed in a blog post

Supported formats: png, jpg, jpeg, gif, svg, webp
Max file size: 5MB

Embedding in blog posts:
  After adding an image, use standard markdown in docs/blog/index.md:

    ![Alt text](images/my-image.png)

  Or with caption (using MkDocs Material figure syntax):

    <figure markdown="span">
      ![Alt text](images/my-image.png){ width="600" }
      <figcaption>Your caption here</figcaption>
    </figure>
USAGE
}

check_extension() {
    local file="$1"
    local ext="${file##*.}"
    ext="$(echo "$ext" | tr '[:upper:]' '[:lower:]')"
    for supported in $SUPPORTED_EXTENSIONS; do
        if [[ "$ext" == "$supported" ]]; then
            return 0
        fi
    done
    echo "Error: Unsupported file type '.$ext'"
    echo "Supported: $SUPPORTED_EXTENSIONS"
    return 1
}

check_size() {
    local file="$1"
    local size
    size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null)
    local max_bytes=$((MAX_SIZE_MB * 1024 * 1024))
    if [[ "$size" -gt "$max_bytes" ]]; then
        echo "Error: File is $(( size / 1024 / 1024 ))MB, max is ${MAX_SIZE_MB}MB"
        echo "Consider compressing the image before adding."
        return 1
    fi
}

cmd_add() {
    local src="${1:-}"
    local name="${2:-}"

    if [[ -z "$src" ]]; then
        echo "Error: No image file specified"
        echo "Usage: blog_image.sh add <image_file> [name]"
        return 1
    fi

    if [[ ! -f "$src" ]]; then
        echo "Error: File not found: $src"
        return 1
    fi

    check_extension "$src"
    check_size "$src"

    local ext="${src##*.}"
    ext="$(echo "$ext" | tr '[:upper:]' '[:lower:]')"

    if [[ -n "$name" ]]; then
        # Add extension if name doesn't have one
        if [[ "$name" != *.* ]]; then
            name="${name}.${ext}"
        fi
    else
        name="$(basename "$src")"
    fi

    # Sanitize filename: lowercase, replace spaces with hyphens
    name="$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')"

    local dest="${BLOG_IMAGES_DIR}/${name}"

    if [[ -f "$dest" ]]; then
        echo "Warning: Image '${name}' already exists. Overwrite? [y/N]"
        read -r confirm
        if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
            echo "Aborted."
            return 1
        fi
    fi

    cp "$src" "$dest"
    echo "Added: docs/blog/images/${name}"
    echo ""
    echo "To embed in a blog post, add this markdown:"
    echo ""
    echo "  ![${name%.*}](images/${name})"
    echo ""
    echo "Or with caption:"
    echo ""
    echo "  <figure markdown=\"span\">"
    echo "    ![${name%.*}](images/${name}){ width=\"600\" }"
    echo "    <figcaption>Your caption here</figcaption>"
    echo "  </figure>"
}

cmd_list() {
    echo "Blog images in docs/blog/images/:"
    echo ""
    local count=0
    for f in "${BLOG_IMAGES_DIR}"/*; do
        local basename
        basename="$(basename "$f")"
        if [[ "$basename" == ".gitkeep" ]]; then
            continue
        fi
        if [[ -f "$f" ]]; then
            local size
            size=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null)
            local size_kb=$(( size / 1024 ))
            echo "  ${basename}  (${size_kb}KB)"
            count=$((count + 1))
        fi
    done
    if [[ "$count" -eq 0 ]]; then
        echo "  (no images yet)"
    fi
    echo ""
    echo "Total: ${count} image(s)"
}

cmd_remove() {
    local name="${1:-}"
    if [[ -z "$name" ]]; then
        echo "Error: No image name specified"
        echo "Usage: blog_image.sh remove <image_name>"
        return 1
    fi

    local target="${BLOG_IMAGES_DIR}/${name}"
    if [[ ! -f "$target" ]]; then
        echo "Error: Image not found: ${name}"
        echo "Run 'blog_image.sh list' to see available images."
        return 1
    fi

    echo "Remove docs/blog/images/${name}? [y/N]"
    read -r confirm
    if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
        echo "Aborted."
        return 1
    fi

    rm "$target"
    echo "Removed: docs/blog/images/${name}"
    echo ""
    echo "Note: Remember to remove any references to this image in blog posts."
}

cmd_embed() {
    local name="${1:-}"
    local alt="${2:-${name%.*}}"
    local caption="${3:-}"

    if [[ -z "$name" ]]; then
        echo "Error: No image name specified"
        echo "Usage: blog_image.sh embed <image_name> [alt_text] [caption]"
        return 1
    fi

    local target="${BLOG_IMAGES_DIR}/${name}"
    if [[ ! -f "$target" ]]; then
        echo "Warning: Image '${name}' not found in docs/blog/images/"
        echo "The markdown will still be generated, but the image won't render."
        echo ""
    fi

    if [[ -n "$caption" ]]; then
        cat <<EOF

<figure markdown="span">
  ![${alt}](images/${name}){ width="600" }
  <figcaption>${caption}</figcaption>
</figure>

EOF
    else
        echo ""
        echo "![${alt}](images/${name})"
        echo ""
    fi
}

# Main
case "${1:-}" in
    add)    shift; cmd_add "$@" ;;
    list)   cmd_list ;;
    remove) shift; cmd_remove "$@" ;;
    embed)  shift; cmd_embed "$@" ;;
    -h|--help|help) usage ;;
    *)
        usage
        exit 1
        ;;
esac
