-- GET ALL FIREARMS WITH DETAILS
SELECT ft.type, f.manufacturer, f.model, fd.magazine_capacity, f.barrel_length, c.short_name AS caliber, f.trigger_action, fd.sight_type, fd.suppressed
FROM firearm AS f
    INNER JOIN firearm_type AS ft
        ON   ft.id = f.type_id
    INNER JOIN caliber AS c
        ON c.id = f.caliber_id
    LEFT OUTER JOIN firearm_details AS fd
        ON fd.id = f.firearm_details_id
ORDER BY ft.type, f.manufacturer, f.model, f.barrel_length;