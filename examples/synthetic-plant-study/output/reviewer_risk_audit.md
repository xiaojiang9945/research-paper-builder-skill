# Reviewer-Risk Audit

| risk | severity | where it appears | why it matters | fix now | longer-term fix |
|---|---|---|---|---|---|
| Reader may mistake synthetic data for a real study | high | title, abstract, Results | could mislead readers | label the dataset as synthetic in every major section | keep demo files separate from real project folders |
| Mechanistic overclaim | high | Discussion | germination counts do not test mechanism | state that no mechanism is inferred | add molecular or physiological assays in a real study |
| Small replicate count | medium | Methods, Results | n=3 supports descriptive summary only | avoid significance and broad generalization | increase replication and preregister analysis in a real study |
| Salt treatment lacks concentration details | medium | Methods | demo omits a key real-world assay detail | state that concentration is intentionally omitted in synthetic demo | include full protocol in a real manuscript |
| Figure source data must remain synchronized | medium | figure plan and source data | stale values would break traceability | keep `source_data_figure1.csv` as the figure source | regenerate source data from scripts in a real project |
| Citation list omitted | low | manuscript draft | demo does not cite real literature | state that demo is not a real article | add verified citations for real manuscripts |
| 200-paper literature gate not actually run | high | literature intake | real high-ambition manuscripts require documented full-text literature reading | label demo citation set as synthetic | run real search, screening and full-text reading of at least 200 relevant papers for real topic |
| Composite figure is illustrative SVG | medium | Figure 1 | real journals require publication-quality data panels | mark schematic/non-data panels clearly | regenerate final figure from plotting scripts and inspect at print size |

## Highest-Leverage Revision Steps

1. Keep "synthetic" in the title, Abstract, Methods and Data Availability.
2. Avoid mechanism language.
3. Keep source data files in the demo output folder.
4. Do not add real project names, accession names or author information.
5. Do not describe the synthetic citation set as a real literature review.
