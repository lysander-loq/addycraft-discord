CREATE TABLE IF NOT EXISTS music_vol (
    guild INTEGER PRIMARY KEY,
    volume INTEGER NOT NULL DEFAULT 100
);
CREATE TABLE IF NOT EXISTS kv_bl (
    key INTEGER PRIMARY KEY,
    data BLOB NOT NULL
)   -- Optional database for storing arbitrary userid:blob data, visible with /whoami