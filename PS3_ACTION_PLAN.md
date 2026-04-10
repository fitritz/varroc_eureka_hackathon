# PS3 Detailed Action Plan (PPT First, Implementation After Selection)

## 0. Delivery Model (Important)

This project will run in two stages:

1. Stage 1: PPT submission with complete idea (current requirement).
2. Stage 2: Full implementation only if PPT is shortlisted/selected.

Current focus is Stage 1 only.

## 1. Goal and Scope

Build a production-oriented proof of concept for PS3 (Accurate Two-Wheeler Driving Behavior Score) that is:

- Explainable: every score change has a human-readable reason.
- Fair: context-aware normalization reduces unfair penalties.
- Reliable: robust to sensor noise, mount variation, and GPS dropout.
- Measurable: baseline vs improved approach with quantitative evidence.

Out of scope:

- Hardware manufacturing
- Full insurance backend integration
- City-scale deployment operations

## 1A. Competitive Intelligence Goal (Selection Critical)

Because shortlist probability is extremely low, the proposal must prove that we understand why many prior telematics-style solutions fail.

Required narrative outputs for Stage 1:

- Existing solution categories and practical limitations.
- Failure-mode-to-mitigation mapping in our architecture.
- Measurable differentiation (fairness, reliability, explainability, anti-gaming).

## 2. Problem Definition

Input:

- IMU streams (accelerometer + gyroscope)
- GPS stream (speed, heading, coordinates)
- Optional context (map speed limits, road roughness indicators)

Output:

- Event timeline with severity and confidence
- Segment and trip safety score (0 to 100)
- Explainability log for each score adjustment
- Coaching recommendations by event type and frequency

Primary event taxonomy:

1. Harsh braking
2. Aggressive acceleration
3. Risky cornering
4. Overspeeding against posted limit
5. Weaving / unstable lane behavior proxy
6. Phone usage proxy (if available from app interaction)

## 2A. Existing Solutions and Observed Failure Patterns

Common existing approaches:

1. Rule-only telematics systems
2. Smartphone score apps
3. Fleet behavior dashboards
4. Proprietary ML-first insurance scoring

Frequent shortcomings:

- Excess false positives under sensor noise and vibration.
- Mount-position sensitivity causing inconsistent event detection.
- Weak context handling (traffic/road conditions ignored).
- Opaque scoring decisions with low rider trust.
- Limited stress testing under tunnel/dropout/rough-road scenarios.

Our design response:

- Confidence-gated penalties.
- Context normalization.
- Mount calibration and repeatability checks.
- Event-level evidence for every score change.
- Replay-based benchmarking under fixed scenarios.

## 3. Scoring Strategy

Final score formula:

Score = Base - RiskPenalty + SafetyBonus - DataQualityPenalty

Where:

- Base: 100
- RiskPenalty: weighted sum of normalized risky events
- SafetyBonus: sustained smooth riding and compliant speed behavior
- DataQualityPenalty: uncertainty penalties when data quality is poor

Guardrails:

- Score clamp to 0 to 100
- No single event can drop more than configured cap per minute
- Penalties scaled by confidence and event persistence
- Context normalization for traffic density and road quality

Additional reliability guardrails:

- Low-confidence events contribute only partial penalty.
- Sudden isolated spikes must pass persistence logic before severe tagging.
- Repeated threshold-edge behavior triggers anti-gaming escalation.
- If signal confidence is below threshold, cap penalties and mark event as uncertain.

## 4. System Architecture

Modules:

1. Ingestion

- Collect IMU and GPS with synchronized timestamps.
- Validate ranges and sampling consistency.

2. Preprocessing

- Low-pass filtering and outlier suppression.
- Orientation normalization and gravity compensation.
- Resampling to a common timeline.

3. Event Detection Engine

- Rule-based detectors with thresholds and hysteresis.
- Feature windows for temporal consistency.
- Severity and confidence assignment.

4. Context Engine

- Speed limit mapping.
- Traffic and road roughness adjustments (if available).
- Confidence downgrades under poor signal conditions.

5. Hybrid Risk Model

- Lightweight ML model using event and context features.
- Outputs risk likelihood for each segment.
- Combined with physics constraints and rules.

6. Scoring and Explainability

- Convert events to score impacts.
- Generate plain-language explanations.
- Build trip summary and coaching suggestions.

7. Reporting Layer

- Timeline chart of events and score drift.
- Segment risk hotspots.
- Rider improvement recommendations.

8. Fairness and Reliability Diagnostics

- Score distribution by mount type, road class, and signal quality bands.
- Stability report using repeated-route replay.

9. Benchmark and Replay Harness

- Fixed scenario packs for heavy traffic, rough roads, GPS dropouts, and aggressive maneuvers.
- Baseline vs hybrid comparison with identical inputs.

## 5. Data Plan

### 5.1 Data Collection

Collect representative rides across:

- Urban traffic
- Suburban roads
- Highways
- Rough roads and pothole-heavy routes
- Day and night conditions

Minimum dataset target:

- Phase 1 (baseline-ready): 100 to 150 trips, 30+ riders, 3+ mount positions
- Phase 2 (DL-ready): 1000+ ride hours across 8 to 12 Indian cities

India-specific capture requirements:

- Temporary diversions and rerouted corridors
- Potholes and speed-breaker-heavy segments
- Monsoon and post-rain conditions
- Day, night, and high-traffic festival windows

### 5.2 Labeling

Create event labels using:

- Rule-assisted pre-labeling
- Human review for ambiguous windows
- Severity tags (low, medium, high)

Scale labeling plan:

- Use weak labels from rule engine for all rides.
- Use active learning to send only uncertain windows for manual review.
- Re-train in cycles so annotation effort focuses on high-value edge cases.

### 5.3 Data Quality Controls

Reject or down-weight segments with:

- GPS drift spikes
- IMU dropout or clipping
- Unrealistic acceleration values
- Time sync mismatch beyond threshold

### 5.4 Drift Monitoring and Refresh Policy

Monitor drift across:

- City distribution shifts
- Seasonal shifts (especially monsoon vs dry)
- Device and mount profile shifts

Refresh policy:

- Monthly drift check with trigger thresholds.
- Retrain when drift exceeds threshold or severe-event false positives rise.
- Maintain previous model fallback until new model passes regression gates.

## 6. Stage 1 Plan: PPT Submission (Current)

## Phase 0: Competitive Teardown (New, before slide finalization)

Deliverables:

- Existing-solution landscape table.
- Prior-model failure matrix (technical + product + adoption).
- Differentiation claims mapped to concrete design controls.

Exit criteria:

- Team can answer "Why older models fail" with evidence and architecture links.

## Phase 1A: Story and Problem Framing

Deliverables:

- Crisp problem statement and motivation for PS3
- Why existing solutions are insufficient
- Clear value proposition and differentiation

Exit criteria:

- One-slide executive summary is complete and reviewer-friendly

## Phase 1B: Solution Blueprint for PPT

Deliverables:

- End-to-end architecture slide
- Event taxonomy slide with severity logic
- Scoring formula and explainability design slide
- Context-awareness and fairness strategy slide

Exit criteria:

- All major design choices are explained visually and verbally

## Phase 1C: Validation and Feasibility Narrative

Deliverables:

- Metrics definition slide (what will be measured and why)
- Test strategy slide (unit, integration, scenario)
- Risk and mitigation slide
- Implementation roadmap slide (post-selection)

Exit criteria:

- PPT convincingly answers: feasibility, reliability, and business impact

Add mandatory proof narrative:

- Why score fairness remains stable across mount and signal conditions.
- How confidence gating prevents brittle penalties.
- How anti-gaming logic prevents score manipulation.

## Phase 1D: Final PPT Packaging

Deliverables:

- Final 10 to 14 slide deck
- Speaker notes for each slide
- 3 to 5 minute pitch flow
- Q&A backup slides (assumptions, constraints, roadmap)

Exit criteria:

- Team can present full idea clearly without code demo

## 7. Stage 2 Plan: Implementation (Only if Selected)

## Phase 2A: Foundation (Week 1 after selection)

Deliverables:

- Final event taxonomy and thresholds v1
- Data schema and logging format frozen
- Ingestion plus preprocessing pipeline
- Baseline detector stubs and unit tests

Exit criteria:

- Can ingest and preprocess a full trip file reliably
- Timestamp synchronization error within defined tolerance

## Phase 2B: Baseline Scoring (Week 2)

Deliverables:

- Rule-based event detectors fully implemented
- Baseline scoring engine (trip and segment)
- Explainability messages for every event
- Baseline dashboard/report output

Exit criteria:

- Baseline runs end-to-end on validation set
- All score changes map to traceable event reasons

## Phase 2C: Hybrid Improvement (Week 3)

Deliverables:

- Feature engineering for risk model
- ML model training and validation
- Rule + ML fusion strategy
- Calibration routine for mount orientation variation

Exit criteria:

- Hybrid outperforms baseline on agreed metrics
- No loss in explainability requirements

## Phase 2D: Hardening and Demo (Week 4)

Deliverables:

- Stress tests on edge cases
- Confidence-gated fallback behavior
- Final demo scenario with replay and live scoring
- Technical report and pitch-ready evidence

Exit criteria:

- Stable runtime in repeated trials
- Clear baseline vs hybrid comparison with numbers

## 8. Metrics and Targets

Primary:

- Event F1 score per event class
- False positive rate per hour
- Mean absolute error vs expert risk rating (if available)
- Score variance under repeated runs of same route

Additional selection-grade metrics:

- Stability delta across mount conditions.
- Penalty share from low-confidence events (should remain low).
- Fairness spread across road classes after normalization.
- Explainability completeness and evidence consistency rate.
- Cross-city generalization score on unseen city test set.
- Seasonal robustness delta (monsoon vs non-monsoon).

Target suggestions:

- Event F1 >= 0.80 for core classes
- False positives <= 2 per hour for severe events
- Inference latency <= 1 second per update window
- Explainability coverage = 100 percent of score deltas

## 9. Test Strategy

Test levels:

1. Unit tests

- Filter correctness
- Threshold and hysteresis behavior
- Score clamp and weight logic

2. Integration tests

- Raw trip to final scorecard flow
- Sensor dropout handling
- Context lookup fallback behavior

3. Scenario tests

- Heavy traffic stop-go
- Sudden braking event
- Poor GPS signal tunnel segment
- Rough road false-positive protection

4. Regression tests

- Freeze benchmark trips
- Compare every release against baseline metrics

5. Split-policy validation

- Split by city and rider, not random windows.
- Keep at least one unseen city as final blind robustness set.

6. Safety fallback tests

- Verify low-confidence windows apply capped penalties only.
- Verify uncertain events remain explainable and auditable.

## 10. Risk Register and Mitigation

Risk: Sensor mount variability inflates false events.
Mitigation: Orientation calibration and adaptive thresholds.

Risk: GPS noise causes overspeed false flags.
Mitigation: Speed smoothing and map-confidence gating.

Risk: Model becomes black-box and loses trust.
Mitigation: Keep score impacts event-driven and explainable.

Risk: Limited labeled data for corner cases.
Mitigation: Hard-negative mining and iterative relabeling.

Risk: Runtime instability on lower-end phones.
Mitigation: Lightweight features, quantized model, profiling.

Risk: Users game thresholds by oscillating just below hard limits.
Mitigation: Persistence-aware escalation and trajectory-level behavior scoring.

Risk: Fairness claims remain subjective without diagnostics.
Mitigation: Add fairness dashboard and publish per-condition stability metrics.

## 11. Team Work Breakdown

Suggested roles:

1. Data and telemetry engineer

- Ingestion pipeline, schema, preprocessing stability

2. Detection and scoring engineer

- Rule engine, scoring logic, explainability layer

3. ML engineer

- Feature design, model training, calibration

4. QA and demo engineer

- Scenario tests, benchmark tracking, demo preparation

## 12. Demo Narrative

Show in this order:

1. Raw trip replay with synchronized telemetry.
2. Real-time detected events with confidence and severity.
3. Score movement with exact reasons.
4. Baseline vs hybrid quantitative comparison.
5. Coaching summary with rider-specific improvements.

## 13. Stage 1 PPT Checklist (Submit First)

- Problem statement and opportunity size
- Limitations of current solutions
- Prior-model failure matrix with mitigation mapping
- Proposed PS3 architecture
- Event taxonomy and scoring logic
- Explainability and fairness approach
- Validation methodology and metrics
- Risk analysis and mitigation
- Competitive differentiation with measurable proof points
- Business impact and scalability
- Post-selection implementation roadmap

## 14. Stage 2 Implementation Deliverables (Only if Selected)

- PS3 architecture diagram
- Event taxonomy and scoring specification
- Baseline implementation and metrics
- Hybrid implementation and improvement metrics
- Explainable scorecard report output
- Test report with edge-case outcomes
- Final presentation with deployment path

## 15. Immediate Action Items (Now, for PPT)

1. Freeze PPT storyline in 3 parts: problem, solution, validation.
2. Finalize architecture and scoring visuals for slides.
3. Prepare quantified expected impact and measurable KPIs.
4. Add phased roadmap that clearly separates selection vs implementation.
5. Rehearse pitch and prepare likely Q&A responses.
