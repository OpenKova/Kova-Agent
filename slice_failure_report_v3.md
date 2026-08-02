# CI Failure Report v3 — run 30702578394 (head afa5b014)

Generated from `gh run view 30702578394 --log-failed`.

## 1. Overall job status

**Python slice 1/8 still green.** 7 slices failing (2-8), 2 Docker builds, review-label gate, 3 JS/TS desktop checks.

## 2. Python test slices

- **Python tests / Run tests slice 2/8**: 9 unique failing tests
- **Python tests / Run tests slice 3/8**: 47 unique failing tests
- **Python tests / Run tests slice 4/8**: 20 unique failing tests
- **Python tests / Run tests slice 5/8**: 29 unique failing tests
- **Python tests / Run tests slice 6/8**: 12 unique failing tests
- **Python tests / Run tests slice 7/8**: 18 unique failing tests
- **Python tests / Run tests slice 8/8**: 40 unique failing tests

**Total unique failing tests across slices: 175** (was 191 in run 30699981302, 280 in 30694412497)

## 3. Still-failing tests (deduped) + assertions


### Python tests / Run tests slice 4/8
- **Unique failing tests: 20**
- `FAILED tests/gateway/test_dingtalk.py::TestMentionPatterns::test_pattern_matches_text`
- `FAILED tests/gateway/test_dingtalk.py::TestShouldProcessMessage::test_group_accepted_when_text_matches_wake_word`
- `FAILED tests/gateway/test_email.py::TestImapIdExtensionForNetEase::test_connect_sends_imap_id_after_login`
- `FAILED tests/hermes_cli/test_dashboard_lifecycle_flags.py::TestDashboardStatus::test_status_no_processes`
- `FAILED tests/hermes_cli/test_dashboard_lifecycle_flags.py::TestDashboardStatus::test_status_with_processes`
- `FAILED tests/hermes_cli/test_dashboard_lifecycle_flags.py::TestDashboardStop::test_stop_when_nothing_running`
- `FAILED tests/hermes_cli/test_kanban_diagnostics.py::test_triage_aux_unavailable_fires_auto_decompose_off_points_at_specifier`
- `FAILED tests/hermes_cli/test_web_ui_build.py::TestBuildWebUIFlock::test_lock_file_is_gitignored`
- `FAILED tests/kova_cli/test_curator_recent_run_notice.py::test_prints_multiline_summary_with_rename_map`
- `FAILED tests/kova_cli/test_gateway_proc_fallback.py::TestProcFallback::test_detects_gateway_pid_via_proc`
- `FAILED tests/kova_cli/test_gateway_proc_fallback.py::TestProcFallback::test_detects_no_supervisor_restart_process_only_when_enabled`
- `FAILED tests/kova_cli/test_gateway_proc_fallback.py::TestProcFallback::test_falls_back_to_ps_when_proc_absent`
- `FAILED tests/kova_cli/test_gui_uninstall.py::test_userdata_dir_per_platform`
- `FAILED tests/kova_cli/test_gui_uninstall.py::test_userdata_dir_windows - Asse...`
- `FAILED tests/kova_cli/test_reasoning_effort_menu.py::test_reasoning_menu_orders_minimal_before_low`
- `FAILED tests/kova_cli/test_systemd_watchdog_unit.py::test_system_unit_reads_watchdog_from_target_home`
- `FAILED tests/kova_cli/test_update_fleet_restart_timeout.py::TestFleetRestartTimeoutIsolation::test_non_gateway_units_in_list_output_are_ignored`
- `FAILED tests/kova_cli/test_update_fleet_restart_timeout.py::TestFleetRestartTimeoutIsolation::test_process_errors_other_than_timeout_still_propagate`
- `FAILED tests/kova_cli/test_update_fleet_restart_timeout.py::TestFleetRestartTimeoutIsolation::test_timeout_on_middle_unit_continues_remaining_units`
- `FAILED tests/run_agent/test_run_agent.py::TestBuildApiKwargs::test_reasoning_sent_for_nous_route`

**Deduped assertion/error lines (17):**
- `E       AssertionError: 'kova-agent' not found in '("name" "hermes-agent" "version" "0.19.0" "vendor" "NousResearch" "support-email" "noreply@nousresearch.com")'`
- `E       AssertionError: assert '.web_ui_build.lock' in '\ufeff__pycache__/\n*.pyc\n*.pyo\n.pytest_cache/\nnode_modules/\nvenv/\n.venv/\ndist/\nbuild/\n*.egg-info/\n.env\n.en...nt.log\nerrors.log\ngateway.log\nkova.log\n*.swp\n*.swo\n*~\n.id`
- `E       AssertionError: assert '2 hermes dashboard process(es) running' in '2 kova dashboard process(es) running:\n    PID 12345\n    PID 12346\n'`
- `E       AssertionError: assert 'No hermes dashboard processes running' in 'No kova dashboard processes running.\n'`
- `E       AssertionError: assert 'Skill curator — last run' in '\nâ„¹ Skill curator â€” last run just now\n  auto: 1 marked stale; llm: consolidated 2 into 1\n  archived 2 skill(s):...  full report: kova curator status\n  (This message shows `
- `E       AssertionError: assert 'Type=notify' in '[Unit]\nDescription=Kova Agent Gateway - Messaging Platform Integration\nAfter=network-online.target\nWants=network-o...p_cleanup\nTimeoutStopSec=60\nStandardOutput=journal\nStandardError=jou`
- `E       AssertionError: assert False is True`
- `E       AssertionError: assert PosixPath('/home/tester/Library/Application Support/Kova') == (((PosixPath('/home/tester') / 'Library') / 'Application Support') / 'Hermes')`
- `E       AssertionError: assert PosixPath('C:\\Users\\tester\\AppData\\Roaming/Kova') == (PosixPath('C:\\Users\\tester\\AppData\\Roaming') / 'Hermes')`
- `E       AssertionError: assert ['hermes-gate...eway-xiaomo7'] == ['hermes-gate...xiaomo7', ...]`
- `E       AssertionError: assert ['minimal', '... use', 'high'] == ['minimal', '... use', 'high']`
- `E       AssertionError: assert [] == ['kova-gateway-coder']`
- `E       Failed: DID NOT RAISE <class 'RuntimeError'>`
- `E       KeyError: 'reasoning'`
- `E       assert 12345 in []`
- `E       assert False`
- `E       assert [] == [12345]`

### Python tests / Run tests slice 6/8
- **Unique failing tests: 12**
- `FAILED tests/gateway/test_slack_mention.py::test_mention_patterns_single_string`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_agent_is_installed_detects_source_and_venv`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_agent_is_installed_venv_only`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_gui_install_summary_shape`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_run_uninstall_yes_keep_data_is_non_interactive`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_uninstall_gui_removes_only_gui_artifacts`
- `FAILED tests/hermes_cli/test_gui_uninstall.py::test_uninstall_module_main_gui_mode`
- `FAILED tests/kova_cli/test_codex_models.py::TestNormalizeModelForProvider::test_default_fallback_when_api_fails`
- `FAILED tests/kova_cli/test_codex_models.py::TestNormalizeModelForProvider::test_default_model_replaced`
- `FAILED tests/kova_cli/test_safe_mode.py::test_shell_hooks_register_without_safe_mode`
- `FAILED tests/tools/test_docker_config_migrate.py::test_docker_config_migrate_does_not_rewrite_invalid_yaml`
- `FAILED tests/website/test_generate_skill_docs.py::test_bundled_catalog_explains_missing_local_skills`

**Deduped assertion/error lines (7):**
- `E       AssertionError: assert 'gpt-5.6-sol' == 'gpt-5.3-codex'`
- `E       AssertionError: assert 'kova config:' in 'Failed to parse /tmp/pytest-of-runner/pytest-313/test_docker_config_migrate_doe0/config.yaml: while parsing a flow se...s saved to /tmp/pytest-of-runner/pytest-313/test_docker_config_migrate`
- `E       AssertionError: assert 'pre_tool_call' in {}`
- `E       AssertionError: assert False is True`
- `E       AssertionError: assert not True`
- `E       assert 'kova skills reset <name> --restore' in '---\nsidebar_position: 5\ntitle: "Bundled Skills Catalog"\ndescription: "Catalog of bundled skills that ship with Her...sing from this list but present in the repo, the catalog is rege`
- `E       assert False is True`

### Python tests / Run tests slice 3/8
- **Unique failing tests: 47**
- `FAILED tests/agent/test_openrouter_response_cache.py::TestBuildOrHeaders::test_base_attribution_always_present`
- `FAILED tests/gateway/test_slack_relay_parent_command.py::test_slack_relay_parent_becomes_gateway_command[/kova model gpt-5.6 --provider openai-/model gpt-5.6 --provider openai]`
- `FAILED tests/hermes_cli/test_placeholder_usage.py::test_config_set_usage_marks_placeholders`
- `FAILED tests/hermes_cli/test_profiles.py::TestCreateProfile::test_clone_all_excludes_default_infrastructure`
- `FAILED tests/kova_cli/test_gui_command.py::test_desktop_build_stamp_round_trip`
- `FAILED tests/kova_cli/test_gui_command.py::test_desktop_build_stamp_skips_build_when_up_to_date`
- `FAILED tests/kova_cli/test_gui_command.py::test_desktop_force_build_overrides_stamp`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_does_not_retry_after_packaged_executable_exists`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_forwards_desktop_environment_overrides`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_install_failure_self_heals_electron_and_continues`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_installs_packages_and_launches_desktop_app`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_linux_configures_sandbox_before_launch`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_linux_falls_back_to_no_sandbox_when_userns_is_restricted`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_linux_skips_fixup_when_already_configured`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_retries_pack_once_after_purging_build_cache`
- `FAILED tests/kova_cli/test_gui_command.py::test_gui_skip_build_launches_existing_packaged_app_without_npm`
- `FAILED tests/kova_cli/test_kanban_core_functionality.py::test_gateway_dispatcher_disables_corrupt_board_without_traceback[guard]`
- `FAILED tests/kova_cli/test_kanban_core_functionality.py::test_gateway_dispatcher_disables_corrupt_board_without_traceback[sqlite]`
- `FAILED tests/kova_cli/test_kanban_core_functionality.py::test_gateway_dispatcher_retries_corrupt_board_after_quarantine`
- `FAILED tests/kova_cli/test_kanban_core_functionality.py::test_gateway_dispatcher_watcher_env_truthy_uses_config`
- `FAILED tests/kova_cli/test_kanban_core_functionality.py::test_gateway_dispatcher_watcher_respects_config_flag_off`
- `FAILED tests/kova_cli/test_mcp_startup.py::test_cli_get_tool_definitions_briefly_waits_for_fast_mcp_thread`
- `FAILED tests/kova_cli/test_mcp_startup.py::test_init_agent_waits_for_mcp_discovery_before_agent_build`
- `FAILED tests/kova_cli/test_tips.py::TestTipsCorpus::test_max_length_reasonable`
- `FAILED tests/kova_cli/test_web_server_cron_profiles.py::test_dashboard_cron_noop_inference_fields_keep_existing_snapshots`
- `FAILED tests/kova_cli/test_web_server_cron_profiles.py::test_fire_cron_job_scopes_store_and_runtime_home_together`
- `FAILED tests/kova_cli/test_web_server_cron_profiles.py::test_update_cron_job_clears_snapshots_for_no_agent`
- `FAILED tests/kova_cli/test_web_server_cron_profiles.py::test_update_cron_job_refreshes_snapshots_when_unpinning`
- `FAILED tests/run_agent/test_provider_attribution_headers.py::test_no_user_default_headers_leaves_provider_defaults_untouched`
- `FAILED tests/run_agent/test_provider_attribution_headers.py::test_openrouter_base_url_applies_or_headers`
- `FAILED tests/run_agent/test_provider_attribution_headers.py::test_openrouter_headers_include_response_cache_when_enabled`
- `FAILED tests/run_agent/test_provider_attribution_headers.py::test_openrouter_headers_no_cache_when_disabled`
- `FAILED tests/run_agent/test_provider_attribution_headers.py::test_user_default_headers_win_over_provider_defaults`
- `FAILED tests/test_live_system_guard_self_test.py::test_asyncio_create_subprocess_shell_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_os_popen_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_os_system_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_subprocess_getoutput_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_subprocess_getstatusoutput_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_subprocess_run_bash_c_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_subprocess_run_sh_c_systemctl_blocked`
- `FAILED tests/test_live_system_guard_self_test.py::test_subprocess_run_string_shell_true_blocked`
- `FAILED tests/tools/test_approval.py::TestGatewayProtection::test_hermes_gateway_multiple_flags_detected`
- `FAILED tests/tools/test_approval.py::TestGatewayProtection::test_hermes_gateway_restart_with_profile_flag_detected`
- `FAILED tests/tools/test_approval.py::TestGatewayProtection::test_hermes_gateway_stop_detected`
- `FAILED tests/tools/test_approval.py::TestGatewayProtection::test_hermes_gateway_stop_with_long_profile_flag_detected`
- `FAILED tests/tools/test_video_generation_dynamic_schema.py::TestDynamicSchemaBuilder::test_no_config_says_so`
- `FAILED tests/tools/test_web_providers.py::TestDisabledPluginDiagnostic::test_extract_tool_reports_disabled_plugin`

**Deduped assertion/error lines (22):**
- `E                   TimeoutError`
- `E           AssertionError: Expected '_purge_electron_build_cache' to not have been called. Called 1 times.`
- `E           AssertionError: Tip 239 too long (152 chars): agent.api_max_retries (default 3) controls how many times th...`
- `E           AssertionError: assert {'job_id': 'w...hermes_test')} == {'job_id': 'w...orker_alpha')}`
- `E           assert 'kova plugins enable' in "web.extract_backend is set to 'firecrawl', but its plugin ('web/firecrawl') is disabled in config. Re-enable it with `hermes plugins enable web/firecrawl` (or remove it from plugins.disabled)."`
- `E           assert 152 <= 150`
- `E           asyncio.exceptions.CancelledError`
- `E       AssertionError: assert '/kova model ...ovider openai' == '/model gpt-5...ovider openai'`
- `E       AssertionError: assert 'Usage: hermes config set' in 'Usage: kova config set [--force] <key> <value>\n\nExamples:\n  kova config set model anthropic/claude-sonnet-4\n  kov...cker\n  kova config set OPENROUTER_API_KEY sk-or-...\n\n  `
- `E       AssertionError: assert 'https://kova-agent.kova.ai' == 'https://kova...sresearch.com'`
- `E       AssertionError: assert 'kova tools' in 'Generate a video from a text prompt (text-to-video), animate a still image (image-to-video), or guide generation with...video backend is available. Calls will return an error until the user pi`
- `E       AssertionError: assert None == 'initial-provider'`
- `E       AssertionError: assert None == 'worker-provider'`
- `E       AssertionError: assert True is False`
- `E       AssertionError: assert not True`
- `E       Failed: DID NOT RAISE <class 'RuntimeError'>`
- `E       IndexError: list index out of range`
- `E       assert 0 == 1`
- `E       assert 0 == 2`
- `E       assert 0.0003167810000093141 >= 0.04`
- `E       assert 1 == 0`
- `E       assert False is True`

### Python tests / Run tests slice 2/8
- **Unique failing tests: 9**
- `FAILED tests/cli/test_resume_quiet_stderr.py::TestResumeQuietStderr::test_session_not_found_goes_to_stderr_in_quiet_mode`
- `FAILED tests/hermes_cli/test_update_autostash.py::test_bootstrap_marker_not_autostashed_by_update`
- `FAILED tests/hermes_cli/test_update_autostash.py::test_install_method_marker_not_autostashed_by_update`
- `FAILED tests/hermes_cli/test_windows_native_docs.py::test_windows_native_install_path_docs_match_installer`
- `FAILED tests/kova_cli/test_kanban_diagnostics.py::test_triage_aux_unavailable_fires_auto_decompose_off_points_at_specifier`
- `FAILED tests/kova_cli/test_update_concurrent_quarantine.py::test_detect_concurrent_matches_case_insensitively`
- `FAILED tests/kova_cli/test_update_concurrent_quarantine.py::test_quarantine_succeeds_first_attempt`
- `FAILED tests/kova_cli/test_web_ui_build.py::TestBuildWebUIFlock::test_lock_file_is_gitignored`
- `FAILED tests/plugins/platforms/photon/test_auth.py::test_find_project_by_name_case_insensitive`

**Deduped assertion/error lines (10):**
- `E        +  where 'Session not found: 20260524_111111_xyz\nUse a session ID from a previous CLI run (hermes sessions list).\n' = CaptureResult(out='', err='Session not found: 20260524_111111_xyz\nUse a session ID from a previous CLI run (he`
- `E       AssertionError: .hermes-bootstrap-complete was swept into the update autostash — it must be listed in .gitignore so `git stash -u` skips it (#38529).`
- `E       AssertionError: .install_method was swept into the update autostash — it must be listed in .gitignore so `git stash -u` skips it (#66189).`
- `E       AssertionError: assert '.web_ui_build.lock' in '\ufeff__pycache__/\n*.pyc\n*.pyo\n.pytest_cache/\nnode_modules/\nvenv/\n.venv/\ndist/\nbuild/\n*.egg-info/\n.env\n.en...nt.log\nerrors.log\ngateway.log\nkova.log\n*.swp\n*.swo\n*~\n.id`
- `E       AssertionError: assert 'kova sessions list' in 'Session not found: 20260524_111111_xyz\nUse a session ID from a previous CLI run (hermes sessions list).\n'`
- `E       AssertionError: assert False`
- `E       AssertionError: assert [] == [(9999, 'HERMES.EXE')]`
- `E       assert '%LOCALAPPDATA%\\kova\\kova-agent\\venv\\Scripts' in '---\ntitle: "Windows (Native) Guide"\ndescription: "Run Kova Agent natively on Windows 10 / 11 — install, feature mat...ws-specific questions.\n- **[Messaging Gateway](./m`
- `E       assert (None is not None)`
- `E       assert False`

### Python tests / Run tests slice 8/8
- **Unique failing tests: 40**
- `FAILED tests/agent/test_auxiliary_client.py::TestCustomEndpointApiKeyInheritance::test_inherits_main_api_key_when_aux_key_empty`
- `FAILED tests/agent/test_billing_links.py::test_is_nous_inference_route_helper`
- `FAILED tests/agent/test_billing_links.py::test_nous_route_by_base_url_host - ...`
- `FAILED tests/agent/test_learn_prompt.py::TestBuildLearnPrompt::test_teaches_the_full_hardline_standards`
- `FAILED tests/gateway/test_slack.py::TestAppMentionHandler::test_app_mention_registered_on_connect`
- `FAILED tests/hermes_cli/test_safe_mode.py::test_mcp_servers_load_without_safe_mode`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_refresh_adopts_singleton_tokens_when_consumed_elsewhere`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_refresh_recovers_when_other_process_already_refreshed`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_seeded_entry_sync_back_after_refresh`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_select_proactively_refreshes_expiring_token`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_sync_back_preserves_active_provider`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_sync_back_writes_to_singleton`
- `FAILED tests/kova_cli/test_auth_xai_oauth_provider.py::test_pool_try_refresh_current_handles_xai_oauth`
- `FAILED tests/kova_cli/test_cli_model_once.py::test_cli_model_once_records_restore_and_does_not_persist`
- `FAILED tests/kova_cli/test_dashboard_basic_auth_plugin_enable.py::TestBasicProviderLoadsAfterUnblock::test_unblock_then_rediscover_registers_provider`
- `FAILED tests/kova_cli/test_model_picker_expensive_confirm.py::test_prompt_toolkit_model_picker_defers_confirmation_off_key_handler`
- `FAILED tests/kova_cli/test_proxy.py::test_xai_adapter_retry_refreshes_current_pool_entry`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_blocked_downgrade_fallback_stays_generic`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_blocked_upgrade_fallback_carries_plan_param`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_bounded_stepup_does_not_loop_on_repeat_denial`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_change_flow_schedules_a_downgrade`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_change_flow_upgrade_charges_now`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_change_menu_cancel_schedules_cancellation`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_insufficient_scope_triggers_stepup_then_replays`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_open_url_in_browser_opens_when_graphical`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_pending_change_menu_offers_undo`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_stepup_declined_grant_does_not_replay`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_upgrade_confirm_names_the_subscription_card`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_upgrade_rate_limit_is_deterministic_not_ambiguous`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_upgrade_transport_failure_is_ambiguous_not_flat_failure`
- `FAILED tests/kova_cli/test_subscription_cli.py::test_upgrade_transport_failure_still_ambiguous_after_narrowing`
- `FAILED tests/kova_cli/test_update_autostash.py::test_bootstrap_marker_not_autostashed_by_update`
- `FAILED tests/kova_cli/test_update_autostash.py::test_install_method_marker_not_autostashed_by_update`
- `FAILED tests/kova_cli/test_web_server.py::TestWebServerEndpoints::test_memory_provider_config_honors_profile_param`
- `FAILED tests/kova_cli/test_windows_native_docs.py::test_windows_native_install_path_docs_match_installer`
- `FAILED tests/kova_cli/test_xiaomi_provider.py::TestXiaomiCredentials::test_resolve_credentials_reads_home_external_secret_scope`
- `FAILED tests/test_packaging_build_guard.py::test_artifact_build_allows_explicit_nix_package_build_marker[sdist-hermes_agent-*.tar.gz]`
- `FAILED tests/test_packaging_build_guard.py::test_artifact_build_allows_explicit_nix_package_build_marker[wheel-hermes_agent-*.whl]`
- `FAILED tests/test_packaging_build_guard.py::test_artifact_build_rejects_nix_development_shell_environment[sdist]`
- `FAILED tests/test_packaging_build_guard.py::test_artifact_build_rejects_nix_development_shell_environment[wheel]`

**Deduped assertion/error lines (28):**
- `E           AssertionError: Slack slash regex does not match /hermes`
- `E           assert None`
- `E       AssertionError: .hermes-bootstrap-complete was swept into the update autostash — it must be listed in .gitignore so `git stash -u` skips it (#38529).`
- `E       AssertionError: .install_method was swept into the update autostash — it must be listed in .gitignore so `git stash -u` skips it (#66189).`
- `E       AssertionError: Custom endpoint with empty api_key should inherit model.api_key from config, got: 'no-key-required'`
- `E       AssertionError: assert '' == 'sk-bws-xiaomi-12345678'`
- `E       AssertionError: assert 'Manage on portal:' in '\n  ⚕ Plan: Plus · renews Jul 28, 2026\n  ─────────────────────────────────────────\n  Org: Acme · Owner\n  ─────────...────────────────────────────\n  Checking the change…\n  🔴 Not log`
- `E       AssertionError: assert 'Manage on portal:' in '\n  ⚕ Plan: Ultra · renews Jul 28, 2026\n  ─────────────────────────────────────────\n  Org: Acme · Owner\n  ────────...────────────────────────────\n  Checking the change…\n  🔴 Not log`
- `E       AssertionError: assert 'Slow down' in '\n  ⚕ Plan: Plus · renews Jul 28, 2026\n  ─────────────────────────────────────────\n  Org: Acme · Owner\n  ─────────...────────────────────────────\n  Checking the change…\n  🔴 Not logged into`
- `E       AssertionError: assert 'Visa ····4242 — the card on your subscription — will be charged.' in '\n  ⚕ Plan: Plus · renews Jul 28, 2026\n  ─────────────────────────────────────────\n  Org: Acme · Owner\n  ─────────...──────────────────`
- `E       AssertionError: assert 'author: always the literal value `kova`' in 'follow the kova skill-authoring standards exactly. these are the same\nhardline rules a maintainer enforces in review...ath — not\n  inlined for the agent to re-ty`
- `E       AssertionError: assert 'github' in {}`
- `E       AssertionError: assert 'may or may not have been charged' in '\n  ⚕ Plan: Plus · renews Jul 28, 2026\n  ─────────────────────────────────────────\n  Org: Acme · Owner\n  ─────────...────────────────────────────\n  Checking the chang`
- `E       AssertionError: assert 'old/model' == 'claude-sonnet-4.6'`
- `E       AssertionError: assert False is True`
- `E       AssertionError: assert None == 'plus'`
- `E       AssertionError: assert None == 'ultra'`
- `E       AssertionError: assert None is True`
- `E       AssertionError: assert []`
- `E       KeyError: 'peerName'`
- `E       assert '%LOCALAPPDATA%\\kova\\kova-agent\\venv\\Scripts' in '---\ntitle: "Windows (Native) Guide"\ndescription: "Run Kova Agent natively on Windows 10 / 11 — install, feature mat...ws-specific questions.\n- **[Messaging Gateway](./m`
- `E       assert 'Building wheels or sdists for kova-agent is not supported' in '/home/runner/work/Kova-Agent/Kova-Agent/.venv/lib/python3.11/site-packages/setuptools/dist.py:483: SetuptoolsDeprecat...x (uv2nix), this error should not fire —\`
- `E       assert 'no-key-required' == 'sk-main-config-key'`
- `E       assert (ModelSwitchR...), True, None) == (ModelSwitchR...), True, None)`
- `E       assert 0 == 1`
- `E       assert 0 == 2`
- `E       assert False`
- `E       assert None is not None`

### Python tests / Run tests slice 7/8
- **Unique failing tests: 18**
- `FAILED tests/agent/test_curator_classification.py::test_rename_summary_pin_hint_appears_when_consolidation_produced_umbrella`
- `FAILED tests/agent/test_curator_classification.py::test_rename_summary_pin_hint_picks_one_umbrella_when_multiple_absorbed`
- `FAILED tests/agent/test_nous_oauth_401_guidance.py::test_nous_401_guidance_strings_present`
- `FAILED tests/hermes_cli/test_backup.py::TestBackup::test_default_output_path`
- `FAILED tests/hermes_cli/test_backup.py::TestBackup::test_excludes_hermes_agent`
- `FAILED tests/hermes_cli/test_backup.py::TestBackup::test_includes_nested_hermes_agent_in_skills`
- `FAILED tests/hermes_cli/test_backup.py::TestBackupEdgeCases::test_output_is_directory`
- `FAILED tests/hermes_cli/test_backup.py::TestPreMigrationBackup::test_backup_uses_shared_exclusion_rules`
- `FAILED tests/hermes_cli/test_backup.py::TestPreUpdateBackup::test_backup_contents_match_full_backup`
- `FAILED tests/hermes_cli/test_backup.py::TestRoundTrip::test_backup_then_import`
- `FAILED tests/hermes_cli/test_backup.py::TestShouldExclude::test_excludes_hermes_agent`
- `FAILED tests/hermes_cli/test_tools_config.py::TestPlatformToolsetConsistency::test_gateway_toolset_includes_all_messaging_platforms`
- `FAILED tests/kova_cli/test_auth_commands.py::test_auth_remove_copilot_suppresses_all_variants`
- `FAILED tests/kova_cli/test_gateway_runtime_health.py::test_runtime_status_running_pid_validates_live_gateway_record`
- `FAILED tests/kova_cli/test_models_dev_preferred_merge.py::TestProviderModelIdsPreferred::test_k3_live_discovery_is_scoped_to_kimi_coding_endpoint`
- `FAILED tests/kova_cli/test_setup_openclaw_migration.py::TestGetSectionConfigSummary::test_gateway_lists_platforms`
- `FAILED tests/kova_cli/test_setup_openclaw_migration.py::TestGetSectionConfigSummary::test_gateway_recognises_whatsapp_enabled`
- `FAILED tests/kova_cli/test_web_server_skill_editor.py::TestSkillContent::test_get_content_scopes_to_profile`

**Deduped assertion/error lines (16):**
- `E           AssertionError: kova-agent files leaked into backup: ['kova-agent/run_agent.py']`
- `E           AssertionError: root kova-agent leaked: ['kova-agent/run_agent.py']`
- `E           assert ['kova-agent/run_agent.py'] == []`
- `E       AssertionError: assert 'k3' in ['kimi-k3', 'kimi-k2.7-code', 'kimi-k2.6', 'kimi-k2.5', 'kimi-for-coding', 'kimi-for-coding-highspeed', ...]`
- `E       AssertionError: assert 'kova curator pin document-tools' in 'archived 2 skill(s):\n  • docx-extraction → document-tools\n  • pdf-extraction → document-tools\nfull report: kova curator status\nkeep an umbrella stable: hermes curator `
- `E       AssertionError: assert 'kova curator pin umbrella-alpha' in 'archived 2 skill(s):\n  • a-skill → umbrella-zeta\n  • b-skill → umbrella-alpha\nfull report: kova curator status\nkeep an umbrella stable: hermes curator pin umbrella-alp`
- `E       AssertionError: assert 'kova portal' in 'def run_conversation(\n    agent,\n    user_message: Any,\n    system_message: str = None,\n    conversation_history:...ication_response,\n        _pending_verification_response_previewed=_pe`
- `E       AssertionError: assert False`
- `E       AssertionError: assert None == 12345`
- `E       AssertionError: assert not True`
- `E       KeyError: 'kova-gateway'`
- `E       TypeError: argument of type 'NoneType' is not iterable`
- `E       assert 0 == 1`
- `E       assert 404 == 200`
- `E       assert None is not None`
- `E       assert not True`

### Python tests / Run tests slice 5/8
- **Unique failing tests: 29**
- `FAILED tests/agent/test_usage_pricing.py::test_nous_portal_pricing_preserves_vendor_prefixed_model_ids`
- `FAILED tests/hermes_cli/test_config.py::TestLoadConfigParseFailure::test_dedup_on_repeated_load_same_file`
- `FAILED tests/hermes_cli/test_config.py::TestLoadConfigParseFailure::test_logs_and_warns_on_parse_failure`
- `FAILED tests/hermes_cli/test_config.py::TestLoadConfigParseFailure::test_rewarns_after_file_edit`
- `FAILED tests/hermes_cli/test_container_aware_cli.py::test_get_container_exec_info_defaults`
- `FAILED tests/hermes_cli/test_gui_command.py::test_desktop_build_stamp_round_trip`
- `FAILED tests/hermes_cli/test_gui_command.py::test_desktop_build_stamp_skips_build_when_up_to_date`
- `FAILED tests/hermes_cli/test_gui_command.py::test_desktop_force_build_overrides_stamp`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_does_not_retry_after_packaged_executable_exists`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_forwards_desktop_environment_overrides`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_install_failure_self_heals_electron_and_continues`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_installs_packages_and_launches_desktop_app`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_linux_configures_sandbox_before_launch`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_linux_falls_back_to_no_sandbox_when_userns_is_restricted`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_linux_skips_fixup_when_already_configured`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_retries_pack_once_after_purging_build_cache`
- `FAILED tests/hermes_cli/test_gui_command.py::test_gui_skip_build_launches_existing_packaged_app_without_npm`
- `FAILED tests/kova_cli/test_25106_global_switch_persists_base_url_api_mode.py::test_global_switch_clears_base_url_and_api_mode_when_unresolved`
- `FAILED tests/kova_cli/test_25106_global_switch_persists_base_url_api_mode.py::test_global_switch_persists_base_url_and_api_mode`
- `FAILED tests/kova_cli/test_25106_global_switch_persists_base_url_api_mode.py::test_global_switch_persists_provider_when_runtime_provider_is_unchanged`
- `FAILED tests/kova_cli/test_apply_model_switch_result_context.py::test_global_switch_clears_context_pin_owned_by_previous_route`
- `FAILED tests/kova_cli/test_auth_codex_quota_probe.py::test_pool_entry_recovers_when_probe_confirms_reset`
- `FAILED tests/kova_cli/test_backup.py::TestBackup::test_default_output_path - ...`
- `FAILED tests/kova_cli/test_backup.py::TestBackupEdgeCases::test_output_is_directory`
- `FAILED tests/kova_cli/test_launcher.py::test_launcher_delegates_to_argparse_entrypoint`
- `FAILED tests/kova_cli/test_setup.py::test_setup_gateway_in_container_shows_docker_guidance`
- `FAILED tests/kova_cli/test_setup.py::test_setup_gateway_skips_service_install_when_systemctl_missing`
- `FAILED tests/kova_cli/test_tools_config.py::TestPlatformToolsetConsistency::test_gateway_toolset_includes_all_messaging_platforms`
- `FAILED tests/skills/test_openclaw_migration.py::test_cron_store_is_archived_without_config_cron_section`

**Deduped assertion/error lines (20):**
- `E           AssertionError: Expected '_purge_electron_build_cache' to not have been called. Called 1 times.`
- `E           AssertionError: assert 'hermes-agent' == 'kova-agent'`
- `E           AssertionError: assert 'kova config:' in '⚠️  hermes config: Failed to parse /tmp/pytest-of-runner/pytest-152/test_dedup_on_repeated_load_sa0/config.yaml: whil...s saved to /tmp/pytest-of-runner/pytest-152/test_dedup_on_repeated`
- `E           AssertionError: assert 'kova config:' in '⚠️  hermes config: Failed to parse /tmp/pytest-of-runner/pytest-152/test_logs_and_warns_on_parse_f0/config.yaml: whil...s saved to /tmp/pytest-of-runner/pytest-152/test_logs_and_warns_on`
- `E           AssertionError: edited file should re-warn`
- `E           assert 'kova config:' in '⚠️  hermes config: Failed to parse /tmp/pytest-of-runner/pytest-152/test_rewarns_after_file_edit0/config.yaml: while ...ping the previously loaded config for this process — edits to config.yaml are bein`
- `E       AssertionError: assert 'Run `kova cron` to recreate scheduled tasks' in '# OpenClaw -> Hermes Migration Notes\n\nThis document lists items that require manual attention after migration.\n\n#...Run `hermes gateway install` if you nee`
- `E       AssertionError: assert 'https://infe...pi.kova.ai/v1' == 'https://infe...search.com/v1'`
- `E       AssertionError: assert ('model.context_length', None) in [('model.default', 'shared-model'), ('model.provider', 'custom'), ('model.base_url', 'https://small.example/v1'), ('model.api_mode', 'chat_completions')]`
- `E       AssertionError: assert True is False`
- `E       AssertionError: assert [] == ['kova_cli.main']`
- `E       IndexError: list index out of range`
- `E       KeyError: 'kova-gateway'`
- `E       KeyError: 'model.base_url'`
- `E       KeyError: 'model.default'`
- `E       KeyError: 'model.provider'`
- `E       assert 'Messaging platforms configured!' in "\nâ—† Messaging Platforms\n  Connect to messaging platforms to chat with Kova from anywhere.\n  Toggle with Space, confirm with Enter.\n\n  No platforms selected. Run 'kova setup gateway'`
- `E       assert 0 == 1`
- `E       assert 1 == 0`
- `E   ModuleNotFoundError: No module named 'kova_cli.auth'`

## 4. JS/TS and Docker failure summaries (top-level)


### Build&Test Docker image / build (arm64, ubuntu-24.04-arm, linux/arm64, type=gha,scope=docker-arm64, type=gha,mode=max,scope...
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
(node:104180) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
[command]/usr/bin/docker buildx rm builder-bd1a551f-b92a-47c0-874d-3e70134c15da
builder-bd1a551f-b92a-47c0-874d-3e70134c15da removed
State not set
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: docker/setup-buildx-action@8d2750c68a42422c14e847fe6c8ac0403b4cbd6f. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### Build&Test Docker image / build (amd64, ubuntu-latest, linux/amd64, type=gha,scope=docker-amd64, type=gha,mode=max,scope=do...
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
(node:112821) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
[command]/usr/bin/docker buildx rm builder-cf1e1922-0e51-4ad1-9e0e-7ebb52ba28ad
builder-cf1e1922-0e51-4ad1-9e0e-7ebb52ba28ad removed
State not set
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: docker/setup-buildx-action@8d2750c68a42422c14e847fe6c8ac0403b4cbd6f. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### Review label gate / Review label gate
- `##[error]CI-sensitive changes require the ci-reviewed label. Add the label and re-run this check.`
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
  HEAD_SHA: afa5b01466836ed928c9e5c154be3d931cc700a3
^[[36;1mecho "::error::CI-sensitive changes require the ci-reviewed label. Add the label and re-run this check."^[[0m
^[[36;1mexit 1^[[0m
shell: /usr/bin/bash -e {0}
##[error]CI-sensitive changes require the ci-reviewed label. Add the label and re-run this check.
##[error]Process completed with exit code 1.
```

### JS & TS checks / apps/desktop / check:test:desktop:all
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
npm error workspace kova@0.17.0
npm error location /home/runner/work/Kova-Agent/Kova-Agent/apps/desktop
npm error command failed
npm error command sh -c node scripts/test-desktop.mjs all
##[error]Process completed with exit code 1.
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### JS & TS checks / apps/desktop / check:test:desktop:platforms
- `##[error]AssertionError: Expected values to be strictly equal:`
- `##[error]AssertionError: Expected values to be strictly equal:`
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
npm error workspace kova@0.17.0
npm error location /home/runner/work/Kova-Agent/Kova-Agent/apps/desktop
npm error command failed
npm error command sh -c vitest run --project electron
##[error]Process completed with exit code 1.
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### JS & TS checks / apps/desktop / check:test:ui
- `##[error]TestingLibraryElementError: Unable to find an element with the text: Remote spending is off for this account — a billing admin can turn it on from the portal's Hermes Agent page.. This could be because the text is broken up by multiple elements. In this case, you can provide a function for your text matcher to make your matcher more flexible.`
- `##[error]TestingLibraryElementError: Unable to find an element with the text: Connect your Nous account. This could be because the text is broken up by multiple elements. In this case, you can provide a function for your text matcher to make your matcher more flexible.`
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
npm error workspace kova@0.17.0
npm error location /home/runner/work/Kova-Agent/Kova-Agent/apps/desktop
npm error command failed
npm error command sh -c vitest run --project ui
##[error]Process completed with exit code 1.
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### JS & TS checks / ui-tui / check
- `##[error]AssertionError: expected 'Out of Kova credits' to contain 'Nous'`
- `##[error]AssertionError: expected '[You #1]\nhello\n\n[Kova #2]\nhi ther…' to contain '[Hermes #2]'`
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
npm error location /home/runner/work/Kova-Agent/Kova-Agent/ui-tui
npm error command failed
npm error command sh -c vitest run
##[error]Process completed with exit code 1.
Terminate orphan process: pid (2614) (sleep)
##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### All required checks pass
- `##[error]3 job(s) failed: tests, js-tests, review-labels`
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
❌ review-labels: failure
✅ supply-chain: success
❌ tests: failure
✅ uv-lockfile: success
##[error]3 job(s) failed: tests, js-tests, review-labels
##[error]Process completed with exit code 1.
```

### CI review comment (live)
- `##[error]Process completed with exit code 1.`

**Last 6 lines:**
```
  No visible jobs pending — waiting 10s for downstream jobs to appear.
  [664s] 44 completed, 0 pending (44 total jobs)
  Updated comment 5126615443
  All jobs done, but 14 failed: Build&Test Docker image / build (arm64, ubuntu-24.04-arm, linux/arm64, type=gha,scope=docker-arm64, type=gha,mode=max,scope..., Build&Test Docker image / build (amd64, ubuntu-latest, linux/amd64, type=gha,scope=docker-amd64, type=gha,mode=max,scope=do..., Python tests / Run tests slice 4/8, Python tests / Run tests slice 6/8, Python tests / Run tests slice 3/8, Python tests / Run tests slice 2/8, Python tests / Run tests slice 8/8, Python tests / Run tests slice 7/8, Python tests / Run tests slice 5/8, Review label gate / Review label gate, JS & TS checks / apps/desktop / check:test:desktop:all, JS & TS checks / apps/desktop / check:test:desktop:platforms, JS & TS checks / apps/desktop / check:test:ui, JS & TS checks / ui-tui / check
  Exiting with error so the run can be rerun via --failed.
##[error]Process completed with exit code 1.
```

## 5. Regression check — NEW failures vs run 30699981302 (191)

**Result: ZERO new failures / zero regressions.** Verified at three levels against the v2 run's raw logs:
- **Test files:** 86 files in v3 ⊆ 89 in v2 (3 files fully cleared) — no new files
- **Test cases:** 184 in v3 ⊆ 190 in v2 — no new cases
- **4 initially-flagged "NEW"** (test_nous_route_by_base_url_host, test_slack_relay_parent_becomes_gateway_command, test_backup::test_default_output_path, test_gui_uninstall::test_userdata_dir_windows) were **truncation artifacts** of the v2 report text (`- ...` suffixes) — all present in v2's raw logs (6/5/12/6 hits).

**What cleared (6 test groups — exactly the fixed cluster):**
- hermes_cli/test_update_stale_dashboard.py::TestFindStaleDashboardPids — all
- hermes_cli/test_update_stale_dashboard.py::TestKillStaleDashboardPosix — all
- hermes_cli/test_update_concurrent_quarantine.py — all 3 (detect case-insensitive, format message, quarantine succeeds)
- hermes_cli/test_update_fleet_restart_timeout.py::TestFleetRestartTimeoutIsolation — all 3

**Count trajectory:** 280 → 191 → **175** unique slice failures.

**Note:** the kova_cli/ twin copies of test_update_fleet_restart_timeout and test_gateway_proc_fallback remain failing (pre-existing, present in v2 at 18 hits each) — the fixes landed on the canonical hermes_cli twins; the kova copies need the same treatment in a follow-up.
