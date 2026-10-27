// Lab cards, two per row in list order (keep each project's docs and replication cards adjacent).
// To add a card, append one object to this list and push; nothing else needs editing.
//   name: card title | description: one line | url: the project's own site | tags: optional short labels
window.PROJECTS = [
  {name: "jaxfne docs", description: "The documentation of jaxfne for biophysical source-field modeling.", url: "https://jaxfne.readthedocs.io/", tags: ["docs"]},
  {name: "jaxfne replications", description: "The replication and validation records of jaxfne.", url: "https://hnxj.github.io/jaxfne/", tags: ["replication"]},
  {name: "jnwb docs", description: "The documentation of jnwb for dataset-agnostic analysis of Neurodata Without Borders electrophysiology.", url: "https://jnwb.readthedocs.io/", tags: ["docs"]},
  {name: "jnwb replications", description: "The replication and validation records of jnwb.", url: "https://hnxj.github.io/jnwb/", tags: ["replication"]}
];
