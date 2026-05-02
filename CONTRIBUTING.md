# Contributing to AI Delivery Warden

Thanks for helping make AI agent deliveries less sloppy.

## Good Contributions

- Add new delivery-risk rules
- Add suspicious phrases from real AI agent failures
- Improve Chinese or English wording
- Add examples of bad and good AI deliveries
- Add JSON output or GitHub PR review mode
- Improve documentation and launch examples

## Rule Design Principles

Rules should be:

- Explainable
- Easy to trigger intentionally in examples
- Low on false positives
- Paired with actionable return prompts
- Useful for real delivery review, not just code style

## Development

```bash
python3 -m ai_delivery_warden.cli examples/bad_delivery_zh.md --lang zh
python3 -m ai_delivery_warden.cli examples/good_delivery_zh.md --lang zh
env PYTHONPYCACHEPREFIX=/private/tmp/ai-delivery-warden-pycache python3 -m compileall ai_delivery_warden
```

## Pull Requests

Please include:

- What problem the rule or change catches
- Before/after example
- Verification command and output
- Any false-positive risk
