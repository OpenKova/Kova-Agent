import re, os

repo = r"C:\Users\chira\KovaAgent"

replacements = {
    "README.zh-CN.md": [
        ("# Hermes Agent \u2624", "# Kova Agent"),
        ("Hermes Agent", "Kova Agent"),
        ("Kova", "Kova"),
        ("kova.ai", "kova.ai"),
    ],
    "README.es.md": [
        ("# Hermes Agent \u2624", "# Kova Agent"),
        ("Hermes Agent", "Kova Agent"),
        ("Kova", "Kova"),
        ("kova.ai", "kova.ai"),
    ],
    "README.ur-pk.md": [
        ("Hermes Agent", "Kova Agent"),
        ("Kova", "Kova"),
        ("kova.ai", "kova.ai"),
    ],
    "SECURITY.md": [
        ("# Hermes Agent Security Policy", "# Kova Agent Security Policy"),
        ("Hermes Agent's", "Kova Agent's"),
        ("Hermes Agent", "Kova Agent"),
    ],
    "SECURITY.es.md": [
        ("# Pol\u00edtica de Seguridad de Hermes Agent", "# Pol\u00edtica de Seguridad de Kova Agent"),
        ("Hermes Agent's", "Kova Agent's"),
        ("Hermes Agent", "Kova Agent"),
    ],
    "CONTRIBUTING.md": [
        ("Kova Discord", "Kova Discord"),
        ("kova.ai", "kova.ai"),
        ("Kova", "Kova"),
    ],
    "CONTRIBUTING.es.md": [
        ("Discord de Kova", "Discord de Kova"),
        ("Kova Discord", "Kova Discord"),
    ],
    os.path.join(".github", "ISSUE_TEMPLATE", "config.yml"): [
        ("Kova Discord", "Kova Discord"),
    ],
    os.path.join(".github", "ISSUE_TEMPLATE", "setup_help.yml"): [
        ("Kova Discord", "Kova Discord"),
    ],
    "pyproject.toml": [
        ('authors = [{ name = "Kova" }]', 'authors = [{ name = "Kova" }]'),
    ],
    "setup.py": [
        ("Hermes Agent", "Kova Agent"),
    ],
    "setup-hermes.sh": [
        ("# Hermes Agent Setup Script", "# Kova Agent Setup Script"),
    ],
    os.path.join("website", "scripts", "generate-llms-txt.py"): [
        ('"# Hermes Agent"', '"# Kova Agent"'),
        ("Hermes Agent", "Kova Agent"),
        ("Kova", "Kova"),
    ],
    os.path.join("website", "scripts", "generate-skill-docs.py"): [
        ("Hermes Agent", "Kova Agent"),
    ],
    os.path.join("agent", "anthropic_adapter.py"): [
        ('"""Anthropic Messages API adapter for Hermes Agent.', '"""Anthropic Messages API adapter for Kova Agent.'),
    ],
    os.path.join("agent", "bedrock_adapter.py"): [
        ('"""AWS Bedrock Converse API adapter for Hermes Agent.', '"""AWS Bedrock Converse API adapter for Kova Agent.'),
    ],
    os.path.join("agent", "insights.py"): [
        ('"""Session Insights Engine for Hermes Agent.', '"""Session Insights Engine for Kova Agent.'),
        ("Hermes Agent's", "Kova Agent's"),
    ],
    os.path.join("agent", "model_metadata.py"): [
        ("Hermes Agent.", "Kova Agent."),
    ],
    os.path.join("agent", "portal_tags.py"): [
        ("Hermes Agent", "Kova Agent"),
        ("Nous", "Kova"),
    ],
    os.path.join("agent", "plugin_llm.py"): [
        ("Hermes Agent", "Kova Agent"),
    ],
    os.path.join("agent", "lsp", "__init__.py"): [
        ('"""Language Server Protocol (LSP) integration for Hermes Agent.', '"""Language Server Protocol (LSP) integration for Kova Agent.'),
    ],
    os.path.join("cron", "__init__.py"): [
        ('"""Cron job scheduling system for Hermes Agent.', '"""Cron job scheduling system for Kova Agent.'),
    ],
    os.path.join("gateway", "platforms", "whatsapp_common.py"): [
        ('"\\u2695 *Hermes Agent*\\n', '"\\u2695 *Kova Agent*\\n'),
    ],
    os.path.join("gateway", "platforms", "weixin.py"): [
        ("Hermes Agent", "Kova Agent"),
    ],
    os.path.join("gateway", "platforms", "api_server.py"): [
        ("Hermes Agent", "Kova Agent"),
    ],
    os.path.join("gateway", "slash_commands.py"): [
        ("Hermes Agent version.", "Kova Agent version."),
        ("update Hermes Agent", "update Kova Agent"),
        ("Hermes Agent to the latest", "Kova Agent to the latest"),
        ("update Hermes Agent", "update Kova Agent"),
    ],
    os.path.join("acp_adapter", "entry.py"): [
        ("Hermes Agent", "Kova Agent"),
    ],
    os.path.join("acp_adapter", "server.py"): [
        ('"""ACP agent server \u2014 exposes Hermes Agent via the Agent Client Protocol."""', '"""ACP agent server \u2014 exposes Kova Agent via the Agent Client Protocol."""'),
        ('f"Hermes Agent v{HERMES_VERSION}"', 'f"Kova Agent v{HERMES_VERSION}"'),
    ],
    os.path.join("docs", "billing-lifecycle.md"): [
        ("Hermes Agent page.", "Kova Agent page."),
        ("Hermes Agent page`", "Kova Agent page`"),
    ],
    "cli.py": [
        ("Kova Hermes", "Kova"),
        ("Hermes models", "models"),
    ],
    os.path.join("hermes_cli", "main.py"): [
        ("Hermes Desktop", "Kova Desktop"),
        ("Hermes.exe", "Kova.exe"),
    ],
    os.path.join("kova_cli", "main.py"): [
        ("Hermes.exe", "Kova.exe"),
    ],
}

# Add remaining hermes-files references
for root, dirs, files in os.walk(repo):
    for fname in files:
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, repo)
        if rel.startswith(".git") or rel.startswith("node_modules") or rel.startswith("target"):
            continue
        if rel in replacements:
            continue
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except:
            continue
        old = content
        # Only fix user-facing strings in certain file types
        ext = os.path.splitext(fname)[1]
        if ext not in (".md", ".py", ".rs", ".sh", ".ps1", ".html", ".yml", ".yaml", ".json", ".toml", ".ts", ".tsx"):
            continue
        # Skip binary/lock files
        if fname in ("package-lock.json", "uv.lock", "Cargo.lock"):
            continue
        # Skip files that are already in the replacements dict
        skip_patterns = [
            "AGENTS.md", ".plans", ".github/workflows", "CHANGELOG",
            "hermes_already_has", "gitignore", "pre-commit"
        ]
        if any(p in rel for p in skip_patterns):
            continue
        
        # Apply replacements
        content = content.replace("Kova", "Kova")
        content = content.replace("Kova", "Kova")
        content = content.replace("KOVA", "KOVA")
        content = content.replace("kova.ai", "kova.ai")
        content = content.replace("kova", "kova")
        
        if content != old:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  CLEANED: {rel}")

# Now apply the targeted replacements
count = 0
for rel_path, repls in replacements.items():
    fpath = os.path.join(repo, rel_path)
    if not os.path.exists(fpath):
        print(f"  SKIP (not found): {rel_path}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    old = content
    for pattern, replacement in repls:
        content = content.replace(pattern, replacement)
    if content != old:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  FIXED: {rel_path}")
        count += 1

print(f"\nFixed {count} files")
