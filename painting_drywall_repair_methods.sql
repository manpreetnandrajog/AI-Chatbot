CREATE TABLE painting_drywall_repair_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    repair_method TEXT NOT NULL
);

INSERT INTO painting_drywall_repair_methods (service_name, repair_method) VALUES
('Interior and Exterior Painting', 'Prepare surfaces by cleaning and sanding to remove old paint or debris. Apply primer to ensure paint adheres well. Use high-quality paint and brushes for a smooth finish. Apply paint in thin, even coats, allowing each coat to dry before adding the next. Protect surrounding areas with painter’s tape and drop cloths.'),
('Repairing or Replacing Damaged Drywall', 'For small holes, use a patch kit with a self-adhesive mesh. Apply joint compound over the patch, smooth it out, and sand when dry. For larger holes, cut a piece of drywall to fit the hole, secure it with screws, and cover with joint compound. Sand smooth and paint to match the surrounding wall.'),
('Wallpaper Removal and Installation', 'Use a wallpaper steamer or a solution of water and wallpaper remover to soften the adhesive. Peel off the wallpaper, starting at a corner. Clean the wall to remove any remaining adhesive. For installation, measure and cut wallpaper to size, apply adhesive to the back, and carefully align and smooth onto the wall, removing air bubbles as you go.');
