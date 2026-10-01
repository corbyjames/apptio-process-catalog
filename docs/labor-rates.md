# Labor rates — how they are calculated, sourced, refreshed and reconciled

Method note for process group **06.4 Cost labor & capitalize**, records 06.4.1–06.4.3 and 06.4.10, and flows UC2 *Rates back* and UC1 *Actuals in*. Method-neutral (TBM / ITFM practice); Apptio Costing is the tool of record for rates. Assumes labor rosters are already loaded into Costing with salary + benefits for employees and contract rates for contractors. This is finance practice, not accounting advice; capitalization treatment should be confirmed with the controller and auditors.

## 1. Three kinds of rate, and which one leaves Costing

| Rate | What it is | Where it is used | Refreshed |
|---|---|---|---|
| **Actual loaded rate** (per person) | Base pay + variable pay + employer taxes + benefits (+ equity), or the contract rate, ÷ productive hours | Inside Costing only: monthly team cost, true-up, capitalization, GL tie-out | Monthly with close |
| **Standard rate** (per cell: band/level × location × employment type) | The rate finance issues: the cell's average actual loaded cost (or the salary-band midpoint), plus overhead uplift, ÷ productive hours; fixed for the year | Targetprocess planning, allocation costing, showback, business cases | Annually after the merit cycle; mid-year by exception |
| **Blended team rate** | Σ(FTE × standard rate of each member's cell) ÷ ΣFTE, or inside Costing the actual average of the team's members | Team-level costing of work where individual or band detail must not be exposed | With the card (standard) or monthly (actual) |

Finance does "hand out" a band rate, but it is derived from the roster, not invented: the derivation is 06.4.2 and the issue is 06.4.3. Which of the three is allowed to leave Costing is design decision **D-02 Rate exposure**. The mature pattern is hybrid: standard (or team-blended standard) rates go to Targetprocess; actual loaded cost stays protected in Costing and is used wherever the number must tie to the GL.

## 2. The calculation

For each cell *c* of the rate structure (band/level × role family × location × employment type):

```
loaded annual cost(person)  = base pay + variable pay + employer taxes + benefits (+ equity)
                              or contract rate × contracted hours          (contractors)
cell loaded cost(c)         = mean of loaded annual cost over people in c   (or band midpoint × (1 + burden %))
fully loaded cost(c)        = cell loaded cost(c) × (1 + overhead uplift %)
standard rate(c)            = fully loaded cost(c) ÷ productive hours(c)
```

- **Burden** (employer taxes, benefits) is usually taken as a percentage by country and employment type from the GL rather than per person, for privacy and because finance already books it that way. Contractors carry no benefits burden but may carry a procurement/management uplift.
- **Overhead uplift** (management, facilities, equipment, tooling) is a policy choice: either carried in the labor rate or left in the TBM tower allocation (06.1). Carry it in the rate when the rate is used for chargeback or business cases; leave it out when the rate is only used to spread team cost across work (it will reach the application through towers anyway). Never both.
- **Productive hours** = contracted hours − PTO − public holidays − training − admin/overhead time, by country and employment type. For a 2,080-hour year this is typically 1,650–1,800. Use HR policy as the divisor and validate it against timekeeping or utilization actuals once a year.
- **Unit of rate** follows decision **D-01 Labor effort signal**: per hour for timesheets; per FTE-month for story points, item count and fixed capacity (the per-point or per-item unit cost is derived monthly in 06.4.7 from team cost ÷ units completed); per allocation unit for planned work-effort units.
- **Thin cells**: below about five people the average exposes compensation and swings with every hire; roll the cell up to the parent band or region and record the roll-up rule in the structure (06.4.1).
- **Validation**: compute the actual rate per cell alongside the standard, compare both with the prior card and with external benchmarks (salary surveys, TBM Council), and raise an exception for any cell outside tolerance before the card goes to approval.

Worked example (one cell, employee, timesheets): mean base pay 120,000 + variable 10% = 132,000; burden 28% → 168,960; overhead uplift 12% → 189,235; productive hours 1,720 → **standard rate 110/hour**. If the same cell's actual average rises to 116/hour by month 6, the 5.5% drift is reported as a rate variance; it triggers a mid-year revision only if it persists (see §4).

## 3. Sources of data

| Source | Supplies | Lands in Apptio as |
|---|---|---|
| HRIS (Workday, SuccessFactors) | Person, job profile, band/level, role family, location, employment type, FTE, cost center, hire/termination dates; the band structure itself | Costing labor roster; Job Profile attributes |
| Payroll / GL | Actual base pay, variable pay, employer taxes and benefits (benefits usually as a burden % by country / employment type) | Loaded cost on the roster; burden reference table |
| VMS / procurement (Fieldglass, Beeline, SOW register) | Contractor and MSP rates, contracted hours, SOW terms | Contractor rows on the roster |
| Finance | Overhead pools (from TBM cost pools), capitalization policy, variance tolerances | Overhead uplift %, rate policy |
| HR policy | Standard hours, PTO, holiday calendars by country | Productive-hours reference table |
| Timekeeping / Targetprocess | Productive-hours actuals, utilization, effort by work item | Validation of the divisor; the effort distribution used in the true-up (UC1) |
| Benchmarks (salary surveys, TBM Council) | External rate ranges by role and region | Validation in 06.4.2 |

## 4. How often to recalculate

- **Standard rates: annually**, timed just after the merit/compensation cycle takes effect and before budget entry (operating calendar: fiscal months 8–9). Merit moves every cell at once; this is the one event that always warrants a new card.
- **Ordinary turnover does not trigger re-rating.** A leaver replaced at a different point in the band moves a thick cell by a fraction of a percent; the cell average absorbs it. Thin cells are rolled up precisely so that turnover cannot swing them.
- **Actual rates: monthly, for free.** The roster loads monthly and Costing recomputes team cost at close (06.4.7), so actuals always reflect turnover.
- **Mid-year revision by trigger, not by calendar.** 06.4.10 compares standard and actual per cell and team every month. Issue an effective-dated revision for a cell when (a) the actual drifts beyond tolerance (e.g. 5%) for two or three consecutive months, or (b) its headcount changes by more than 10–15% through reorganization, acquisition, offshoring or a contractor-to-employee conversion. Revise the affected cells only; never re-issue the whole card mid-year.

## 5. Keeping the accounting view and the portfolio view in sync

Treat the two views as deliberately different and reconcile them, rather than forcing them to agree. Portfolio operations (Targetprocess) value work at **standard** (rate × hours, or cost per point); the GL carries **actual** cost; the difference is a **rate variance** (standard vs actual rate) plus a **volume variance** (planned vs delivered effort). It is reported, never hidden, and standard-cost figures never post to the GL. Four mechanisms hold the views together:

1. **Monthly true-up (UC1, 06.4.7–06.4.9).** Costing takes the team's actual cost for the month and spreads it across the work the team completed using the effort distribution from Targetprocess (points, items, hours or allocations). Capitalization actuals and App TCO are therefore built on actuals while Targetprocess keeps showing standard.
2. **Reconciliation key team × month (06.4.10).** After the true-up, the sum of cost on work for a team must equal that team's actual cost for the month. Anything that does not tie is an unmapped person, a missing involvement or a stale team mapping, and is fixed in 04.1.x before close.
3. **Variance report per team (06.4.10).** Standard cost of work vs actual team cost, by month and year to date, with the rate and volume split. It is both the control and the trigger for the mid-year revision in §4; UC2's "true-up pattern" is this report feeding a re-publication.
4. **One rate card of record, versioned and effective-dated (06.4.3).** Both tools reference the card by version, so a plan built in March on card 2026.1 is compared with actuals without dispute about which rate was used. Prior versions are archived for audit.

If auditors require capitalized labor at actual cost, mechanism 1 provides it. If they accept standard rates with documented variance treatment, mechanism 3 is the documentation.
