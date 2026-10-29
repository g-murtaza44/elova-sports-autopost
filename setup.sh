#!/bin/bash
# Run from the engine checkout. Recreates the /home/claude layout the renderer expects.
set -e
E=$(pwd)
for d in playbook3 photos commons scripts; do rm -rf /home/claude/$d; ln -s $E/$d /home/claude/$d; done
mkdir -p /home/claude/fonts && cp $E/fonts/package.json /home/claude/fonts/ && (cd /home/claude/fonts && npm install --silent)
pip install --break-system-packages -q rembg onnxruntime pillow playwright >/dev/null 2>&1 || true
echo ready
