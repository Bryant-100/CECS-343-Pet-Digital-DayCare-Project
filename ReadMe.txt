AccountManager:
(Technical)
-- ACC_FILENAME is a constant string that allows us to easily change csv filename if desired
-- currently, the csv format is:
-- logout() is currently empty
username,id
(Conceptual)
-- id is a 5-digit unique randomly generated (random library) number (10000-99999) (values under 10000 unaccounted for)
-- username is unique (which beckons question of usage for Id in the first place)
------ I decided to keep id just in case, the whole password thing is too much given our current manpower
-- composition/aggregation relationship to Account

Account:
-- its creation simplify future/potential modifications (i.e password)