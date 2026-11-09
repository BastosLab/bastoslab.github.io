# memory

Verified lessons the code and git do not show. This project only. No state, secrets, or unverified claims.

- trigger: a header-clearance probe selects the first element with a class that sits below the header
  cause: the .card block sits below the h1, so the probe measured the wrong box (lab/index.html: h1 at line 9, card-section at line 12)
  repair: select the heading at the top of the page and print the tag and text of the match
  evidence: this session's probe on lab/index.html measured the .card box (top 322 px) instead of the h1 (cap top 129 px at 390 px before the fix); commit 9cea4ce records the h1 measurement
  scope: header-clearance probes
