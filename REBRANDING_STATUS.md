# Kova Agent — Rebranding Status

## Completed ✓

### Core branding
- All source code references to CLI commands (`hermes` → `kova`, `hermes-agent` → `kova-agent`, `hermes-acp` → `kova-acp`)
- CLI ASCII art logo → "KOVA"
- Banner text → "KOVA" / "Kova Agent"
- All Python module namespaces (`hermes_cli` kept as-is for backward compat)
- CSS class names (`hermes-fade-in` → `kova-fade-in`)
- PATH and env var names (`HERMES_HOME` backward compat retained)
- Config file paths

### Desktop app
- `intro.tsx` WORDMARK → "KOVA"
- `intro-copy.jsonl` → "Kova is ready."
- Slash command → "Show Kova version"
- Install overlay comment → "no Kova installed"
- About settings release notes URL → `OpenKova/Kova-Agent`
- Onboarding docs URL → `OpenKova/Kova-Agent`
- Window title → "Kova"
- Uninstall section heading → "Uninstall Kova"
- Brand logo images replaced across the entire repo (PNG, ICO, JPG)
- `_desktop_packaged_executable` → looks for `Kova.exe`/`Kova.app`

### Bootstrap installer (Tauri)
- All UI text → "Kova" (welcome, progress, success screens)
- `tauri.conf.json` → `productName: "Kova"`, `identifier: "com.kovaai.kova.setup"`
- Rust code → `Kova.exe`, `Kova-Setup.exe`, `force_kill_other_kova()`
- Brand mark (`nous-girl.jpg`) → replaced with Kova logo

### Install scripts
- `install.ps1` → Kova Agent Installer, Kova.exe candidates, OpenKova/Kova-Agent URLs
- `install.sh` → Kova Agent Installer, Kova.exe candidates, OpenKova/Kova-Agent URLs
- `install_script.rs` → download URL OpenKova/Kova-Agent

### Website
- `assets/banner.png` → replaced with Kova logo
- All favicons (PNG + ICO) → replaced with Kova logo
- `logo.png`, `nous-logo.png`, `hermes-agent-banner.png` → replaced with Kova logo

### Git history
- Clean single-parent history on `OpenKova/Kova-Agent`
- No Hermes/Nous mentions in commit messages

---

## 🔴 High Priority — User-Facing Text

These are things real users see in the product. Fix these first.

### CLI / Agent Identity

| File | What to change |
|------|----------------|
| `kova_cli/default_soul.py:4` | "created by Nous Research" → "created by Kova" |
| `hermes_cli/default_soul.py:25,45` | "Hermes Agent Persona" template comment |
| `cli.py:6593` | "Nous Research Hermes models are NOT agentic" → remove "Nous Research" |
| `kova_cli/model_switch.py:182` | "Nous Research Hermes 3 & 4 models are NOT agentic" → remove "Nous Research" |
| `acp_adapter/entry.py:119` | "Run Hermes Agent as an ACP stdio server" → "Kova Agent" |
| `acp_adapter/server.py:2133` | `"Hermes Agent v{VERSION}"` → `"Kova Agent v{VERSION}"` |

### Gateway / Platform Messages

| File | What to change |
|------|----------------|
| `gateway/platforms/whatsapp_common.py:57` | `"⚕ *Hermes Agent*"` reply prefix → `"⚕ *Kova Agent*"` |
| `gateway/slash_commands.py:1348` | "show the running Hermes Agent version" → "Kova Agent" |
| `gateway/slash_commands.py:4870,4898` | "update Hermes Agent" → "update Kova Agent" |
| `gateway/platforms/api_server.py:99` | "Hermes Agent version string" docstring |
| `gateway/platforms/weixin.py:4` | "Connects Hermes Agent to WeChat" → "Kova Agent" |

### Desktop App

| File | What to change |
|------|----------------|
| `apps/desktop/electron/main.ts:3601` | "Hermes Agent not installed yet" → "Kova Agent" |
| `apps/desktop/src/app/settings/uninstall-section.tsx:24,31,32,39` | "the Hermes agent" → "the Kova agent" in descriptions |
| `apps/desktop/src/app/settings/constants.ts:45` | `docsUrl: 'https://portal.nousresearch.com'` → Kova URL |
| `apps/desktop/src/app/settings/gateway-settings.tsx:1184` | `portal.nousresearch.com` link |
| `apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx:32` | `portal.nousresearch.com` link |
| `apps/desktop/src/i18n/en.ts:696` | `hermes-agent.nousresearch.com/install.sh` URL |
| `apps/desktop/src/i18n/ja.ts:777` | same URL |
| `apps/desktop/src/i18n/zh.ts:899` | same URL |
| `apps/desktop/src/i18n/zh-hant.ts:755` | same URL |

### README Files

| File | What to change |
|------|----------------|
| `README.zh-CN.md` | Title "Hermes Agent ☤", "Built by Nous Research", URLs |
| `README.es.md` | Title "Hermes Agent ☤", "Creado por Nous Research", URLs |
| `README.ur-pk.md` | Title, "Built by Nous Research", URLs |
| `SECURITY.md` | "Hermes Agent Security Policy" throughout |
| `SECURITY.es.md` | "Política de Seguridad de Hermes Agent" throughout |
| `CONTRIBUTING.md` | "Nous Research Discord" → "Kova Discord", URLs |
| `CONTRIBUTING.es.md` | "Discord de Nous Research" → "Discord de Kova" |
| `setup.py` | "Hermes Agent" pip description |

### Package / Project Metadata

| File | What to change |
|------|----------------|
| `pyproject.toml:4` | `name = "hermes-agent"` — changes pip package name |
| `pyproject.toml:16` | `authors = [{ name = "Nous Research" }]` → `"Kova"` |
| `pyproject.toml:230-246` | `hermes-agent[cli]`, `hermes-agent[cron]` etc. extras |
| `.github/ISSUE_TEMPLATE/config.yml` | "Nous Research Discord" |
| `.github/ISSUE_TEMPLATE/setup_help.yml` | "Nous Research Discord" link |

### Billing / Account

| File | What to change |
|------|----------------|
| `kova_cli/cli_billing_mixin.py:1112,1482` | "allow Nous Research to charge your card" → "allow Kova" |

### ALL Plugin Manifests (44 files)

| Pattern | What to change |
|---------|----------------|
| `plugins/platforms/*/plugin.yaml:6` | `description: "..." — "Hermes Agent" → "Kova Agent"` |
| `plugins/model-providers/*/plugin.yaml:5` | `author: Nous Research` → `author: Kova` |
| `plugins/*/plugin.yaml` | Various `author: Nous Research` fields |

### SKILL.md Author Frontmatter (76 files)

| Pattern | What to change |
|---------|----------------|
| `skills/*/SKILL.md` and `optional-skills/*/SKILL.md` | `author: Hermes Agent` → `author: Kova Agent` |
| Files with `author: Hermes Agent (Nous Research)` | → `author: Kova Agent` |

### Web Dashboard (all 16 i18n files)

| File | What to change |
|------|----------------|
| `web/src/i18n/en.ts` | "Hermes Gateway", "Update Hermes", "Hermes Plugins", "Hermes Achievements", "Hermes Console" |
| `web/src/i18n/es.ts` | Same pattern in Spanish |
| `web/src/i18n/fr.ts` | Same pattern in French |
| `web/src/i18n/de.ts` | Same pattern in German |
| `web/src/i18n/ja.ts` | Same pattern in Japanese |
| `web/src/i18n/zh.ts` | Same pattern in Chinese |
| `web/src/i18n/zh-hant.ts` | Same pattern in Traditional Chinese |
| `web/src/i18n/af.ts` | Same pattern in Afrikaans |
| `web/src/i18n/ga.ts` | Same pattern in Irish |
| `web/src/i18n/hu.ts` | Same pattern in Hungarian |
| `web/src/i18n/it.ts` | Same pattern in Italian |
| `web/src/i18n/ko.ts` | Same pattern in Korean |
| `web/src/i18n/pt.ts` | Same pattern in Portuguese |
| `web/src/i18n/ru.ts` | Same pattern in Russian |
| `web/src/i18n/tr.ts` | Same pattern in Turkish |
| `web/src/i18n/uk.ts` | Same pattern in Ukrainian |

### Web Dashboard Components

| File | What to change |
|------|----------------|
| `web/src/themes/presets.ts:43-44` | `"Hermes Teal"` theme name |
| `web/src/components/HermesConsoleModal.tsx` | Component name, "Hermes Console" title, "hermes>" prompt |
| `web/src/components/SidebarFooter.tsx:24` | `nousresearch.com` link |
| `web/src/i18n/*.ts` | "Hermes" in ~20+ user-facing strings per locale |

### ALL Locale YAML Files (16 files)

| Pattern | What to change |
|---------|----------------|
| `locales/*.yaml` | "Hermes Commands", "Hermes team", "Hermes Gateway Status", "Restarting gateway" |

### Gateway Platform Adapters (User-Facing Defaults)

| File | What to change |
|------|----------------|
| `plugins/google_meet/*.py` | `guest_name: str = "Hermes Agent"` default |
| `plugins/platforms/email/adapter.py:934,1048,1128,1222` | `subject = "Hermes Agent"` |
| `plugins/platforms/irc/adapter.py:196,234,803` | `":Hermes Agent"` as IRC realname/quit |
| `plugins/platforms/matrix/adapter.py:1323` | `device_name="Hermes Agent"` |
| `plugins/platforms/discord/adapter.py:5107` | `"Update Hermes Agent"` slash command |
| `plugins/platforms/homeassistant/adapter.py:406` | `"title": "Hermes Agent"` |
| `plugins/platforms/photon/cli.py:48,144` | `"Project name (default: 'Hermes Agent')"` |
| `plugins/dashboard_auth/nous/__init__.py:157,634` | `display_name = "Nous Research"` |

### Install Scripts

| File | What to change |
|------|----------------|
| `scripts/install.sh:3,1821` | "Hermes Agent Setup Script", agent identity "created by Nous Research" |

---

## 🟡 Medium Priority — Website & Docs

### Docusaurus Configuration

| File | What to change |
|------|----------------|
| `website/docusaurus.config.ts:10,13,14` | `url: 'https://hermes-agent.nousresearch.com'` |
| `website/docusaurus.config.ts:107` | `organizationName: 'NousResearch'` |
| `website/docusaurus.config.ts:148` | `projectName: 'hermes-agent'` |
| `website/docusaurus.config.ts:157,162,167,188,196-198,202` | Footer links, copyright |

### Website Scripts

| File | What to change |
|------|----------------|
| `website/scripts/generate-llms-txt.py` | "# Hermes Agent" header, "Nous Research" references |
| `website/scripts/generate-skill-docs.py:475` | `"ship with Hermes Agent"` description |

### Website React Pages

| File | What to change |
|------|----------------|
| `website/src/pages/skills/index.tsx:645,651` | "Browse all skills for Hermes Agent" |
| `website/src/components/UserStoriesCollage/index.tsx:177,306` | "What the Hermes Agent community is building" |
| `website/src/data/userStories.json` | ~50+ user-submitted quotes mentioning "Hermes Agent" (may keep as-is) |
| `website/src/css/custom.css:2` | "/* Hermes Agent — Custom Docusaurus Theme */" |

### Website English Docs

| File | What to change |
|------|----------------|
| `website/docs/getting-started/installation.md` | Install URLs (`hermes-agent.nousresearch.com`) |
| `website/docs/getting-started/quickstart.md` | Same URLs |
| `website/docs/getting-started/platform-support.md` | "Hermes Desktop" references |
| `website/docs/getting-started/termux.md` | Install URL |
| `website/docs/developer-guide/prompt-assembly.md:50` | **"You are Hermes, an AI assistant created by Nous Research"** (agent identity!) |
| `website/docs/developer-guide/prompt-assembly.md:177` | "created by Nous Research" |
| `website/docs/developer-guide/contributing.md:52` | Install URL |
| `website/docs/developer-guide/plugins/index.md:42` | NousResearch/hermes-agent, Nous Research Discord |
| `website/docs/reference/faq.md` | Nous Research, Nous Portal, Nous Research Discord |
| `website/docs/reference/model-catalog.md` | Install URLs |
| `website/docs/integrations/nous-portal.md` | "Nous Research's unified subscription", "Hermes 4" |
| `website/docs/integrations/providers.md:65` | "Nous Research's unified subscription" |
| `website/docs/guides/run-nemotron-3-ultra-free.md` | "Nous Research has been inducted" |
| `website/docs/guides/run-hermes-with-nous-portal.md` | Filename + content |
| `website/docs/user-guide/desktop.md` | Install URLs, "Sign in with Nous Research" |
| `website/docs/user-guide/features/web-dashboard.md` | "Default provider: Nous Research", "Sign in with Nous Research" |
| `website/docs/user-guide/features/personality.md:127` | "created by Nous Research" |
| `website/docs/user-guide/features/skills.md` | URLs |
| `website/docs/user-guide/secrets/index.md:50` | Nous Research Discord |
| `website/docs/user-guide/windows-wsl-quickstart.md:103` | Install URL |
| `website/docs/user-guide/windows-native.md:23,31` | Install URL |

### Website Chinese Docs (zh-Hans)

| Files | What to change |
|-------|----------------|
| `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/` | ~50+ files with Hermes Agent, Nous Research, Docker image references, install URLs |
| `getting-started/installation.md`, `quickstart.md` | Install URLs |
| `user-guide/docker.md` | `nousresearch/hermes-agent` Docker image references |
| `user-guide/cli.md` | "Hermes Agent" title/body |
| `user-guide/messaging/*.md` | "Hermes Agent" references |
| `integrates/nous-portal.md` | Nous Research references |
| `guides/run-hermes-with-nous-portal.md` | Full file |
| All SKILL docs in zh-Hans | `author: Hermes Agent` |

### Optional Skills

| File | What to change |
|------|----------------|
| `optional-skills/DESCRIPTION.md:3` | "maintained by Nous Research" |
| `optional-skills/migration/DESCRIPTION.md:2` | "into Hermes Agent" |
| `optional-skills/finance/stocks/scripts/stocks_client.py:3,676` | "Hermes Agent project" |
| `optional-skills/blockchain/solana/scripts/solana_client.py:3,646` | "Hermes Agent" |
| `optional-skills/blockchain/hyperliquid/scripts/hyperliquid_client.py:3,1537` | "Hermes Agent" |
| `optional-skills/blockchain/evm/scripts/evm_client.py:3` | "Hermes Agent project" |
| `optional-skills/productivity/canvas/scripts/canvas_api.py:2,130` | "Hermes Agent" |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py:5,2961` | "into Hermes Agent" |

### SKILL.md Body Text

| File | What to change |
|------|----------------|
| `skills/software-development/test-driven-development/SKILL.md:302` | "## Hermes Agent Integration" |
| `skills/software-development/systematic-debugging/SKILL.md:362` | "## Hermes Agent Integration" |
| `optional-skills/devops/hermes-s6-container-supervision/SKILL.md:26` | "Hermes Agent" |
| `optional-skills/mcp/mcp-oauth-remote-gateway/SKILL.md:184` | `"client_name": "Hermes Agent (manual OAuth)"` |
| `optional-skills/research/qmd/SKILL.md:223,257` | "Hermes Agent" |
| `optional-skills/mlops/obliteratus/SKILL.md:23` | "Hermes Agent's MIT license" |
| `optional-skills/security/web-pentest/templates/*.md` | "Hermes Agent" references |
| `optional-skills/research/osint-investigation/references/sources/gdelt.md:73` | "Nous Research" query example |

---

## 🟢 Low Priority — Internal Comments & Docstrings

These are developer-facing only. Fix when convenient.

| File | What to change |
|------|----------------|
| `agent/anthropic_adapter.py:1` | `"""Anthropic Messages API adapter for Hermes Agent."""` |
| `agent/bedrock_adapter.py:1` | `"""AWS Bedrock Converse API adapter for Hermes Agent."""` |
| `agent/insights.py:2,8` | `"""Session Insights Engine for Hermes Agent."""` |
| `agent/model_metadata.py:193` | "Minimum context length required to run Hermes Agent" |
| `agent/plugin_llm.py:5` | "Plugins built on Hermes Agent" |
| `agent/lsp/__init__.py:1` | `"""LSP integration for Hermes Agent."""` |
| `cron/__init__.py:2` | `"""Cron job scheduling system for Hermes Agent."""` |
| `gateway/__init__.py:4` | "connecting the Hermes agent" |
| `hermes_cli/debug.py:1` | `"""debug tools for Hermes Agent."""` |
| `hermes_cli/build_info.py:2` | "Baked-in build metadata for Hermes Agent." |
| `hermes_cli/auth.py:2` | "auth system for Hermes Agent." |
| `hermes_cli/fallback_cmd.py:6,131` | `hermes-agent.nousresearch.com` URL in comments |
| `web/src/index.css:46,144` | "/* Hermes Agent — Nous DS */" CSS comments |

### Function/variable names that say "Hermes" (NOT user-facing, backward-compat)

These should be KEPT as-is unless you want to break backward compatibility:
- `HERMES_HOME` env var
- `HERMES_DESKTOP_*` env vars
- Internal Python function names with `hermes_` prefix
- IPC channel names with `hermes`
- CSS class names in web dashboard

---

## 📊 Summary

| Priority | Count | Estimated effort |
|----------|-------|-----------------|
| 🔴 High | ~90 files | Several hours (many are mechanical find-replace) |
| 🟡 Medium | ~120+ files | Days (docs are verbose, zh-Hans is large) |
| 🟢 Low | ~20 files | ~30 min (pure find-replace) |
| **Total** | **~230+ files** | **Significant effort — prioritize batch by impact** |
