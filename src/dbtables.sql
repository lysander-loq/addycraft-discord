CREATE TABLE IF NOT EXISTS music_vol (
    guild INTEGER PRIMARY KEY,
    volume INTEGER NOT NULL DEFAULT 100
);  -- Music volume settings per guild
CREATE TABLE IF NOT EXISTS mod_audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT, --case id
    moderator INTEGER NOT NULL, --who triggered the audited action
    privilege_tier INTEGER NOT NULL DEFAULT 0, --rank of moderator at time of exectuion
    moderated INTEGER DEFAULT NULL, --targeted user id, if any
    action_id INTEGER NOT NULL, --int referring a later defined enum with al list of all audited actions 
    reason TEXT NOT NULL, --reason for action carried, cannot be modified by lt
    notes TEXT DEFAULT NULL, --notes that can be modified and read by staff
    ht_notes TEXT DEFAULT NULL, --notes that can be modified by owners & ht & read by staff
    refmedia BLOB DEFAULT NULL, --attached media (magicval sep BLOBs)
    refids TEXT DEFAULT NULL, --referenced discord IDs (comma sep strs)
    tstamp INTEGER NOT NULL --unix offset timestamp
);
CREATE TABLE IF NOT EXISTS kv_bl (
    uid INTEGER PRIMARY KEY,
    dat BLOB NOT NULL
)   -- Optional database for storing arbitrary userid:blob data (visible with /whoami)