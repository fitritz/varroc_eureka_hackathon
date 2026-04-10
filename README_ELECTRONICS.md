# Electronics Team README (PS3)

This document is for the hardware/electronics student team.
Goal: verify whether the PS3 sensing plan is physically feasible, affordable, and reliable.

Software team will build the algorithms and scoring pipeline.
Electronics team must verify sensor applicability and provide validated data.

## 1. Team Split and Responsibilities

Software team (students):

- Define data schema and software interfaces
- Build preprocessing, event detection, scoring, and explainability
- Build validation scripts and dashboards

Electronics team (students):

- Select sensors and mounting design
- Validate sensor range, sampling rate, noise, and drift
- Confirm power and communication stability
- Deliver sensor data in agreed format
- Sign off whether each event is measurable in real riding conditions

## 2. What Hardware Team Must Verify

This section directly addresses common failure points from earlier telematics systems (noise, mount bias, and unstable speed signals).

For every proposed sensor, verify:

1. Is it available and affordable for prototype use?
2. Is sampling rate sufficient for ride dynamics?
3. Is noise level acceptable after basic filtering?
4. Is mounting practical on a two-wheeler?
5. Is vibration tolerance acceptable?
6. Is data stable during real road tests?
7. Is synchronization possible with GPS timestamps?

Mandatory output from hardware team:

- Applicable: Yes/No
- Constraints: clear technical limits
- Recommendation: use / replace / optional

## 2A. Prior-Model Failure Checks (Must Report)

For each ride batch, hardware team must report:

1. Noise-induced event risk

- How often vibration bursts could look like harsh braking/cornering.

2. Mount-bias risk

- Variance in measured acceleration/rotation across mount positions.

3. GPS overspeed risk

- Frequency of unrealistic speed spikes and recovery lag.

4. Sync integrity risk

- Timestamp misalignment distribution between IMU and GPS.

These checks are mandatory because many earlier models fail precisely on these points.

## 3. Minimum Sensor Set (Required)

Required sensors for baseline PS3:

1. 6-axis IMU (accelerometer + gyroscope)
2. GPS module (speed, location, heading)

Optional but useful:

1. Magnetometer (orientation support)
2. Barometer (road gradient support)

## 4. Sensor Technical Targets

Use these as acceptance targets.

IMU targets:

- Accelerometer range: at least +/-8g
- Gyroscope range: at least +/-500 deg/s
- Effective sampling rate: 50 to 100 Hz minimum
- Timestamp precision: 10 ms or better
- Dropout rate: less than 1% per ride

GPS targets:

- Update rate: at least 5 Hz (10 Hz preferred)
- Speed stability: no frequent spikes in steady movement
- Cold start and reacquisition behavior documented
- Signal drop behavior recorded (tunnels, dense streets)

System targets:

- Sensor and GPS timestamp alignment error: less than 100 ms
- End-to-end packet loss: less than 1%
- Stable power without sensor reset events

## 5. Mounting and Mechanical Validation

Hardware team must test at least 3 mounting conditions:

1. Rigid dashboard mount
2. Handlebar mount
3. Loose/noisy mount condition (stress case)

For each mount, provide:

- Vibration profile notes
- Bias drift observations
- Practicality score (1 to 5)
- Recommendation for production-like mounting

India route requirement:

- Include test routes with potholes, speed breakers, temporary diversions, and mixed traffic density.

## 6. Event Feasibility Validation Matrix

Hardware team must confirm whether the following events are measurable with confidence.

1. Harsh braking

- Feasibility by sensors: Yes/No
- Notes: deceleration clarity, false spikes, braking distinguishability

2. Aggressive acceleration

- Feasibility by sensors: Yes/No
- Notes: throttle surge detectability, noise impact

3. Risky cornering

- Feasibility by sensors: Yes/No
- Notes: roll/yaw detectability, mount impact

4. Overspeeding (with map speed limit)

- Feasibility by sensors: Yes/No
- Notes: GPS stability, speed jitter

5. Weaving/instability proxy

- Feasibility by sensors: Yes/No
- Notes: lane-level limitation, confidence expectations

6. Pothole and speed-breaker disturbance handling

- Feasibility by sensors: Yes/No
- Notes: can the system separate road disturbance spikes from risky rider behavior

## 7. Data Interface Contract (Hardware to Software)

Hardware team must export data in CSV or JSON with these fields:

- timestamp_ms
- accel_x, accel_y, accel_z (m/s^2)
- gyro_x, gyro_y, gyro_z (deg/s)
- gps_lat, gps_lon
- gps_speed_mps
- gps_heading_deg
- quality_flag (0 or 1)
- mount_id
- ride_id

Rules:

- Timestamps must be monotonic.
- Units must match exactly.
- Missing values must be explicit (null), not silent.
- One ride = one unique ride_id.

## 8. Hardware Sign-Off Checklist

Electronics team signs off only when all are complete:

1. Sensor BOM finalized with part numbers
2. Sampling rates verified in real runs
3. Data format validated against interface contract
4. Synchronization quality validated
5. Mounting recommendation finalized
6. Event feasibility matrix completed
7. Known limitations documented
8. Prior-model failure check report attached (Section 2A)

Sign-off format:

- Status: Approved / Approved with constraints / Not approved
- Date:
- Team members:
- Final notes:

## 9. Risk and Fallback Plan

If IMU quality is poor:

- Increase filtering and reduce event sensitivity
- Restrict to high-confidence events only

If GPS is unstable:

- Confidence-gate overspeed events
- Skip scoring in low-confidence windows

If road disturbance dominates (pothole/diversion corridors):

- Apply uncertain-event mode with capped penalties
- Tag event as low-confidence until persistence criteria are met

If mounting variance is high:

- Require calibration step before ride
- Use mount-specific threshold profiles

## 10. Weekly Sync Between Teams

Weekly 30-minute sync agenda:

1. Hardware status and blockers
2. Data quality report from latest rides
3. Software feedback on missing or noisy signals
4. Decision log updates
5. Next week action owners

## 11. Final Decision Rule

Software implementation proceeds only on events marked feasible by hardware team.
If an event is not feasible with current sensors, it must be:

1. Deferred, or
2. Replaced with a proxy event, or
3. Marked optional in final scope.

This avoids over-promising in PPT and keeps implementation realistic.
