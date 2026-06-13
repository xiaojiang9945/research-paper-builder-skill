# Synthetic Wheat Study Demo

This runnable example uses wheat salt-response data structures to show a formal manuscript-scale package with three main figures.

## Run The Demo

```bash
python scripts/build_demo.py
```

The script regenerates:

- three input CSV files for germination, physiology and expression;
- three formal SVG figures;
- `output/manuscript_draft.md` with figure captions below the figures;
- Nature-style numbered references;
- a five-pass QC report stored outside the formal manuscript.

## Design Notes

- Organism context: wheat (_Triticum aestivum_).
- Figure style: candy-colour data accents on a premium-gray scaffold.
- Formal figures avoid process notes, claim-boundary panels and QC labels.
- Literature status: real manuscripts still require documented searching and a 200-paper full-text reading matrix before polished writing.
