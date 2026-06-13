# Synthetic Wheat Study Demo

This runnable example uses wheat salt-response data structures to show a formal manuscript-scale package with three main figures.

## Run The Demo

```bash
python scripts/build_demo.py
```

The script uses `matplotlib` and `numpy` and regenerates:

- four input CSV files for germination, physiology, expression and geographic distribution;
- three white-background six-panel SVG figures;
- `output/manuscript_draft.md` with figure captions below the figures;
- at least 30 Nature-style numbered references;
- a five-pass QC report stored outside the formal manuscript.

## Design Notes

- Organism context: wheat (_Triticum aestivum_).
- Figure style: pure white background, compact multi-panel layout, candy-colour data accents and premium-gray axes/grid lines.
- Figure examples include geographic distribution maps, scatter and bubble plots, box/violin plots, heatmaps, contour fields and 3D response surfaces.
- Literature status: real manuscripts still require documented searching and a 200-paper full-text reading matrix before polished writing.
