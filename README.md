# AddyCraft Discord Bot

Developed by: Mahler von Loqerlien

Deployed/Hosted by: Adzel Firestar
## How to deploy:

Open a terminal on your (preferrably linux) machine and paste:
```
git clone https://github.com/mahler-loq/addycraft-discord
cd addycraft-discord
python3 -m venv pyvenv
source pyvenv/bin/activate
pip install -r requirements.txt
```
Now with `python3 main.py`, you will be able to deploy the bot, STDOUT/STDERR can be forwarded to a logfile if desired.
It is recommended to adjust `./config.py` before a first run

## Particular Paths:
- `src/cogs/admin.py` -> Panel-less bot administration
- `src/cogs/dummy.py` -> Template for new cogs
- `src/cnst.py` -> Hardcoded constants
- `src/helpers.py` -> Helper functions, permission system
- `src/dbtables.sql` -> SqlDB INIT script (table C-I-N-E list)
- `config.py` -> Global configuration
- `fixedstr.py` -> Hardcoded strings that are reused across scriptfiles
- `main.py` -> main script, starts the dance party
- `ongoing_work_notes.md` -> self explainatory (me dumping the details of what i have to do next)
- `requirements.txt` dependency list (PIP)
- `src/**` -> the actual source files :)