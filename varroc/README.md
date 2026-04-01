# Varroc Hackathon Playbook (Selected Problem Statement: PS3)

This workspace is now focused only on PS3: Accurate Two-Wheeler Driving Behavior Score.

## Final Selection

- Selected statement: PS3
- Objective: Build an explainable, context-aware, fair rider behavior scoring system for two-wheelers.

## What Is Included

- PS3 problem context and PPT submission focus
- Two-stage strategy: idea submission first, implementation after selection
- Detailed action plan in PS3_ACTION_PLAN.md
- Hardware feasibility and sensor validation guide in README_ELECTRONICS.md

## What Was Removed

- PS2 and PS6 problem content from active planning scope
- PS2 and PS6 architecture assets
- Multi-problem comparison artifacts

## PS3 System Vision

The solution must convert raw ride telemetry into:

1. Event-level safety detections (harsh braking, aggressive acceleration, risky cornering, overspeeding, weaving)
2. Segment-level and trip-level safety score
3. Explainable feedback for every score change
4. Actionable post-ride coaching suggestions

## Core Success Metrics

- Event detection precision and recall
- False alerts per hour
- Score stability across phone mount variations
- Inference latency for near-real-time feedback
- Explainability coverage (percentage of score changes with clear reason)

## Submission Strategy

Stage 1 (Current):

- Submit a strong PPT with complete concept, architecture, methodology, scoring design, validation strategy, impact, and roadmap.
- No full implementation required in this stage.

Stage 2 (Only if selected):

- Start technical implementation, benchmarking, testing, and final demo build.

## Detailed Plan

Use the complete stage-wise plan here:

- PS3 action plan: PS3_ACTION_PLAN.md

## Repository Structure

- README.md
- PS3_ACTION_PLAN.md
- README_ELECTRONICS.md
- assets/images/ps3-architecture.svg
- scripts/readme_to_pdf.py

## Immediate Next Execution Steps (PPT Phase)

1. Finalize the full PS3 concept narrative and problem framing.
2. Freeze scoring definition and event taxonomy for presentation.
3. Build slide-level architecture and data flow visuals.
4. Add validation plan, risk register, and expected impact metrics.
5. Add a clear post-selection implementation roadmap.
