.PHONY: build verify tokens sync sync-check report report-check links

build: ## rebuild all Office exports from Markdown
	@bash scripts/build.sh

verify: ## rebuild and verify Office packages
	@bash scripts/build.sh

tokens: ## check tokens.css and brand-tokens.json agree
	@python3 scripts/check_tokens.py

sync: ## push tokens and exports into the main repo
	@python3 scripts/sync.py all

sync-check: ## fail if the main repo has drifted from this repo
	@python3 scripts/sync.py check

report: ## rebuild the internal executive report (HTML, plus PDF when Chromium exists)
	@bash scripts/build_report.sh

report-check: ## rebuild the report and run the Playwright acceptance pass
	@bash scripts/build_report.sh
	@python3 generators/report-ui/test_report.py

links: ## check that every relative Markdown cross-reference resolves
	@python3 scripts/check_links.py
