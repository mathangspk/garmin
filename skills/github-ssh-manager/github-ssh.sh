#!/bin/bash
# GitHub SSH Manager Utility Script

SKILL_DIR="/home/node/.openclaw/workspace/boma/skills/github-ssh-manager"
SSH_KEY="$SKILL_DIR/ssh_key"
SSH_PUB_KEY="$SKILL_DIR/ssh_key.pub"

export GIT_SSH_COMMAND="ssh -i $SSH_KEY -o StrictHostKeyChecking=no"

case "$1" in
    "generate-key")
        ssh-keygen -t ed25519 -C "boma-openclaw@github" -f "$SSH_KEY" -N ""
        chmod 600 "$SSH_KEY"
        echo "✅ SSH key generated: $SSH_KEY"
        ;;
    "show-public-key")
        if [ -f "$SSH_PUB_KEY" ]; then
            echo "📋 Public Key for GitHub:"
            cat "$SSH_PUB_KEY"
            echo ""
            echo "ℹ️ Add this to GitHub: Settings → SSH and GPG keys → New SSH key"
        else
            echo "❌ Public key not found. Run 'generate-key' first."
        fi
        ;;
    "test-connection")
        ssh -T -i "$SSH_KEY" git@github.com
        ;;
    "clone")
        if [ -z "$2" ]; then
            echo "❌ Usage: clone <username/repo>"
            exit 1
        fi
        git clone "git@github.com:$2.git"
        ;;
    "push")
        if [ -z "$2" ]; then
            echo "❌ Usage: push \"commit message\""
            exit 1
        fi
        git add .
        git commit -m "$2"
        git push origin HEAD
        ;;
    "pull")
        git pull origin HEAD
        ;;
    *)
        echo "GitHub SSH Manager Commands:"
        echo "  generate-key       - Generate new SSH key pair"
        echo "  show-public-key    - Show public key for GitHub setup"
        echo "  test-connection    - Test SSH connection to GitHub"
        echo "  clone <repo>       - Clone repository (user/repo)"
        echo "  push \"message\"    - Commit and push changes"
        echo "  pull              - Pull latest changes"
        ;;
esac