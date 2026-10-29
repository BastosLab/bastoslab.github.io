// Lab cards, grouped by section (webpages on top, presentations on bottom).
// To add a card, run: python3 artifacts/tools/add_card.py --subject "..." --desc "..." --url "..."
// Or append one object to this list.
// Schema:
//   subject: card title / topic
//   description: one- or two-line summary
//   url: destination link (https://...)
//   image: path to thumbnail image (e.g. assets/preview.png or https://...)
//   category: "webpage" (top section) or "presentation" (bottom section)
//   tags: optional array of short labels
window.PROJECTS = [
  {subject: "jaxfne docs", name: "jaxfne docs", description: "The documentation of jaxfne for biophysical source-field modeling.", url: "https://jaxfne.readthedocs.io/", image: "../assets/favicon.png", category: "webpage", tags: ["docs"]},
  {subject: "jaxfne replications", name: "jaxfne replications", description: "The replication and validation records of jaxfne.", url: "https://hnxj.github.io/jaxfne/", image: "../assets/favicon.png", category: "webpage", tags: ["replication"]},
  {subject: "jnwb docs", name: "jnwb docs", description: "The documentation of jnwb for dataset-agnostic analysis of Neurodata Without Borders electrophysiology.", url: "https://jnwb.readthedocs.io/", image: "../assets/favicon.png", category: "webpage", tags: ["docs"]},
  {subject: "jnwb replications", name: "jnwb replications", description: "The replication and validation records of jnwb.", url: "https://hnxj.github.io/jnwb/", image: "../assets/favicon.png", category: "webpage", tags: ["replication"]},
  {subject: "jnwb: Agent-Assisted Ephys", name: "jnwb: Agent-Assisted Ephys", description: "Dataset-agnostic electrophysiology analysis and verifiable agent tools.", url: "/slides/jnwb/", image: "/slides/jnwb/thumb.png", category: "presentation", tags: ["slides"]},
  {subject: "JaxFNE: Spectrolaminar Dynamics", name: "JaxFNE: Spectrolaminar Dynamics", description: "Tensor-field neural equations, oscillations, and laminar LFP microcircuits.", url: "/slides/jaxfne/", image: "/slides/jaxfne/thumb.png", category: "presentation", tags: ["slides"]}
];
