# GitScience Registry

This repository is the canonical, versioned scientific record rendered by the
[GitScience Observatory](https://napoles3d-gitscience-observatory.static.hf.space/).
It contains claims, mathematical exposition, equations, models, evidence,
artifacts, reviews, and open obligations. The Observatory is a generated view;
scientific content is edited and reviewed here.

The registry currently contains two complete case studies:

- **Twisted ribbon transport:** a conditional Lean argument and a finite Kwant
  check of transmission under twist reversal.
- **Quantum-FMM occupancy:** an abstract Lean accumulation proof and a finite
  occupancy-tail diagnostic motivated by a quantum fast multipole method.

GitScience does not assign truth scores. A successful verification establishes
only the declared assertion, under its recorded assumptions and scope.

## Layout

```text
registry.yaml                         central publication manifest
studies/twisted-ribbon/               one GitScience study root
studies/quantum-fmm/                  another GitScience study root
  articles/                           ordered human-readable arguments
  equations/                          numbered LaTeX records
  claims/                             structured scientific claims
  evidence/ and artifacts/            verifier outputs and provenance
```

Both study roots share this repository's single Git history. There are no
nested repositories. This lets ordinary commits and pull requests attribute
each addition, correction, reproduction, or challenge.

## Inspect locally

Install [GitScience](https://github.com/napoles-uach/gitscience), then run:

```bash
gitscience -C studies/twisted-ribbon claim graph
gitscience -C studies/twisted-ribbon claim explain GS-QT-0005
gitscience -C studies/twisted-ribbon audit

gitscience -C studies/quantum-fmm claim graph
gitscience -C studies/quantum-fmm claim explain GS-QF-0007
gitscience -C studies/quantum-fmm audit

gitscience registry build --from registry.yaml --output /tmp/registry.json
```

The committed evidence was generated with the trusted `lean_formal`,
`kwant_transport`, and `fmm_occupancy` verifier contracts. Evidence is
integrity-checked but not yet cryptographically authenticated.

## Contribute

Researchers comfortable with Git can follow [CONTRIBUTING.md](CONTRIBUTING.md)
and submit a pull request. Researchers who do not use Git can open a structured
**research seed** issue. A seed remains explicitly incomplete until a
contributor turns it into versioned claims and evidence; it is never presented
as a validated result merely because it was submitted.

Reproductions and challenges are first-class contributions. They should target
an exact claim ID and revision, state the changed conditions, and attach enough
information for independent inspection.
