# Diagram and visualization guidance

Choose visuals because they improve technical understanding.

## Suggested mapping
- Algorithms: flowcharts, pseudocode, trace tables, complexity tables.
- Data structures: labeled node/link/tree diagrams.
- IoT/embedded systems: system architecture, block diagrams, data flow; circuit diagrams only when connections are specified.
- Networking: topology and protocol-layer diagrams.
- Cybersecurity: threat models, trust boundaries, security architecture.
- Databases: ER diagrams and schema diagrams.
- ML/data science: pipeline diagrams and charts based on real data.
- Research projects: methodology flowcharts, literature matrices, test setup diagrams.
- Experimental work: charts from actual supplied measurements, with axes, units, legends, and method.

## Rules
- Prefer Mermaid for text-defined flowcharts and simple diagrams; Graphviz for graph layouts.
- Use Python/Matplotlib for charts from actual numerical data.
- Never fabricate measured results to fill a graph.
- Mark illustrative data explicitly if synthetic data is necessary for demonstrating a chart.
- Label all components, arrows, units, and figure numbers clearly.
- Refer to each important figure in the body text.
- Do not call a conceptual drawing a validated circuit or production-ready design.
- For circuit diagrams, ask for exact components, pin assignments, voltage levels, and platform when needed.
- If rendering tools are unavailable, include a textual diagram or source definition and disclose the limitation.
