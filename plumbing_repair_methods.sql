CREATE TABLE plumbing_repair_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    repair_method TEXT NOT NULL
);

INSERT INTO plumbing_repair_methods (service_name, repair_method) VALUES
('Fixing Leaks and Clogs', 'For leaks, first shut off the water supply. Clean the area around the leak, then apply plumber''s tape around the threads of the leaking pipe or joint. For clogs, use a plunger to create a seal over the drain and push down repeatedly to dislodge the blockage. If the plunger doesn’t work, use a drain snake to reach deeper clogs. Regularly pour boiling water down the drain to prevent future clogs.'),
('Repairing or Replacing Faucets, Sinks, and Toilets', 'To fix a leaky faucet, start by turning off the water supply. Remove the faucet handle, then replace the worn washer or O-ring inside. For sinks, check for and tighten any loose connections. For toilet repairs, check the flapper and fill valve; replace any worn parts. Regular maintenance includes tightening bolts and checking for leaks around seals.'),
('Water Heater Repair or Installation', 'For minor water heater issues, check the thermostat settings and reset if necessary. If there’s no hot water, the heating element may need replacement. Flush the tank annually to remove sediment buildup. If the heater leaks, check for loose connections or cracks in the tank, which may need professional replacement if severe.');
