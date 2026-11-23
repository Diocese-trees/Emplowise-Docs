.PHONY: build verify tokens sync sync-check

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
