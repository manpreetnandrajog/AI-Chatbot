CREATE TABLE carpentry_repair_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    repair_method TEXT NOT NULL
);

INSERT INTO carpentry_repair_methods (service_name, repair_method) VALUES
('Repairing or Replacing Doors and Windows', 'For sticking doors, tighten hinge screws and apply lubricant to the hinges. Check for and replace any worn weatherstripping around doors and windows. If the door or window is damaged, remove the old unit and measure the opening for a replacement. Install the new door or window, ensuring it is level and secure. Apply caulk around the frame to seal gaps.'),
('Building or Fixing Cabinetry and Shelving', 'Tighten any loose screws and replace damaged hardware. Use wood filler to fill in cracks or holes, then sand smooth. For sagging shelves, add additional support brackets underneath. When building new cabinetry, measure and cut wood to size, assemble using screws and wood glue, and finish with paint or stain for a polished look.'),
('Structural Repairs and Modifications', 'Reinforce weak joints with metal brackets or additional wood supports. For termite damage, remove and replace affected wood, treating the area with a termite deterrent. Consult a structural engineer for major modifications. Regular inspections and maintenance can prevent small issues from becoming major structural problems.');
