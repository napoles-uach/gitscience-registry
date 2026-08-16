# Contributing to the scientific registry

## Two entry points

1. **Structured proposal without Git:** open a `Research seed` issue and provide
   the question, hypothesis, equations, assumptions, scope, and intended
   verification. Another contributor may help formalize it.
2. **Versioned contribution with Git:** fork this repository, create a branch,
   add or revise a GitScience study, run the checks below, and open a pull
   request.

Issues are the incubator; the canonical scientific state consists only of
reviewed files merged into Git. Discussion never silently becomes evidence.

## Required structure

A publishable study should make these distinctions explicit:

- research question and plain-language resolution;
- ordered prose and numbered equations;
- definitions, assumptions, supporting results, main results, limitations, and
  open questions;
- exact claim dependencies and scope;
- trusted verifier contract and generated evidence where applicable;
- what the result does not establish.

Numerical evidence must not be generalized beyond its declared parameter
domain. A Lean proof must identify which premises are encoded and which
physical correspondence obligations remain outside the theorem.

## Local checks

```bash
gitscience -C studies/YOUR-STUDY audit
gitscience -C studies/YOUR-STUDY claim obligations
gitscience registry build --from registry.yaml --output /tmp/registry.json
python scripts/validate_registry.py /tmp/registry.json
```

Do not edit generated verifier evidence or artifacts by hand. Re-run the
declared verifier instead. Never commit API keys, `.env` files, credentials, or
private participant data.

## Review expectations

A pull request should say which claim revisions change, why the verification is
sufficient for the stated scope, and which obligations remain open. Review can
accept a useful incomplete research seed, but incomplete work must retain an
explicit non-established status.
