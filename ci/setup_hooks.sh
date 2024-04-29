#!/bin/bash

# Setup Git hooks.
REPO_HOOKS_DIR=$(git rev-parse --show-toplevel)/git_hooks
GIT_HOOKS_DIR=$(git rev-parse --git-dir)/hooks

# Create the hooks directory if it doesn't exist.
mkdir -p $GIT_HOOKS_DIR

# Link each script from the git_hooks directory to the .git/hooks directory and make them executable.
for hook in $REPO_HOOKS_DIR/*; do
    hook_name=$(basename $hook)
    ln -sf $hook $GIT_HOOKS_DIR/$hook_name
    chmod +x $GIT_HOOKS_DIR/$hook_name
    echo "Linked and set executable: $hook_name"
done

echo "Git hooks set up successfully."
