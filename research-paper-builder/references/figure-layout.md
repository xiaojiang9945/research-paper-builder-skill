# Figure Layout

Use this reference when planning, rebuilding or visually checking figures.

## Figure-Led Manuscript Logic

Before drawing or polishing, assign each main figure one result question. The manuscript should be able to tell the Results story by walking through the figures in order.

For each figure, record:
- result question;
- panels and evidence type;
- source data file or worksheet;
- key statistic or model;
- caption claim;
- manuscript subsection that cites it.
- why each plot type is the best match for the available data.

If two panels answer the same question, merge, remove or repurpose one of them.

Formal main figures should contain scientific content only. Do not place author-facing statements, claim-boundary boxes, QC gates, package manifests, process notes, generation notes, prompt notes or explanatory demo text inside figures intended to represent a submitted manuscript. Put those checks in separate QC files, evidence maps or reviewer-risk audits.
Synthesis models, mechanism cartoons and experimental roadmaps can be main figures only when they are clearly derived from preceding evidence and labeled as models, hypotheses or assay logic. Their captions and Results text must not imply direct validation unless the panel contains measured data.

## Data-Figure Contract

Every data-bearing panel needs a contract before it is drawn:
- panel question: the exact result question the panel answers;
- source data: file, worksheet, columns and filtering rule;
- statistical unit: plant, line, accession, plot, replicate, gene, site or time point;
- analysis: test, model, normalization, projection, smoothing or transformation;
- visual reason: why this plot type is the clearest match for the result;
- manuscript link: Results subsection, panel callout and caption claim;
- reproducibility path: script, notebook or command that rebuilds the panel.

If the source data do not support the proposed map, 3D surface, contour, bubble plot, distribution plot or heatmap, produce a figure plan or request the missing data. Do not invent a rich visual only to make the manuscript look advanced.

## Figure Planning

Each main figure should answer one result question. A strong composite figure usually combines:
- one overview or design panel,
- one primary quantitative result,
- one stratified or temporal comparison,
- one mechanistic or explanatory analysis,
- one source-data-supported candidate or validation-oriented panel when appropriate.

Panel count follows the evidence, but formal main figures should default to 4 or 6 panels when there is no special reason to do otherwise. Use 2, 3, 5 or more panels only when the target journal, evidence structure, figure geometry or readability clearly justifies the departure.

## Composite Layout

Use these defaults unless the journal specifies otherwise:
- one panel letter per panel, placed consistently;
- no duplicate letters inside source plots;
- no internal titles when captions explain panel content;
- shared legends where possible;
- aligned axes for comparable panels;
- balanced panel area, with no large empty regions;
- consistent margins and gutters across a figure;
- pure white outer figure background for submitted or submission-like figures;
- compact gutters that keep panels visually close while preserving labels, legends and axis readability.
- visibly readable type at manuscript insertion size, with axis labels, tick labels, legends and colorbar labels not treated as afterthoughts;
- intentional stroke weight for axes, lines, boxplot outlines, violin outlines, error bars and marker edges.

If a source plot has a long y-axis label, reduce label distance, abbreviate terms or widen that panel. Do not solve label collisions by shrinking all text.

## Typography

Final composite figures must be readable at print size:
- panel letters larger than axis text;
- axis labels larger than tick labels;
- legends similar to tick labels;
- avoid very thin lines and tiny marker sizes;
- check readability after the figure is inserted into DOCX or PDF.

Do not scale font size with viewport width in generated web or HTML figures. Use stable dimensions and explicit font sizes.

## Color

Use restrained publication palettes:
- red and blue for opposing directions or treatments;
- grey for context and non-highlighted groups;
- one accent color per main biological or experimental class;
- avoid palettes dominated by only one hue unless the journal style clearly supports it;
- ensure color meanings remain consistent across figures.

Check that colors are distinguishable in greyscale when the data require it.

## Data-Rich Figure Types

When the dataset supports them, prefer richer figure panels over repeated simple bar charts:
- maps or coordinate plots for accession, sampling or geographic-distribution metadata;
- scatter or bubble plots for trait relationships and multi-variable ranking;
- box, violin or raincloud-style distributions for replicate-level variation;
- heatmaps for trait-by-line or gene-by-line matrices;
- two-dimensional density fields or contour plots for paired physiological spaces;
- 3D surfaces only when they clarify a continuous response surface and remain readable at print size.

Use these panels to answer distinct evidence questions. Do not add a complex plot only for decoration.

## Map Panels

Use data-bearing maps only when the user data include coordinates, regions, sampling sites, accession origins or spatial summaries.

Preferred implementation:
- use Cartopy, GeoPandas, Natural Earth, GADM, shapefiles, GeoJSON or another declared geospatial source;
- state or preserve the coordinate reference system when a projection or boundary file is used;
- use point size, colour or faceting only for variables present in the data;
- keep boundaries light and neutral so the user's data remain visually primary.

Avoid hand-drawn country or province outlines for manuscript maps. Use schematic maps only when the panel is explicitly conceptual, and label them as non-data schematics outside the formal manuscript if needed.

## Candy-Color Plus Premium-Gray Mode

Use this mode when the user asks for candy colors, soft colors, high-end gray, premium gray or a lighter but still publication-oriented figure style.

Recommended roles:
- candy colors: genotype, treatment subgroup, candidate class, workflow checkpoint or the one comparison that needs attention;
- premium gray: page background, panel border, grid line, axis, tick label, secondary text, neutral control and non-highlighted context;
- dark gray: main text, panel letters and key numerical labels.

Default candy accents:
- soft peach `#FFD59E`;
- soft pink `#FFB3BA`;
- candy blue `#BAE1FF`;
- mint `#BAFFC9`;
- lilac `#D7C7FF`.

Default premium grays:
- outer background `#FFFFFF`;
- panel fill `#FFFFFF`;
- panel/grid line `#D9DDE3`;
- neutral control `#C9CDD4`;
- main text `#2F3437`;
- muted text `#6F7782`.

Rules:
- do not flood the whole figure with candy colors;
- keep axes, grid lines, text and non-focal groups gray;
- assign one stable color to one stable category across all panels;
- use direct labels or a compact legend so the color mapping is not ambiguous;
- check print readability and grayscale separation before delivery.

## Editable Output

For journal figures:
- prefer editable vector output such as SVG or PDF for line art and plots;
- keep text as editable text where the plotting system supports it;
- export high-resolution PNG/TIFF previews only as secondary review files;
- preserve source panels separately from composites;
- keep plotting scripts or notebooks with stable input paths.

If a generated figure is only a style concept, redraw data-bearing panels from traceable source data before manuscript delivery.

## Captions

Captions should:
- start with a short figure title;
- define each panel in order;
- identify sample size, statistic, error bars and test where relevant;
- explain abbreviations not already obvious;
- avoid interpreting beyond the panel evidence.
- distinguish measured data panels from conceptual, synthesis or proposed-experiment panels.
- avoid method/QC titles such as `quality control`, `filtering logic`, `workflow`, `claim boundary` when a scientific title can state the result and scope.

## Visual QA

Before final delivery:
- inspect every source panel and composite figure;
- confirm no panel titles remain unintentionally;
- check axis-label distance and clipping;
- confirm legends do not cover data;
- check labels and numbers are not cropped;
- build a contact sheet for all main figures when there are many display items;
- keep source panels separate from final main figures.
- check that every figure caption has the format expected by the target journal, normally `Figure N. Title. A, ... B, ...`.
- ensure DOCX or PDF exports include all figures, matching captions, and accessible image descriptions when the format supports them.
- scan figure filenames, embedded labels and captions for old version tags, internal placeholders, local paths and project-management terms before packaging.

For high-impact submissions, also check whether:
- the first figure establishes the study system and primary evidence clearly;
- later figures add non-redundant evidence rather than variations of the same comparison;
- panel density is high enough for the venue but still readable at print scale;
- visual hierarchy moves from overview to quantitative comparison to validation or interpretation.
