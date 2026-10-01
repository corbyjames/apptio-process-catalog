"""Reviewer personas: the four roles a catalog review is run with, and how the catalog's
persona_list values map onto them. Customers override or extend these in their overlay
(`personas[]` in customer.json, same shape)."""
DEFAULT_PERSONAS = [
 {"key": "finance", "name": "Technology Finance & FP&A", "short": "Finance",
  "maps": ["IT Finance & FP&A", "Budget & cost-category owners"],
  "goals": "Own the budget of record, the labour rate card, variance and reforecast, and the capitalization numbers the auditors see.",
  "narrative": "Monthly: load actuals, reconcile the model to the GL, review standard-vs-actual labour variance, narrate variances and reforecast. Quarterly: re-plan with the portfolio. Annually, after the merit cycle: rebuild and approve the rate card, then run budget entry and review."},
 {"key": "tbm", "name": "TBM Office & Costing analysts", "short": "TBM",
  "maps": ["TBM Office & analysts", "FinOps practitioners", "Platform admins & integration"],
  "goals": "Keep the cost model, mappings, rates and data pipelines accurate so every allocation, TCO and showback figure can be defended.",
  "narrative": "Daily: data pipelines, anomalies, mapping fixes. Monthly: close the allocation run, compute team cost and blended CapEx, allocate to work or towers, publish TBM reporting, tie out team x month. Quarterly and annually: rate computation, benchmarks, taxonomy governance."},
 {"key": "portfolio", "name": "Portfolio & resource management", "short": "Portfolio",
  "maps": ["Portfolio management", "PMO & project managers", "Resource management", "Agile teams & RTEs", "HR & approvers", "Product management", "Requesters", "Engineering"],
  "goals": "Turn demand into funded, staffed, delivered work: intake, prioritization, capacity, allocations, effort capture, PI planning.",
  "narrative": "Daily: triage demand, keep allocations and timesheets current. Weekly / per sprint: flow, impediments, utilization. Monthly: balance demand vs capacity, position requests. Quarterly: PI planning, scenarios, commitments. Annually: workforce plan and headcount budget."},
 {"key": "leadership", "name": "Business-line leadership", "short": "Leadership",
  "maps": ["Executive leadership", "Business, app & service owners", "Vendor management & procurement"],
  "goals": "Decide what gets funded and staffed, see what technology costs the business line, and steer run vs change.",
  "narrative": "Monthly: operations review, cost review with the TBM office, showback. Quarterly: investment decisions, OP rationalization, capacity trade-offs. Annually: targets, budget approval, strategy refresh."},
]
MOMENTS = [("daily", "Daily / continuous", ["Continuous"]), ("weekly", "Weekly / sprint", ["Weekly"]), ("monthly", "Monthly", ["Monthly"]),
           ("quarterly", "Quarterly / PI", ["Quarterly"]), ("annual", "Annual", ["Annual / per cycle"]), ("event", "When triggered", ["Event-driven"])]
