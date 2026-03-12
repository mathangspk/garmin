---
name: github-ssh-manager
description: "Manage GitHub SSH keys for persistent access across sessions. Handles key generation, GitHub configuration, and git operations with persistent SSH keys stored in skill directory."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔑",
        "category": "development",
        "tags": ["github", "ssh", "git", "authentication"]
      }
  }
---

# GitHub SSH Manager Skill

Persistent SSH key management for GitHub access across OpenClaw sessions.

## Features

- 🔑 **Persistent SSH Keys**: Keys stored in skill directory survive session resets
- 🔧 **Auto Configuration**: Automatic git SSH configuration
- 🌐 **GitHub Integration**: Ready-to-use GitHub operations
- 📁 **Workspace Safe**: Keys stored within workspace, not system-wide

## Setup

### First-time Setup

```bash
# Generate new SSH key pair
skill github-ssh-manager generate-key

# Add public key to GitHub
skill github-ssh-manager show-public-key
```

### GitHub Configuration

1. Copy the public key shown above
2. Go to GitHub Settings → SSH and GPG keys
3. Add new SSH key with name "OpenClaw BOMA"
4. Paste the public key and save

### Verify Connection

```bash
skill github-ssh-manager test-connection
```

## Usage

### Git Operations with Persistent Key

All git commands automatically use the persistent SSH key:

```bash
# Clone repositories
skill github-ssh-manager clone mathangspk/repo-name

# Push changes
skill github-ssh-manager push "commit message"

# Pull updates
skill github-ssh-manager pull
```

### Manual Git Commands

For manual git operations, use the exported environment:

```bash
# Export SSH command for manual use
export GIT_SSH_COMMAND="ssh -i /home/node/.openclaw/workspace/boma/skills/github-ssh-manager/ssh_key"

# Then use git normally
git clone git@github.com:mathangspk/repo.git
git push origin main
```

## File Structure

```
github-ssh-manager/
├── SKILL.md          # This documentation
├── ssh_key           # Private SSH key (secure)
├── ssh_key.pub       # Public SSH key
└── config.json       # Configuration (optional)
```

## Security Notes

- 🔒 Private key is stored with 600 permissions
- 📁 Keys are contained within workspace directory
- 🔄 Survives session resets but not workspace deletion
- ⚠️ Treat this workspace as secure - contains sensitive credentials

## Examples

### Clone a Repository

```bash
skill github-ssh-manager clone mathangspk/garmin
```

### Push Current Directory

```bash
# Navigate to your project
cd /path/to/project

# Add, commit, and push
skill github-ssh-manager push "Added new feature"
```

### Check GitHub Access

```bash
skill github-ssh-manager test-connection
```

## Troubleshooting

### Connection Issues

```bash
# Re-generate keys if needed
skill github-ssh-manager generate-key --force

# Re-add public key to GitHub if connection fails
skill github-ssh-manager show-public-key
```

### Permission Errors

```bash
# Fix permissions if needed
chmod 600 /home/node/.openclaw/workspace/boma/skills/github-ssh-manager/ssh_key
```

## API Reference

### generate-key
Generate new SSH key pair

### show-public-key
Display public key for GitHub configuration

### test-connection
Test SSH connection to GitHub

### clone <repo>
Clone repository using persistent SSH key

### push "<message>"
Commit and push changes from current directory

### pull
Pull latest changes from remote