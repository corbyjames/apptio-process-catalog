# PI Planning/Enterprise Value Delivery Agent
## Consolidated General Business Requirements
## Author: Anuj Nath (IBM)
## 1. Purpose
Organizations conduct PI Planning to translate strategy and portfolio priorities into coordinated, achievable delivery commitments across products, Agile Release Trains, teams, shared services, platforms, funding sources, and technology dependencies.
Today, this process is often supported by disconnected tools, spreadsheets, planning boards, manual data reconciliation, meetings, and institutional knowledge. Considerable effort is required not only to construct the plan, but also to:
prepare work for planning;
identify and resolve dependencies;
align capacity and funding;
facilitate planning conversations;
assess risks and confidence;
communicate decisions;
track commitments;
coordinate execution; and
continuously connect delivery to strategic and business outcomes.
The purpose of the PI Planning/Enterprise Value Delivery Agent is to reduce this administrative and coordination burden while improving the quality, transparency, and predictability of planning and execution.
The agent must augment—not replace—the collaborative decisions made by product leaders, portfolio leaders, RTEs, STEs, Product Owners, architects, Scrum Masters, finance leaders, and delivery teams.
# 2. Product Vision
## 2.1 Vision Statement
The PI Planning/Enterprise Value Delivery Agent transforms PI Planning from a manually coordinated event into a continuously operating, AI-assisted value delivery intelligence capability that connects:
strategy
portfolios
products
customer outcomes
objectives and key results
planned work
teams and capacity
dependencies
funding
delivery activity
realized outcomes
The agent should not be positioned solely as a chatbot or an assistant that helps run a planning ceremony.
It should function as:
an intelligent planning copilot
an orchestration layer
a decision-support capability
an early-warning system
a facilitation assistant
an execution intelligence layer
a participant in a broader ecosystem of Product, Portfolio, Delivery, Workforce, and Financial agents
## 2.2 Core Value Proposition
The agent should help users answer five fundamental questions:
Are we ready to plan?
Is the proposed plan achievable and aligned?
What risks, dependencies, conflicts, and trade-offs require attention?
Are we delivering what we committed to deliver?
Is the work producing the intended strategic, customer, operational, and financial outcomes?
# 3. Guiding Principles
## 3.1 Human-in-the-Loop Decision-Making
The agent may:
analyze
summarize
recommend
draft
simulate
identify
prioritize
prompt
escalate
coordinate
The agent must not autonomously approve material planning, funding, scope, priority, objective, risk, or commitment changes unless explicitly authorized through configurable governance rules.
Human users must be able to:
accept
revise
reject
defer
override
agent recommendations
## 3.2 Facilitate Collaboration Rather Than Remove It
PI Planning creates value through shared understanding, negotiation, team commitment, and collective decision-making.
The agent should accelerate and improve these interactions without creating an anti-pattern in which plans or objectives are generated before teams have understood and committed to the intended outcomes.
## 3.3 Recommendations Must Be Explainable
For every material recommendation, the agent should explain:
what it identified
why it matters
what information was evaluated
which objectives, teams, investments, or commitments are affected
the confidence level of the recommendation
the proposed action
## 3.4 Recommendations Must Reflect Enterprise Context
The agent should support local organizational context, including:
planning methodology
customer journeys
product taxonomy
solution architecture
portfolio guardrails
investment categories
definitions of ready and done
risk and ROAM practices
capacity rules
objective-writing standards
funding policies
capitalization policies
security and compliance requirements
governance authorities
entity naming and hierarchy conventions
## 3.5 Configurable Operating Model
The agent must accommodate different:
industries
organizational structures
Agile maturity levels
planning cadences
terminology
entity models
team structures
planning tools
governance models
NOTE: It should not assume that every organization implements PI Planning or SAFe in exactly the same manner.
# 4. Target Users and Stakeholders
Primary users include:
Release Train Engineers
Solution Train Engineers
Product Managers
Product Owners
Portfolio Managers
Business Owners
Enterprise and Solution Architects
Engineering and Delivery Leaders
Scrum Masters
Team Leads
Finance and TBM Leaders
Workforce and Capacity Managers
PMO or Transformation Leaders
Executives
NOTE: Each user should receive insights appropriate to their role, authority, scope, and decision rights.
# 5. End-to-End Lifecycle
The agent must support five connected stages:
# 6. Strategy and Portfolio Preparation Requirements
## 6.1 Strategy-to-Work Traceability
The agent must validate the traceability chain across:
Strategic Objective → Portfolio Priority → Product or Value Stream → PI Objective → Epic → Feature → Story → Delivery → Outcome
The agent should identify:
strategic objectives with no supporting execution
investments with weak strategic alignment
PI objectives with insufficient supporting Features
Features with no business or strategic linkage
delivered work with no defined outcome
breaks or inconsistencies in the hierarchy
changes in work that weaken previously established alignment
### Agent outcome
Continuous strategy-to-execution traceability.
## 6.2 Portfolio Opportunity and Epic Discovery
The agent should analyze portfolio-level opportunities, epics, initiatives, and investment proposals to identify:
materially similar opportunities
overlapping investments
potential duplicate initiatives
teams independently pursuing similar outcomes
opportunities for consolidation
related work that should be coordinated
existing capabilities that may make proposed work unnecessary
The analysis should use more than exact title matching and should consider:
descriptions
expected outcomes
customer journeys
architecture
affected capabilities
target users
products
business processes
planned benefits
### Agent outcome
NOTE: Reduced duplicate investment and improved portfolio coordination.
## 6.3 Work Decomposition Assistance
The agent should assist users in decomposing:
opportunities into portfolio epics
portfolio epics into Features
Features into Stories or other executable work
strategic outcomes into measurable PI objectives
large work items into sequenced delivery increments
NOTE: The agent may draft suggested work items, but users must determine whether they are appropriate before creation or synchronization with delivery tools.
### Agent outcome
Faster and more consistent preparation of executable work.
# 7. Pre-PI Planning Requirements
Pre-PI Planning is expected to be the most manually intensive phase and should be a primary focus of the initial solution.
## 7.1 PI Readiness Assessment
The agent must automatically identify:
missing Features, Stories, or required work items
incomplete descriptions or acceptance criteria
missing owners
missing estimates
missing team assignments
missing target iterations or dates
unresolved dependencies
absent or weak business outcomes
work that does not meet the organization’s definition of ready
overallocated teams
insufficient planned work
unsupported PI objectives
architecture or security prerequisites that are not ready
required decisions that remain unresolved
external approvals with insufficient lead time
The readiness assessment should be available at:
team
ART
Solution Train
product
portfolio
enterprise levels
NOTE: The agent should calculate a readiness score and explain the factors that influenced it.
### Agent outcome
A transparent and actionable PI readiness score.
## 7.2 Readiness Resolution Recommendations
NOTE: The agent should not only report that an item is unready. It should recommend how to resolve the issue.
Examples include:
assign an owner
add an estimate
clarify acceptance criteria
split an oversized Feature
create missing predecessor work
initiate an architecture or security review
move the work to a later PI
identify a team capable of delivering the work
draft a missing work item
escalate an unresolved decision
### Agent outcome
Faster closure of readiness gaps.
## 7.3 Dependency Discovery and Intelligence
The agent must analyze:
initiatives
epics
Features
Stories
technical components
architecture relationships
teams
shared services
shared platforms
delivery dates
historical dependencies
work across value streams
It should identify:
cross-team dependencies
cross-ART dependencies
cross-portfolio dependencies
blocked work
missing predecessor work
sequencing conflicts
unrecorded or implied dependencies
shared-service contention
platform bottlenecks
dependencies with insufficient lead time
dependency ownership gaps
aging dependencies
dependencies likely to affect multiple objectives
NOTE: The agent should produce a dynamic dependency graph and a prioritized dependency heatmap.
### Agent outcome
Earlier detection and proactive management of dependency risk.
## 7.4 Capacity and Workforce Validation
The agent should evaluate:
historical velocity and throughput
planned and actual allocations
available workforce
leave and holidays
skills and roles
shared-team demand
planned non-delivery work
operational support obligations
carryover
team stability
historical capacity accuracy
relevant constraints
It should identify:
overcommitted teams
underutilized capacity
unrealistic planning assumptions
skill shortages
shared-resource conflicts
sprint-level overload
excessive work in progress
work that cannot reasonably fit within the PI
NOTE: The agent should recommend capacity adjustments but preserve RTE, Scrum Master, or authorized team ownership of final capacity values.
### Agent outcome
More achievable commitments and more reliable capacity forecasts.
## 7.5 Financial and Investment Alignment
Where financial data is available, the agent should integrate with ApptioOne or other financial systems to evaluate:
approved funding
portfolio allocation
labor and non-labor cost
cloud and infrastructure cost
capitalization implications
investment guardrails
budget versus planned work
forecast versus actual cost
product or value-stream funding
financial exposure associated with delivery risk
The agent should identify:
unfunded commitments
work outside approved investment priorities
potential funding shortfalls
underfunded strategic objectives
investments with weak outcome linkage
financial impacts of replanning
capitalization or accounting issues requiring review
### Agent outcome
Plans that are both operationally and financially feasible.
## 7.6 Objective Preparation and Quality Analysis
The agent should help teams develop PI objectives without replacing collaborative objective-setting.
It should:
prompt teams with questions
summarize the work being considered
draft candidate objectives
recommend measurable outcomes
identify objectives that are too vague
detect objectives written as tasks rather than outcomes
identify objectives with no measurement method
identify duplicate objectives across teams
assess strategic and OKR alignment
verify that sufficient Features support each objective
identify planned work not represented by an objective
help roll team objectives into ART or program objectives
### Agent outcome
Clearer, measurable, outcome-oriented PI objectives.
# 8. During PI Planning Requirements
## 8.1 Live Planning Copilot
The agent should act as a real-time:
planning facilitator
dependency analyst
capacity advisor
objective-quality advisor
risk analyst
scenario-modeling capability
recorder of decisions
action coordinator
source of contextual information
NOTE: The agent should assist participants within their existing planning workflow rather than require a completely separate planning experience.
## 8.2 Real-Time Impact Analysis
When users change:
scope
sequencing
iteration placement
team ownership
capacity
priority
estimates
dependencies
objectives
delivery dates
the agent should immediately assess the impact on:
upstream and downstream work
other teams and ARTs
objectives and key results
roadmap milestones
capacity
cost and funding
architecture
delivery commitments
confidence
customer outcomes
regulatory or operational obligations
### Agent outcome
Immediate visibility into the consequences of planning changes.
## 8.3 Conflict and Duplicate Work Detection
The agent should detect:
competing priorities
duplicate work
overlapping Features
incompatible sequencing
resource conflicts
dependency mismatches
roadmap conflicts
multiple teams changing the same capability
objectives competing for the same capacity
inconsistent plans across tools
The agent should recommend potential resolutions such as:
consolidate
re-sequence
reassign
defer
split
escalate
obtain an explicit business decision
### Agent outcome
Reduced planning confusion and fewer hidden conflicts.
## 8.4 Scenario and Trade-Off Analysis
The agent should support scenarios such as:
What happens if a team loses 20% of its capacity?
What happens if a critical Feature slips by two iterations?
What changes if Objective A is prioritized over Objective B?
What happens if security approval takes four additional weeks?
What happens if a shared platform cannot support all planned demand?
What are the financial consequences of moving scope to the next PI?
What is the minimum scope required to preserve the customer outcome?
Which commitments are most exposed to a specific dependency?
Scenarios should compare:
strategic impact
customer impact
capacity
cost
risk
dependencies
delivery timing
confidence
expected outcomes
### Agent outcome
Evidence-based trade-off decisions.
## 8.5 Risk and ROAM Facilitation
The agent should:
detect emerging risks
identify risks not explicitly entered by teams
link risks to objectives, Features, dependencies, and commitments
recommend ROAM classifications
identify risk owners
draft mitigation actions
monitor aging
detect changes in severity
identify risks requiring escalation
track accepted and mitigated risks
summarize risk exposure across the ART or Solution Train
NOTE: The agent must allow authorized users to approve or modify risk classifications and mitigation decisions.
### Agent outcome
Consistent and proactive risk management.
## 8.6 Confidence Vote Intelligence
The agent should support confidence voting by:
summarizing unresolved risks and dependencies before voting
identifying teams or objectives with low confidence
explaining likely drivers of low confidence
correlating votes with capacity, risk, readiness, and dependency data
identifying material differences between team and leadership confidence
recording remediation actions after a low-confidence vote
tracking whether concerns were resolved
comparing confidence with actual delivery performance over time
### Agent outcome
Confidence votes that are explainable and actionable.
## 8.7 Decision and Action Capture
The agent should capture:
decisions
assumptions
risks
dependencies
commitments
owners
due dates
unresolved questions
changes to scope
management-review actions
NOTE: It should draft or update the corresponding records in the appropriate systems after human approval.
### Agent outcome
Reduced loss of decisions and follow-up actions across planning sessions.
# 9. Post-PI Planning and Execution Requirements
## 9.1 Commitment Baseline
At the conclusion of PI Planning, the agent should create a governed baseline containing:
committed and uncommitted objectives
planned Features and milestones
team and ART commitments
capacity assumptions
accepted risks
unresolved dependencies
funding assumptions
delivery dates
confidence results
known constraints
The baseline must preserve an auditable record of what was agreed.
## 9.2 Continuous Commitment Validation
During execution, the agent should continuously evaluate:
actual velocity and throughput
planned versus actual progress
objective status
Feature completion
slippage
blocked dependencies
scope changes
capacity changes
funding changes
quality issues
carryover risk
delivery confidence
changes in expected outcomes
The agent should distinguish between:
normal execution variation
emerging risk
likely missed commitment
confirmed scope or commitment change
### Agent outcome
NOTE: An early-warning system for commitments and outcomes.
## 9.3 Predictive ART and Solution Train Health
The agent should monitor:
objective predictability
flow time
flow efficiency
flow load
work in progress
dependency aging
blocked time
carryover
defect trends
capacity variance
team overload
objective slippage
delivery risk
recurring bottlenecks
It should answer:
What leadership conversation should occur today or this week?
### Agent outcome
NOTE: Continuous and prioritized delivery health intelligence.
## 9.4 RTE and STE Daily Briefing
The agent should provide a configurable briefing containing:
new or escalating risks
slipping objectives
dependency changes
capacity concerns
teams requiring attention
pending decisions
overdue actions
unresolved ownership
approaching milestones
demo readiness
confidence changes
recommended escalations
Users should be able to drill from the briefing into the supporting data.
### Agent outcome
Less time searching for issues and more time leading resolution.
## 9.5 Continuous Replanning
When conditions materially change, the agent should propose:
reprioritization
reallocation
resequencing
scope reduction
team reassignment
dependency resolution
revised target dates
revised funding
escalation
NOTE: The agent should show the impact of each alternative before a decision is made.
### Agent outcome
Adaptive planning without waiting for the next formal PI event.
# 10. Ceremony and Facilitation Support
## 10.1 Iteration Review and System Demo Preparation
The agent should identify:
significant completed Features
customer-facing outcomes
high-value demo candidates
work that best demonstrates progress toward objectives
teams missing demo submissions
incomplete demo information
relevant metrics
risks or lessons that should be discussed
It should draft:
demo agendas
outcome summaries
speaker notes
executive highlights
## 10.2 Inspect and Adapt Assistant
The agent should aggregate:
missed objectives
carryover
dependencies
risks
defects
blockers
capacity variance
estimation variance
flow metrics
retrospective observations
It should identify patterns such as:
recurring dependency failures
chronic estimation inaccuracy
repeated overcommitment
persistent shared-service bottlenecks
common causes of missed objectives
quality-related delivery delays
ineffective mitigation patterns
It should propose improvement themes and draft measurable improvement actions.
## 10.3 Retrospective Assistance
The agent should:
summarize significant events
identify recurring themes
distinguish systemic issues from isolated events
recommend discussion topics
draft improvement experiments
connect retrospective findings to objective and delivery results
track whether prior improvement actions were completed
NOTE: The agent must support psychological safety and should not generate individual performance judgments from team delivery data.
# 11. Cross-ART and Enterprise Coordination
The agent should identify and support coordination across:
ARTs
Solution Trains
shared services
shared platforms
products
portfolios
architecture teams
external providers
It should detect:
ART-to-ART dependency hotspots
shared-team contention
strategic objective overlap
platform bottlenecks
sequencing conflicts
competing demand for scarce skills
shared external dependencies
risks affecting multiple value streams
### Agent outcome
Enterprise-level visibility beyond individual team or ART boundaries.
# 12. Reporting, Analytics, and Communications
## 12.1 Executive and Operational Reporting
The agent should produce or support:
readiness scores
PI confidence
delivery confidence
objective status
dependency heatmaps
capacity heatmaps
financial exposure
strategic alignment
roadmap status
commitment status
risk exposure
value-stream performance
flow metrics
outcome realization
cross-ART health
Reporting should be role-based and explainable.
## 12.2 BI Integration
The agent should operate as part of or alongside the enterprise BI layer.
Users should be able to:
interrogate planning and delivery data conversationally
ask why a metric changed
identify drivers of a trend
compare ARTs, products, or PIs
evaluate flow metrics
identify anomalies
request recommended actions
navigate from an insight to the underlying work
NOTE: The agent should supplement—not replace—governed BI reporting.
## 12.3 Stakeholder Communication Drafting
Using approved enterprise data, the agent should draft:
PI summaries
ART updates
executive briefs
dependency escalations
risk escalations
decision requests
milestone updates
outcome summaries
demo communications
post-planning recaps
NOTE: The user must review and approve external or executive communications before distribution.
# 13. Agent Architecture
## 13.1 Multi-Agent Ecosystem
The PI Planning Agent should be capable of operating within a broader ecosystem that may include:
Portfolio Agent
Product Agent
Strategy Agent
Delivery Agent;
Workforce Agent
Financial Agent
Architecture Agent
Risk Agent
Value Realization Agent
The PI Planning Agent should orchestrate context and recommendations across these domains without duplicating every specialized capability.
## 13.2 MCP and Extensibility
The architecture should support an MCP-based or equivalent extensibility model that enables:
controlled access to approved tools and data
customer-specific agents
configurable business logic
local skills and prompts
extension of supported ceremonies
integration with enterprise services
role-based tool access
auditable actions
## 13.3 Local Context and Knowledge
The agent should be grounded in approved organizational information such as:
customer journeys
solution architectures
product documentation
policies
portfolio guardrails
planning playbooks
naming conventions
objective templates
historical decisions
definitions of ready and done
financial rules
delivery governance
Local context should be version-controlled, governed, and attributable.
# 14. Integration Requirements
## 14.1 Core Systems
## 14.2 Data Synchronization
The agent must account for:
entities stored in different systems
delayed synchronization
conflicting records
renamed entities
incomplete integrations
duplicate records
source-of-truth rules
two-way integration governance
differences between planning and execution hierarchies
The agent must disclose when recommendations are affected by missing, stale, or conflicting data.
# 15. Governance, Security, and Trust Requirements
The solution must provide:
role-based access control
enterprise authentication
data entitlements
separation of duties
approval workflows
complete action history
recommendation traceability
data-source attribution
confidence indicators
configurable autonomy
protection of sensitive financial, workforce, and delivery data
customer-specific data isolation
retention controls
model and prompt governance
monitoring for inappropriate or unsupported recommendations
The agent should never present a recommendation as fact when the supporting data is incomplete or uncertain.
# 16. Nonfunctional Requirements
The agent should be:
responsive enough to support live PI Planning
scalable across large portfolios, ARTs, teams, and work-item volumes
resilient to incomplete data
configurable without excessive custom development
observable and supportable
auditable
explainable
accessible through multiple workflows
capable of asynchronous analysis
capable of proactive alerts
able to work across renamed or customized entity types
able to operate without materially degrading the performance of Targetprocess or connected platforms
# 17. Success Measures
The solution should be evaluated using measurable outcomes.
## 17.1 Planning Efficiency
Reduction in time spent preparing for PI Planning
Reduction in manual board validation
Reduction in spreadsheet reconciliation
Reduction in time spent identifying dependencies
Reduction in planning administration
Reduction in time spent preparing reports and communications
## 17.2 Plan Quality
Percentage of work meeting readiness criteria before PI Planning
Reduction in missing estimates, owners, dependencies, or assignments
Improvement in objective quality
Reduction in duplicate or overlapping work
Improvement in capacity forecast accuracy
Reduction in unplanned carryover
## 17.3 Execution Predictability
Improvement in PI objective predictability
Improvement in commitment delivery
Earlier identification of slippage
Reduction in blocked dependency duration
Reduction in aging risks
Improvement in confidence-to-delivery correlation
## 17.4 Strategic and Financial Alignment
Percentage of work traceable to strategic objectives
Percentage of PI objectives with measurable outcomes
Percentage of investment linked to approved priorities
Reduction in unfunded or misaligned commitments
Improvement in visibility from funding to delivery and outcomes
## 17.5 Leadership Productivity
Reduction in RTE/STE time spent assembling information
Reduction in manual ceremony preparation
Reduction in time spent creating executive updates
Increase in risks resolved before affecting commitments
Increase in proactive versus reactive interventions
# 18. Proposed Capability Prioritization
## MVP / Foundational Release
PI readiness assessment and scoring

Readiness resolution recommendations

Dependency discovery and visualization

Capacity validation and recommendations

PI objective drafting and quality analysis

Live planning copilot

Real-time impact analysis

Risk and ROAM facilitation

Commitment baseline and tracking

Executive and RTE operational briefings

Human approval and governance controls

Targetprocess and Jira/ADO integration
## Second Release
Confidence vote intelligence

Cross-ART coordination

Portfolio duplicate and overlap analysis

Work decomposition assistance

Predictive ART health

Continuous traceability

BI integration

Stakeholder communication drafting

System demo preparation

Continuous replanning
## Strategic Expansion
Multi-agent ecosystem

Inspect and Adapt assistant

Financial and funding intelligence

Workforce and skills optimization

Architecture intelligence

Enterprise-wide value realization

Extensible MCP-based customer agents

Continuous enterprise value delivery intelligence
# 19. Consolidated Outcome Statement
The solution should move organizations from:
manually prepared plans
fragmented planning artifacts
reactive dependency management
capacity assumptions
weak objective quality
delayed risk recognition
manual reporting
disconnected funding
limited strategy-to-delivery traceability
event-based planning
to:
continuously assessed readiness
dynamic dependency intelligence
capacity-aware commitments
measurable and aligned objectives
explainable confidence
proactive risk resolution
continuous commitment monitoring
integrated financial and delivery visibility
adaptive replanning
coordinated cross-ART execution
enterprise value delivery intelligence
20. OPPORTUNITY
The ultimate opportunity is not simply to use AI to run PI Planning.
The opportunity is to establish an operational intelligence and orchestration layer connecting strategy, products, work, teams, dependencies, funding, delivery, and measurable outcomes across the full value delivery lifecycle.

Lifecycle stage | Primary agent role
Strategy and portfolio preparation | Translate strategy and investment priorities into planning context
Pre-PI Planning | Assess readiness and prepare an achievable planning baseline
During PI Planning | Facilitate, analyze, coordinate, and support decisions in real time
Post-PI Planning and execution | Track commitments, risks, dependencies, flow, and outcomes
Inspect, adapt, and continuously replan | Identify patterns, propose improvements, and maintain alignment

System | Purpose
Targetprocess | Strategy, portfolio, product, work hierarchy, planning and PI structure
Jira | Team execution, Stories, sprint data, dependencies and delivery status
Azure DevOps | Work execution, backlog, sprint and delivery information
GitHub | Development activity, pull requests, code delivery and engineering signals
ApptioOne | Funding, cost, investment, labor, budget and financial alignment
HR and workforce systems | Capacity, availability, roles, skills and organizational assignments
BI platforms | Governed analytics, metrics and reporting
Architecture repositories | Solution components, technical dependencies and standards
Miro or collaborative planning tools | Planning artifacts, workshop inputs and breakout-session information
Communication platforms | Approved notifications, briefings, actions and escalations

Capability | General Requirements | General Requirements | Customer 1 | Customer 2 | Customer 3 | Customer 4 | Customer 5 | Overall Priority
Readiness Assessment | Readiness Assessment | ✓ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | Very High
Dependency Discovery | Dependency Discovery | ✓ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | Very High
Capacity Validation | Capacity Validation | ✓ | ★★ | ★★ | ★★★ | ★★ | ★★ | High
Financial Alignment | Financial Alignment | ✓ | ★ | ★ | ★ | ★★ | ★★ | Medium
PI Objective Creation | PI Objective Creation | Partial | ★ | ★ | ★★★ | ★★★ | ★ | Very High
PI Objective Quality | PI Objective Quality | No | ★ | ★ | ★★ | ★★★ | ★ | High
Roadmap Visualization | Roadmap Visualization | No | ★ | ★★★ | ★★ | ★★ | ★★ | High
OKR Alignment | OKR Alignment | ✓ | ★ | ★★★ | ★★ | ★★★ | ★★★ | High
Duplicate Work Detection | Duplicate Work Detection | Partial | ★★★ | ★ | ★ | ★★ | ★★ | High
Portfolio Epic Discovery | Portfolio Epic Discovery | No | ★★★ | ★ | ★★ | ★★ | ★ | High
Commitment Tracking | Commitment Tracking | Partial | ★ | ★★★ | ★★ | ★★★ | ★★★ | Very High
Confidence Vote Intelligence | Confidence Vote Intelligence | No | ★ | ★ | ★★ | ★★★ | ★ | Medium-High
Risk / ROAM Management | Risk / ROAM Management | Partial | ★★ | ★★★ | ★★ | ★★★ | ★★★ | Very High
Predictive ART Health | Predictive ART Health | No | ★ | ★ | ★ | ★★★ | ★ | High
Cross-ART Coordination | Cross-ART Coordination | Partial | ★ | ★★ | ★ | ★★★ | ★★ | High
Executive Reporting | Executive Reporting | ✓ | ★ | ★★★ | ★ | ★★★ | ★★★ | High
Executive Communications | Executive Communications | No | ★ | ★ | ★ | ★★★ | ★★★ | Medium-High
Inspect & Adapt Assistant | Inspect & Adapt Assistant | No | ★ | ★ | ★ | ★★★ | ★★★ | Medium-High
Demo Preparation | Demo Preparation | No | ★ | ★ | ★ | ★★★ | ★★★ | Medium
Continuous Traceability | Continuous Traceability | Partial | ★ | ★★ | ★ | ★★★ | ★★★ | High
AI Planning Copilot | AI Planning Copilot | Partial | ★★ | ★★ | ★★★ | ★★★ | ★★★ | Very High
Multi-Agent Ecosystem | Multi-Agent Ecosystem | No | ★ | ★ | ★ | ★★★ | ★ | Strategic