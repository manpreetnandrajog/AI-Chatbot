CREATE TABLE hvac_repair_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    repair_method TEXT NOT NULL
);

INSERT INTO hvac_repair_methods (service_name, repair_method) VALUES
('Repairing or Servicing Heating and Cooling Systems', 'Regularly replace air filters to ensure efficient airflow. Clean the evaporator and condenser coils to remove dust and debris. Check the thermostat settings and batteries. Inspect ductwork for leaks and seal with foil tape if necessary. If the system isn’t cooling or heating properly, a refrigerant recharge or professional service may be required.'),
('Installing New HVAC Units', 'Installation of a new HVAC unit is complex and typically requires professional service. However, ensure the unit is properly sized for your home. Clear the installation area and provide proper ventilation. Connect the unit to existing ductwork and electrical systems. Follow manufacturer instructions carefully. Regular maintenance includes cleaning filters and inspecting ducts.'),
('Cleaning and Maintaining Ducts', 'Remove vent covers and use a vacuum with a long hose to clean inside the ducts. For deeper cleaning, consider renting a duct-cleaning machine. Inspect ducts for leaks and seal any gaps with duct tape or mastic sealant. Regular cleaning improves air quality and system efficiency. Professional duct cleaning is recommended every few years.');
