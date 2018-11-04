# IGSN Borehole Matcher

This library matches boreholes from state surveys with those in the GA database. It does this by finding all GA  boreholes within a 500m radius of the coordinates from each state borehole. It then finds the similarity between strings for the set returned.

- For those boreholes that match exactly on name one-to-one within the radius, these are exported to an 'EXACT' spreadsheet.
- For one-to-one matches that have a fuzzy name match, these are exported to a 'FUZZY' spreadsheet.
- For multiple matches of one of the above (but not both, a single exact match trumps multiple fuzzy matches), these are exported to a 'MULTIPLE' spreadsheet
- Any that *don't* match are exported to a NO\_MATCHES spreadsheet