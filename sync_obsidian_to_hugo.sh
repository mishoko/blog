#!/bin/bash

# Ensure environment variables are set
if [ -z "$OBSIDIAN_DIR" ] || [ -z "$HUGO_POSTS_DIR" ] || [ -z "$ATTACHMENTS_DIR" ] || [ -z "$STATIC_IMAGES_DIR" ]; then
  echo "Environment variables OBSIDIAN_DIR, HUGO_POSTS_DIR, ATTACHMENTS_DIR, and STATIC_IMAGES_DIR must be set."
  exit 1
fi

# sync files from Obsidian to Hugo posts directory
rsync -av --exclude='.*' "$OBSIDIAN_DIR/" "$HUGO_POSTS_DIR/"

echo "Files synced from $OBSIDIAN_DIR to $HUGO_POSTS_DIR"

# port the needed images
python3 import-images.py

echo "Images ported from $ATTACHMENTS_DIR to $STATIC_IMAGES_DIR"